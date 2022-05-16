FROM python

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install net-tools

COPY sub_server.py /py_socket/

WORKDIR /py_socket
