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

# install node and npm
RUN apt-get update && apt-get install -y \
      nodejs \
      npm

# cp node application 
