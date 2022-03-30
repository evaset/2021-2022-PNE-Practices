import socket
import colorama
from Seq1 import Seq

def convert_message(base_count, percent_count):
    message = ""
    for k,v in base_count.items():
        message = message+ f"{k}:  {base_count[k]} ({percent_count[k]}%)"+ "\n"
    return message

seq_list = ["AAA","AGG","ACC","AGC", "ACG"]

PORT = 6123
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()

        splitted_command = msg.split(" ")
        command = splitted_command[0]

        if command != "PING":
            argument = splitted_command[1]
        print(colorama.Fore.GREEN + f"{command} command!")

# -- manage message
        if command == "PING":
            response = "OK!\n"
            print(colorama.Fore.WHITE + response)
        elif command == "GET":
            try:
                argument = int(splitted_command[1])
                if argument in range(0,5):
                    response = seq_list[argument]
                else:
                    response = "Number not in range"
            except ValueError:
                response = "Must be a number between 0 and 4"
            print(colorama.Fore.WHITE + response)

        elif command == "INFO":
            seq = Seq(argument)
            count = seq.count()
            percent = seq.percent(count)
            response = convert_message(count, percent)
            response = f"Total length: {str(seq.len())}\n{response}\n"
            response = "Sequence:" + argument + "\n" + response
            print(colorama.Fore.WHITE + response)

        elif command == "COMP":
            seq = Seq(argument)
            response = seq.complement()
            print(colorama.Fore.WHITE + response)

        elif command == "REV":
            response = argument[::-1]
            print(colorama.Fore.WHITE + response)

        elif command == "GENE":
            seq = Seq()
            response = seq.read_fasta(argument)
            print(colorama.Fore.WHITE + response)

        elif command == "OPE":
            seq = Seq(argument)
            dict_count = seq.count()
            response = str(seq.operation(dict_count))
            if response == "null":
                response = "We could not multiply the bases since the sequence is not correct."
            print(colorama.Fore.WHITE + response)

        else:
            response = "This command is not available in the server.\n"

        cs.send(response.encode())
        cs.close()