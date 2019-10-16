from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dltools",
    author='aqreed',
    description='Useful tools/scripts/gists for deep learning applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.0.1",
    url='https://github.com/aqreed/dl-python-tools',
    packages=['dltools'],
    install_requires=['numpy'],
    tests_requires=['pytest'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ]
    )
