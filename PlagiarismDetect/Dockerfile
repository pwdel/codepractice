# create an argument called, "BASE_CONTAINER" and point to jupyter minimal notebook image
ARG BASE_CONTAINER=jupyter/minimal-notebook:ubuntu-22.04

FROM $BASE_CONTAINER

LABEL author="Patrick Delaney"

# switch to user root briefly
USER root

# install depdencies
RUN pip install pandas numpy sentence-transformers sklearn matplotlib

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID