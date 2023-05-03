# build custom image based on 'python' image and to run code from 'run_get.py' inside of my container

FROM python:latest
MAINTAINER Anna Derhachova
#ENV POSTGRES_PASSWORD:123
#EXPOSE 9997:5432
COPY run_get.py .
COPY requirements.txt .
# COPY will copy files to container, RUN - will execute command and install 'requests' lib
RUN pip instal -r requirements.txt


# Command: docker build -t my_get_example .  -- will download 'python' image and based on it - create custom image 'my_get_example'