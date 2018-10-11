#!/bin/bash

sudo su 

apt-get update

sudo add-apt-repository ppa:webupd8team/java

sudo apt-get update 

sudo apt-get install -y oracle-java8-installer

apt-get install -y python2-pip

pip install pyspark

