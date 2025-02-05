FROM python:3.12


ENV DISPLAY=:99


RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./ .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]

