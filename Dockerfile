FROM python:3.8-slim-buster

WORKDIR /usr/src/app
SHELL [ "/bin/bash", "-c" ]
RUN chmod 777 /usr/scr/app

RUN apt update && apt upgrade -y
COPY start /start
CMD ["/bin/bash", "/start"]
