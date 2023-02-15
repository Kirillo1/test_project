#FROM python:3.9
#
#ENV PYTHONDONTWRITEBYTECODE 1
#
#RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
#
#COPY . .
#
#











FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/test_project

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /usr/src/test_project

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
