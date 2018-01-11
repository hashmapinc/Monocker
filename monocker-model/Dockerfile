FROM ubuntu:16.04

MAINTAINER Randy Pitcher <randy.pitcher@hashmapinc.com>

# expose tf serving port
EXPOSE 9000

# install libs
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libfreetype6-dev \
    libpng12-dev \
    libzmq3-dev \
    mlocate \
    pkg-config \
    python-dev \
    python-numpy \
    python-pip \
    software-properties-common \
    swig \
    zip \
    zlib1g-dev \
    libcurl3-dev \
    openjdk-8-jdk\
    openjdk-8-jre-headless \
    wget \
    && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install python libs
RUN pip install mock grpcio tensorflow-serving-api requests

# Install tf serving server
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" \
  | tee /etc/apt/sources.list.d/tensorflow-serving.list &&\
  curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - &&\
  apt-get update  &&\
  apt-get install tensorflow-model-server

# get default model
RUN curl https://raw.githubusercontent.com/tensorflow/serving/master/tensorflow_serving/example/mnist_saved_model.py > mnist_saved_model.py && \
  curl https://raw.githubusercontent.com/tensorflow/serving/master/tensorflow_serving/example/mnist_input_data.py > mnist_input_data.py

# train and export model
RUN python mnist_saved_model.py /tmp/mnist_model 

# upload the entrypoint
COPY monocker-model/ /monocker-model

# run tf serving and start model registrant service
CMD ["sh", "/monocker-model/entrypoint.sh"]