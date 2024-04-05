FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
RUN apt update
RUN apt install iproute2 -y
CMD python greeter_server.py
