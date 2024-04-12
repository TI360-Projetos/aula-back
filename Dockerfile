FROM python:3.9.10-alpine3.14
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","api_fake.py"]