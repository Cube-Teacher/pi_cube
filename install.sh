#!/bin/bash

# install pupil_apriltags
pip3 install pupil_apriltags

# install processing
curl https://processing.org/download/install-arm.sh | sudo sh

# copy peasyCam to library
cp ./lib/peasycam /home/pi/sketchbook/libraries
