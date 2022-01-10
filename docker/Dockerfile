FROM python3:alpine
WORKDIR /opt/haydarctl/
COPY ./src/ .
COPY main.py requirements.txt .
RUN pip3 install -t requirements.txt