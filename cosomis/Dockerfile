
FROM python:3.10-bullseye

# python output set straight to the terminal 
# without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for mis app in the container
RUN mkdir /mis_app

# set the working directory to /mis_app
WORKDIR /mis_app

# copy current directory contents into container at /mis_app
COPY . /mis_app/

# update pip
RUN pip install -U pip

COPY requirements.txt .

# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN pip install gunicorn
RUN rm cosomis/local_settings.py

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "cosomis.wsgi:application"]