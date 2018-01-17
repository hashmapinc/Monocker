#==============================================================================
# Dockerfile for monocker-registry project
#
# Flask api with sqlite3 db (provided through a k8's PV)
#==============================================================================
FROM python:3

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# add flask app
COPY monocker_registry/ /monocker_registry

#install python libs
WORKDIR /monocker_registry
RUN pip install -r requirements.txt

#add envs
ENV REGISTRATION_FREQUENCY=60 \
    REGISTRY_DB_PATH=/mnt/registry.db \
    REGISTRY_TABLE_NAME=monocker_registry \
    PYTHONPATH=/:$PYTHONPATH

# open flask app port
EXPOSE 5000

# start flask app
CMD ["python", "-m", "monocker_registry.app"]
#==============================================================================