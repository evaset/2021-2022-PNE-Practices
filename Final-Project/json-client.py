
import http.client
import json
import termcolor

def print_info(data1):
    for k,v in data1.items():
        print(k,":",v)

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
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1) 
    print_info(data1)

    conn.request("GET", "/karyotype?specie=human&json=1")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print_info(data1)

    conn.request("GET", "/chromosomeLength?specie=human&chromo=1&json=1")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print_info(data1)

    conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print_info(data1)

    conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print_info(data1)

    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print_info(data1)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()



