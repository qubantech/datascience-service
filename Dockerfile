FROM python:3.8-alpine
RUN mkdir code
ADD requirements.txt main.py /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
