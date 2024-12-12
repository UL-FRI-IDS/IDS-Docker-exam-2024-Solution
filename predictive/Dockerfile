FROM python:3.10-slim

WORKDIR /model

# copy the requirements file
COPY requirements.txt .

# install the dependencies before copying the source code to take advantage of docker cache
RUN pip3 install -r requirements.txt

COPY model.py .

# command to run on container start
CMD [ "python", "model.py" ]
