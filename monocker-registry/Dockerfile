#==============================================================================
# Dockerfile for monocker-registry project
#
# Flask api with sqlite3 db (provided through a k8's PV)
#==============================================================================
FROM python:3

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# add flask app
COPY monocker-registry/ /monocker-registry

#install python libs
WORKDIR /monocker-registry
RUN pip install -r requirements.txt

#add envs
ENV REGISTRATION_FREQUENCY=60 \
    REGISTRY_DB_PATH=/mnt/registry.db \
    REGISTRY_TABLE_NAME=monocker_registry

# open flask app port
EXPOSE 5000

# start node app
CMD ["/bin/bash"]
#==============================================================================