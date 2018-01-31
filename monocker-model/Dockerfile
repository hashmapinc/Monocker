FROM openjdk:8

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# install dependencies 
RUN apt-get update \
  && apt-get install -y \
    python-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install \
    grpcio \
    mock \
    requests \
    tensorflow-serving-api \
  && echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" \
  | tee /etc/apt/sources.list.d/tensorflow-serving.list \
  && curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - \
  && apt-get update  \
  && apt-get install tensorflow-model-server

# upload the entrypoint
COPY monocker-model/ /monocker-model

# configure environment variables
ENV TF_SERVING_PORT=9000 \
    REGISTRATION_FREQUENCY=60 \
    REGISTRY_HOSTNAME=monocker-registry-service \
    REGISTRY_PORT=80 \
    REGISTRY_ROUTE=models

# expose tf serving port
EXPOSE $TF_SERVING_PORT

# run tf serving and start model registrant service
CMD ["sh", "/monocker-model/entrypoint.sh"]