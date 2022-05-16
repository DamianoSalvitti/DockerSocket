import socket
import subprocess


# Socket ready to receive commands from the Client
def sub_server(address, backlog=1):  # Backlog: max queue of admitted connections not already accepted
    try:
        s = socket.socket()  # Client socket creation
        s.bind(address)  # Socket connection to the host's address and the desired port
        s.listen(backlog)  # Waiting for the Client connection
        print("Initialized server: now listening.")
        connection, client_address = s.accept()  # Client acceptance
        print(f"Server - Client connection established: {client_address}")
        receive_commands(connection)
    except socket.error as err:
        print(f"\nSomething went wrong: \n{err}")
        print("Trying to reinitialize the server...")
        sub_server(address, backlog=1)  # Retry


# Commands computing
def receive_commands(connection):
    counter = 1
    while counter <= 5:
        print(f"Service {counter}/5 is being executed.")
        # Get Client's request
        request = connection.recv(4096)  # 4096 is the buffer size: maximum amount of data to be received at once
        # Answer computing
        answer = subprocess.run(request.decode(encoding='utf-8').strip(), shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data = answer.stdout + answer.stderr
        # Sending answer to the Client
        connection.send(data)
        # Counter updating
        counter += 1
    print(f"The server has been automatically blocked for security reasons.")

    # SINGLE INPUT
    # # Get Client's request
    # request = connection.recv(4096)  # 4096 is the buffer size: maximum amount of data to be received at once
    # # Answer computing
    # answer = subprocess.run(request.decode(encoding='utf-8').strip(), shell=True,
    #                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # data = answer.stdout + answer.stderr
    # # Sending answer to the Client
    # connection.send(data)


if __name__ == '__main__':
    sub_server(("", 15000))
