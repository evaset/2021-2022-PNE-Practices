import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"

SEQ_LIST = ["AAAT", "GGCT", "AGGT", "ACGT", "TGGT"]
GENE_LIST = ["U5", "ADA", "FRAT1", "RNU6_269P","FXN" ]
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents


def convert_message(base_count, percent_count):
    message = ""
    for k,v in base_count.items():
        message = message+ f"{k}:  {base_count[k]} ({percent_count[k]}%)"+ "<br>"
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
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was: ", self.path)
        print("the new path is: ", url_path.path)
        print("The argument is: ", arguments)

        if self.path == "/":
            contents = read_html_file("form-1.html").render(context={"n_seq": len(SEQ_LIST), "gene": GENE_LIST})
        elif self.path == "/favicon.ico":
            contents = Path("html/form-1.html").read_text()
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_seq = int(arguments["n_seq"][0])
            seq = SEQ_LIST[n_seq]
            contents = read_html_file(path[1:] + ".html").render(context={"n_seq": n_seq, "seq": seq})
        elif path == "/gene":
            n_gene = arguments["n_gene"][0]
            seq = Seq()
            seq.read_fasta(n_gene)
            contents = read_html_file(path[1:] + ".html").render(context={"n_gene": n_gene, "seq": seq.strbases})
        elif path == "/operation":
            sequence = arguments["seq"][0]
            operation = arguments["op"][0]
            seq = Seq(sequence)
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence, "operation": operation, "result": seq.reverse() })
            elif operation == "comp":
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence, "operation": operation, "result": seq.complement()})
            else:
                count = seq.count()
                percent = seq.percent(count)
                response = convert_message(count, percent)
                response = f"Total length: {str(seq.len())}<br>{response}<br>"
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence, "operation": operation, "result": response})
        else:
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
        print("Stopped by the user")
        httpd.server_close()