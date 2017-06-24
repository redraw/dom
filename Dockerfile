FROM python:3.5

ENV PUP_VERSION 0.4.0

RUN apt-get update && \
    apt-get install -y unzip && \
    wget -O pup.zip https://github.com/ericchiang/pup/releases/download/v${PUP_VERSION}/pup_v${PUP_VERSION}_linux_amd64.zip && \
    unzip pup.zip && mv pup /usr/bin && rm pup.zip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py"]
