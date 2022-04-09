FROM python:3
RUN mkdir code
ADD flask_server.py requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP flask_server.py
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]