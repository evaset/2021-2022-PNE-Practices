import http.client
import json
from Seq1 import Seq

def convert_message(base_count, percent_count):
    message = ""
    for k,v in base_count.items():
        message = message+ f"{k}:  {base_count[k]} ({percent_count[k]}%)"+ "\n"
    return message

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



SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
for k,v in GENES.items():
    ID = GENES[k]

    print(f"\nServer: {SERVER}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
            #print("url", ENDPOINT + ID + PARAMS)
        conn.request("GET", ENDPOINT + ID + PARAMS)
            # request only need endpoint and params NO THE SERVER
            # -- Read the response message from the server
        r1 = conn.getresponse()
            # -- Print the status line
        print("URL:", ENDPOINT + ID + PARAMS)
        print(f"Response received!: {r1.status} {r1.reason}\n")
            # -- Read the response's body
        data1 = r1.read().decode("utf-8")
            #print(f"CONTENT: {data1}")
        data1 = json.loads(data1)
        print("Gene:", k)
        print("Description:", data1["desc"])
        seq = Seq(data1["seq"])
        print("Total lengh:", seq.len())
        count = seq.count()
        percent = seq.percent(count)
        response = convert_message(count, percent)
        print(response, end="")
        print("Most frequent Base:", seq.max_val(count))

            # json.loads() transform the string into the corresponded type (integer, for example)
            # -- Print the received data


    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")