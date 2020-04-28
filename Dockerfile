FROM python:3.7-alpine
MAINTAINER carmelo.califano@gmail.com

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY appcalc3.py .
EXPOSE 5000

ENTRYPOINT ["python3","./appcalc3.py"]
