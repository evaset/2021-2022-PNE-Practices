import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"
PORT = 8080
GENES = {"SRCAP":"ENSG00000080603",
         "FRAT1":"ENSG00000165879",
         "ADA":"ENSG00000196839",
         "FXN":"ENSG00000165060",
         "RNU6_269P":"ENST00000391077",
         "MIR633":"ENSG00000207552",
         "TTTY4C":"ENSG00000228296",
         "RBMY2YP":"ENSG00000227633",
         "FGFR3":"ENSG00000068078",
         "KDR":"ENSG00000128052",
         "ANK2":"ENSG00000145362"}

def convert_message(base_count, percent_count):
    message = ""
    for k, v in base_count.items():
        message = message + f"{k}:  {base_count[k]} ({percent_count[k]}%)" + "<br>"
    return message

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

def make_ensembl_request2(url):
    SERVER = "rest.ensembl.org"
    # params shuld be &param=1
    ARGUMENT = "?feature_type=Variation;content-type=application/json"
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
            except KeyError:
                contents = Path("html/Error.html").read_text()
        elif path == "/karyotype":
            try:
                class_specie = arguments["specie"][0]
                dict_answer = make_ensembl_request("/info/assembly/"+class_specie)
                list_chromosomes = dict_answer["karyotype"]
                contents = read_html_file("karyotype" + ".html") \
                    .render(context={"list_chromosomes": list_chromosomes})
            except KeyError:
                contents = Path("html/Error.html").read_text()
            except ValueError:
                contents = Path("html/Error.html").read_text()
        elif path == "/chromosomeLength":
            try:
                class_specie = arguments["specie"][0]
                n_chromosome = int(arguments["chromo"][0])
                dict_answer = make_ensembl_request("/info/assembly/" + class_specie)
                list_chromosomes = dict_answer["top_level_region"][n_chromosome]["length"]
                contents = read_html_file("chromosomeLength" + ".html")\
                    .render(context={"chromosome_length": list_chromosomes})
            except KeyError:
                contents = Path("html/Error.html").read_text()
        elif path == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                ID = GENES[gene]
                dict_answer = make_ensembl_request("/sequence/id/" + ID)
                list_seq = dict_answer["seq"]
                contents = read_html_file("geneSeq" + ".html") \
                    .render(context={"list_seq": list_seq})
            except KeyError:
                contents = Path("html/Error.html").read_text()
            except ValueError:
                contents = Path("html/Error.html").read_text()
        elif path == "/geneInfo":
            try:
                gene = arguments["gene"][0]
                ID = GENES[gene]
                dict_answer = make_ensembl_request("/sequence/id/" + ID)
                gene_info_list = dict_answer["desc"].split(":")
                gene_start = int(gene_info_list[3])
                gene_end = int(gene_info_list[4])
                gene_length = gene_end - gene_start
                gene_chromosome_name = gene_info_list[1]
                #gene_length2 = len(dict_answer["seq"])
                contents = read_html_file("geneInfo" + ".html") \
                    .render(context={"gene_start": gene_start, "gene_end": gene_end, "gene_length": gene_length,"ID": ID, "gene_chromosome_name": gene_chromosome_name})
            except KeyError:
                contents = Path("html/Error.html").read_text()
            except ValueError:
                contents = Path("html/Error.html").read_text()
        elif path == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                ID = GENES[gene]
                dict_answer = make_ensembl_request("/sequence/id/" + ID)
                list_seq = dict_answer["seq"]
                seq = Seq(list_seq)
                total_length = seq.count()
                base_percentage = seq.percent(total_length)
                message = convert_message(total_length, base_percentage)
                gene_length = len(list_seq)
                contents = read_html_file("geneCalc" + ".html") \
                    .render(context={"gene_length": gene_length, "message": message})
            except KeyError:
                contents = Path("html/Error.html").read_text()
            except ValueError:
                contents = Path("html/Error.html").read_text()
        elif path == "/geneList":
            try:
                CHROMO = arguments["chromo"][0]
                START = arguments["start"][0]
                END = arguments["end"][0]
                dict_answer = make_ensembl_request2("/phenotype/region/homo_sapiens/" + CHROMO + ":" + START + "-" + END)
                print(dict_answer)
                genes_names = []
                for d in dict_answer:
                    phenotype = d["phenotype_associations"]
                    print("phenotype: ",phenotype)
                    try:
                        for e in phenotype:
                            genes_names.append(e["attributes"]["associated_gene"])
                            print(genes_names)
                    except KeyError:
                        pass
                if len(genes_names) == 0:
                    contents = Path("html/Error.html").read_text()
                else:
                    contents = read_html_file("geneList" + ".html") \
                        .render(context={"list_names": genes_names})
            except KeyError:
                contents = Path("html/Error.html").read_text()
            except ValueError:
                contents = Path("html/Error.html").read_text()
            except TypeError:
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