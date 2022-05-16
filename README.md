# DockerSocket
Socket connection (Server - Client) developed in Python for Docker use.

1) Type `docker-compose up --build` from the Command Prompt (the Path must reach this directory) in order to create the images *socket-server* e *socket-client*
2) Open the server container in the interactive bash mode `docker run -it --name <NAME-CONT-SERV> socket-server bash`; then the client's one `docker run -it --name <NAME-CONT-CLIENT> socket-client bash` in two different Prompt shells (**please follow this order**)
3) Run `python sub_server.py` from the Server's shell
4) Run `python sub_client.py` from the Client's shell
5) The Client can ask to the Server up to 5 available commands in a Linux Command Prompt
