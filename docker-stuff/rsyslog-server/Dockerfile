FROM ubuntu:latest
RUN apt update 
RUN apt install rsyslog -y
COPY rsyslog.conf /etc
RUN touch /var/log/syslog
ENTRYPOINT ["rsyslogd", "-n"]
