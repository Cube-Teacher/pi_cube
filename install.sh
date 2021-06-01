#!/bin/bash

# install pupil_apriltags
pip3 install pupil_apriltags

# install processing
curl https://processing.org/download/install-arm.sh | sudo sh

# run processing and it would be fail
/usr/local/bin/processing-java --sketch=/home/pi/pi_cube/main --run

# copy peasyCam to library
cp -r ./lib/peasycam /home/pi/sketchbook/libraries
