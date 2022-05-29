FROM python:3.8

RUN apt-get update && apt-get install -y libblas-dev liblapack-dev gfortran

RUN pip install --upgrade pip
#RUN pip install numpy scipy

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -e .[dev]
RUN pip install -r requirements.txt

COPY image_match /usr/src/app/image_match
COPY templates /usr/src/app/templates
COPY *.py /usr/src/app/

CMD "python" "/usr/src/app/main.py"
