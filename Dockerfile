FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY src/ .

RUN mkdir cache

CMD ["python3", "main.py"]