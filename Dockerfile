
FROM python:3.10

# python output set straight to the terminal 
# without buffering it first
#ENV PYTHONUNBUFFERED 1

# create root directory for mis app in the container
RUN mkdir /mis_app

# Set the working directory to /mis_app
WORKDIR /mis_app

# Copy current directory contents into container at /mis_app
ADD . /mis_app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN pip install gunicorn
