#!/bin/bash

echo "Building image and tagging with name: jupyter/minimal-notebook/pdfscrape:ubuntu-22.04 "
docker build -t jupyter/minimal-notebook/pdfscrape:ubuntu-22.04 .