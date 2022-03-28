FROM python:3.8-alpine
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY app.py /src/app.py
CMD ["python", "app.py"]
