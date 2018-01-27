#==============================================================================
# Dockerfile for monocker-api project
#
# Flask api for user interaction with monocker
#==============================================================================
FROM python:2

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# add flask app
COPY monocker_api/ /monocker_api

# install python libs
WORKDIR /monocker_api
RUN pip install -r requirements.txt

# add envs
ENV REGISTRY_HOSTNAME=monocker-registry-service \
    REGISTRY_PORT=80 \
    REGISTRY_ROUTE=models \
    PYTHONPATH=/:$PYTHONPATH

# open flask app port
EXPOSE 80

# dev port
EXPOSE 8123

# start flask app
CMD ["python", "-m", "monocker_api.app"]
#==============================================================================