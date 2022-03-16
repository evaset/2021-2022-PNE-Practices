import socket
import colorama
from Seq1 import Seq

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v) + "\n"
    return message

seq_list = ["AAA","AGG","ACC","AGC"]

PORT = 6123
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        print(colorama.Fore.RESET)

# -- manage message
        if command == "PING":
            response = "OK!\n"
            print(colorama.Fore.WHITE + response)
            print(colorama.Fore.RESET)

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
            print(colorama.Fore.RESET)

        elif command == "INFO":
            seq = Seq(argument)
            count = seq.count()
            percent = seq.percent(count)
            response1 = convert_message(count)
            response2 = convert_message(percent)
            response3 = f"Total length: {str(seq.len())}\n {response1}\n {response2}"
            response = "Sequence:" + argument + "\n" + response3

        elif command == "COMP":
            seq = Seq(argument)
            response = seq.complement()

        elif command == "REV":
            response = argument[::-1]

        elif command == "GENE":
            pass

        else:
            response = "This command is not available in the server.\n"

        cs.send(response.encode())
        cs.close()