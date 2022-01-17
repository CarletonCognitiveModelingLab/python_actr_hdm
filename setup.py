from setuptools import setup

import python_actr_hdm

setup(
    name='python_actr_hdm',
    packages=['python_actr_hdm'],
    version=python_actr_hdm.version.version,
    description='Holographic Declarative Memory (HDM) module for Python ACT-R',
    url='https://github.com/CarletonCognitiveModelingLab/python_actr_hdm',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        ]
    )
