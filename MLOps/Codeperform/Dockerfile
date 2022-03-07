# syntax=docker/dockerfile:1
FROM ubuntu:20.04

# switch to bash shell in Docker runtime
RUN /bin/bash

RUN apt-get update                                              && \
    # install shell tools, bc, python
    apt-get install -y --no-install-recommends                     \
        bc=1.07.*                                                  \
        python3-minimal=3.8.2-0ubuntu2                             \
        python3-pip=20.0.*                                      && \
    apt-get clean                                               && \
    rm -rf /var/lib/apt/lists/*

# copy files from local directory
COPY app /home/app

# move into the proper working directory
WORKDIR /home/app

# install python requirements.txt via binary
RUN apt-get update                                              && \
    apt-get install -y                                             \
        build-essential                                            \
        make                                                       \
        gcc                                                     && \
    pip install -r requirements.txt                             && \
    apt-get remove -y --purge make gcc build-essential          && \
    apt-get autoremove -y                                       && \
    rm -rf /var/lib/apt/lists/*

# Create executable shell script for codeperform.sh
# Add to ~/bin, make executable
RUN mkdir ~/bin                                                 && \
    cp codeperform.sh ~/bin/codeperform                         && \
    chmod +x ~/bin/codeperform                                  && \
    echo "export PATH=\$PATH:~/bin" >> ~/.bashrc                && \
    . ~/.bashrc