#./Dockerfile
FROM python:3 

WORKDIR /usr/src/app 

COPY requirements.txt ./ 

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000   

#CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "example.wsgi:application"]  