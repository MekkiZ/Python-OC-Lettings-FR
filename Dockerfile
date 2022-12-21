FROM python:3.10

WORKDIR /Python-OC-Lettings-FR

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]

