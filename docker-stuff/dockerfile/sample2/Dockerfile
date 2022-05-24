FROM ubuntu

RUN apt-get update
RUN apt-get -y install python
RUN mkdir /server_query

COPY start.sh /server_query

CMD sh /server_query/start.sh
