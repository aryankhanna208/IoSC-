FROM python:latest
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


RUN python ./manage.py migrate
CMD [ "python", "./manage.py" , "runserver", "0.0.0.0:8000"]
EXPOSE 8000
