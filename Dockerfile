FROM python:3

WORKDIR /mysite

COPY . /mysite

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME MySite

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]