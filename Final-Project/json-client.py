
import http.client
import json

def print_info(data1):
    for k,v in data1.items():
        if type(v) == list:
            print(k)
            for e in v:
                print("·",e)
        else:
            print(k,v)
PORT = 8080
SERVER = '127.0.0.1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listSpecies?limit=10&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1) 
    print("\n" + "1) List of specie in the genome database with limit 10")
    print_info(data1)

    conn.request("GET", "/karyotype?specie=human&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print("\n" + "2) Information about human karyotype:")
    print_info(data1)

    conn.request("GET", "/chromosomeLength?specie=human&chromo=1&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print("\n" + "3) Human chromosome 1 length")
    print_info(data1)

    conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print("\n" + "4) Sequence of a human gene FRAT1:")
    print_info(data1)

    conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print("\n" + "5) Information about a human gene FRAT1:")
    print_info(data1)

    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print("\n" + "6) Length and percentage of human gene FRAT1 bases:")
    print_info(data1)

    conn.request("GET", "/geneList?chromo=9&start=22125500&end=22136000&json=1")
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1= json.loads(data1)
    print("\n" + "7) Names of the genes in the chromosome 9 from 22125500 to 22136000")
    print_info(data1)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()



