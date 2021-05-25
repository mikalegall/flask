FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8 

WORKDIR /usr/src/app

COPY / .

RUN apt-get update && apt-get install -y apt-utils python3 python3-flask

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["/usr/src/app/hello.py"]
