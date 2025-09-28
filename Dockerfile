FROM python:3-slim
WORKDIR /programas/ingesta
COPY . .
RUN pip3 install -r ./requirements.txt
CMD [ "python3", "./ingesta.py" ]
