import setuptools
import numpy

from setuptools import setup, find_packages
from setuptools.extension import Extension
from distutils.command.build_ext import build_ext as DistUtilsBuildExt

setup(
    name              = 'object-detection-retinanet',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet',
    url               = 'https://github.com/NewKnowledge/object-detection-retinanet/',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    #packages          = ['object_detection_retinanet'],
    packages          = find_packages(),
    include_package_data = True,
    install_requires  = ['keras==2.3.0',
                         'keras-resnet==0.1.0',
                         'six',
                         'scipy>=1.2.1,<=1.3.1',
                         'cython==0.29.14',
                         'Pillow',
                         'progressbar2',
                         'opencv-python',
                         'numpy>=1.15.4,<=1.17.3'
                        ],
    ext_modules       = [
        Extension('object_detection_retinanet.utils.compute_overlap', ['object_detection_retinanet/utils/compute_overlap.pyx'],
        include_dirs = [numpy.get_include()])
    ]
)