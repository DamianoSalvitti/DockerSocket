import socket
import sys


# Socket ready to send commands to the Server
def conn_sub_server(server_address):  # Server address
    try:
        s = socket.socket()  # Socket client creation
        s.connect(server_address)  # Connecting to the Server
        print(f"Successfully connected to the server: {server_address}.")
        send_commands(s)
    except socket.error as err:
        print(f"Something went wrong: \n{err}")
        sys.exit()  # Interpreter exiting


# Send commands
def send_commands(s):
    while True:
        command = input("Insert command (type \"ESC\" to close): ")
        if command == "ESC":
            print("Closing connection to server")
            s.close()  # Socket closing
            sys.exit()  # Interpreter exiting
        else:
            s.send(command.encode(encoding='utf-8').strip())  # Sending commands as byte object
            data = s.recv(4096)  # Receiving data from the Server
            print(data.decode(encoding='utf-8').strip())

    # SINGLE INPUT
    # command = "ifconfig"  # Command to be computed in the Commands Prompt
    # s.send(command.encode(encoding='utf-8').strip())  # Sending commands as byte object
    # data = s.recv(4096)  # Receiving data from the Server
    # print(data.decode(encoding='utf-8').strip())


if __name__ == '__main__':
    # IPv4 address: found by typing "ipconfig" in Windows OS
    # Examples -> Ethernet: 172.25.192.1, LAN Wi-Fi: 192.168.10.101, Container bridge: 172.17.0.2
    conn_sub_server(("172.17.0.2", 15000))
