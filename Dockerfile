
FROM python:3.8


WORKDIR /app


COPY . /app


RUN pip install flask


EXPOSE 4000


CMD ["python", "app.py"]

