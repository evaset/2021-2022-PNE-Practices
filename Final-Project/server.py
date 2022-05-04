import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"


# Define the Server's port
PORT = 8080

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def make_ensembl_request(url):
    SERVER = "rest.ensembl.org"
    # params shuld be &param=1
    ARGUMENT = "?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", url + ARGUMENT)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received:{r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    return json.loads(data1)

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
            contents = Path("html/index.html").read_text()
        elif self.path == "/favicon.ico":
            contents = Path("html/index.html").read_text()
        elif path == "/listSpecies":
            try:
                limit_species = int(arguments["limit"][0])
                dict_answer = make_ensembl_request("/info/species")
                list_species = []
                n_species = len(dict_answer["species"])
                try:
                    for i in range(limit_species):
                        list_species.append(dict_answer["species"][i]["name"])
                except IndexError:
                    for i in range(n_species):
                        list_species.append(dict_answer["species"][i]["name"])
                contents = read_html_file("list_species" + ".html")\
                    .render(context={"n_species": n_species,"limit_species": limit_species, "species": list_species})
            except ValueError:
                contents = Path("html/Error.html").read_text()

        else:
            contents = Path("html/Error.html").read_text()

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