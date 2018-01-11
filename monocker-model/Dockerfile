FROM openjdk:8

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# install pip, python libs, and curl / run mnist files
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
  && curl https://raw.githubusercontent.com/tensorflow/serving/master/tensorflow_serving/example/mnist_saved_model.py > mnist_saved_model.py \
  && curl https://raw.githubusercontent.com/tensorflow/serving/master/tensorflow_serving/example/mnist_input_data.py > mnist_input_data.py \
  && python mnist_saved_model.py /tmp/mnist_model

# Install tf serving server
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" \
  | tee /etc/apt/sources.list.d/tensorflow-serving.list &&\
  curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - &&\
  apt-get update  &&\
  apt-get install tensorflow-model-server

# upload the entrypoint
COPY monocker-model/ /monocker-model

# configure environment variables
ENV REGISTRATION_FREQUENCY=60

# expose tf serving port
EXPOSE 9000

# run tf serving and start model registrant service
CMD ["sh", "/monocker-model/entrypoint.sh"]