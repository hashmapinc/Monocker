#==============================================================================
# Dockerfile for monocker-registry project
#
# This dockerfile uses oscarfonts/h2 as a base, installs node/npm, then
# runs the monocker-registry flask service for discovery and tracking of 
# monocker-model services.
#==============================================================================
# https://hub.docker.com/r/oscarfonts/h2/builds/
FROM oscarfonts/h2:latest

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# install node, npm, and swagger
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash \
  && apt-get update \
  && apt-get install -y nodejs \
  && npm install -g swagger

# start h2 in the background
RUN java -cp /opt/h2/bin/h2*.jar org.h2.tools.Server \
  -web -webAllowOthers -webPort 81 \
  -tcp -tcpAllowOthers -tcpPort 1521 \
  -baseDir ${DATA_DIR} &

# add node app
COPY monocker-registry/ /monocker-registry

# set working dir to node app home
WORKDIR /monocker-registry

# open node app port
EXPOSE 10010

# start node app
CMD ["swagger", "project", "start"]
#==============================================================================