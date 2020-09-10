# Base Image
FROM python:3.7
ENV PYTHONUNBUFFERED 1

# create and set working directory
RUN mkdir /code/
COPY src/ /code/
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code/

RUN echo "-------------- WORD ------------ \n \n \n \n \n "

# Install system dependencies
RUN apt-get update

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

CMD ['bash']
