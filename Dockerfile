FROM python:3.6-slim-bullseye as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create app directory
WORKDIR /core
COPY requirements.txt ./
RUN pip install -r requirements.txt 

# ---- Copy Files/Build ----
FROM base

WORKDIR /core

COPY ./core /core

RUN chmod -R 777 /core

LABEL org.opencontainers.image.source="https://github.com/PICT-ACM-STUDENT-CHAPTER/SES-Email-Service"

CMD  python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py shell < tools/create_superuser.py \
    && python manage.py runserver 0.0.0.0:8000