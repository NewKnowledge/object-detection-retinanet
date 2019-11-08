#!/bin/bash

# Install packages
pip3 install -e git+https://gitlab.com/datadrivendiscovery/common-primitives@dataset_sample#egg=common_primitives
pip3 install -e /object-detection/

# Copy pipeline file, JSON, metadata, and ResNet50 weight to home
cp /object-detection/object_detection/object_detection_pipeline.py ~
cp /object-detection/787bb5eb-7ba0-4f34-8af3-0b277337e4b4.* ~
cd ~
wget https://github.com/fizyr/keras-models/releases/download/v0.0.1/ResNet-50-model.keras.h5

echo 'object-detection debugging setup complete.'