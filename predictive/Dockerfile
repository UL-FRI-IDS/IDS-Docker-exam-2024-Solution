FROM python:3.10-slim

# copy the requirements file
COPY requirements.txt .

# install the dependencies
RUN pip3 install -r requirements.txt

COPY predictive.py .

# command to run on container start
CMD [ "python", "./predictive.py" ]
