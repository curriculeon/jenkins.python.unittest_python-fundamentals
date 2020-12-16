FROM ubuntu:18.04
RUN apt-get update && \
    apt install python3 -y
ADD * /home/
WORKDIR "/home/jenkins.python.unittest_python-fundamentals"
