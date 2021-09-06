FROM python:3.9-slim


WORKDIR /workspace

COPY requirements.txt /workspace

RUN pip3 install -r requirements.txt

COPY . /workspace

WORKDIR /workspace

CMD ["python", "entrypoint.py"]