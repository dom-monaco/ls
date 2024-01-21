FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

# default path to root
ENV PATH_ARG /app/root

CMD python webserver.py ${PATH_ARG}
