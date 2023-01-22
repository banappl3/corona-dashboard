#Deriving the latest base image
FROM python:3.9


#Labels as key value pair
#LABEL Maintainer="roushan.me17"

COPY . /opt/app
WORKDIR /opt/app

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
#WORKDIR /usr/app/src

#RUN pip install -r requirements.txt


#to COPY the remote file at working directory in container
#COPY tests/unit/. ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "test_prime.py"]
