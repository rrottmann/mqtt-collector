FROM python:3

WORKDIR /usr/src/app

RUN mkdir /data

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/data"]

CMD [ "python", "./collect.py" ]