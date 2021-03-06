import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

seq_list = ["AAAT", "GGCT", "AGGT", "ACGT", "TGGT"]
gen_list = ["U5", "ADA", "FRAT1", "RNU6_269P","FXN" ]
def convert_message(base_count, percent_count):
    message = ""
    for k,v in base_count.items():
        message = message+ f"{k}:  {base_count[k]} ({percent_count[k]}%)"+ "\n"
    return message
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""


        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        print(self.path)

        if len(self.requestline) > 0:
            if self.path == "/":
                contents = Path('html/form-1.html').read_text()
            elif self.path == "/favicon.ico":
                contents = Path("html/form-1.html").read_text()
            else:
                try:
                    file = self.path
                    filename = file.split("?")[0]
                    arg = file.split("?")[1]
                    arg = arg.split("=")[1]
                    print("filename: ", filename)
                    print("argument: ", arg)
                    if len(arg)<1:
                        filename = filename.removesuffix("?")
                        print(filename)
                        contents = Path("html/" + filename + ".html").read_text()
                    elif arg.isdigit():
                        contents = Path("html/" + filename + ".html").read_text().format(arg,seq_list[int(arg)])
                    elif arg in gen_list:
                        seq = Seq()
                        contents = Path("html/" + filename + ".html").read_text().format(arg,seq.read_fasta(arg))
                    elif "&" in arg:
                        sequence = arg.split("&")[0]
                        operation = self.path.split("=")[2]
                        seq = Seq(sequence)
                        if seq.valid_sequence() and len(sequence) > 0:
                            if operation == "info":
                                count = seq.count()
                                percent = seq.percent(count)
                                response = convert_message(count, percent)
                                response = f"Total length: {str(seq.len())}\n{response}\n"
                                result = "Sequence:" + sequence + "\n" + response
                            elif operation == "comp":
                                result = seq.complement()
                            elif operation == "rev":
                                result = sequence[::-1]
                            contents = Path("html/" + filename + ".html").read_text().format(sequence,operation,result)
                        else:
                            contents = Path("html/error.html").read_text()
                except IndexError:
                    filename = filename.removesuffix("?")
                    print(filename)
                    contents = Path("html/" + filename + ".html").read_text()
                except FileNotFoundError:
                    print("file not found")
                    contents = Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()