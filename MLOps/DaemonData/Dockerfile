# syntax=docker/dockerfile:1
FROM debian:bullseye-slim

# install any system tools
RUN apt-get update                                              && \
    # install cron
    apt-get install -y --no-install-recommends                     \
        cron=3.0pl1-137                                            \
        python3-pip=20.3.4                                      && \
    apt-get clean

# copy files from local directory
COPY app /home/app

# move into the proper working directory
WORKDIR /home/app

# Python installation of requirements with pip
# install python requirements.txt via binary
RUN apt-get update                                              && \
    pip install -r requirements.txt

# pip3 install requests

# pip3 install pytz

# pip3 install pandas

# apt-get -y install cron


# add python weather grabbing script to bash to make it visible to all apps

# setup cron job


# execute cron job

# any executable shell scripts


# entrypoints