# Stackoverflow Top Questions & Answers ― Crawler
A script get the highest voted questions from StackOverflow.com and print its best anwser url.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Requirement](#requirement)
* [Setup](#setup)

## General info
This tool is a part of project I learnt about crawler.

## Technologies
Project is created with:
* Python version: 3.8.10
* Stack Exchange API version: 2.3

(Latest version at: https://api.stackexchange.com/docs/)

## Requirement
* `stackoverflow API key` store in config file (i.e. `myconfig.cfg`) located in the same directory of this script.

(To register an API key: https://stackapps.com/apps/oauth/register)

## Setup
To run this project, spin up terminal locally:
```
$ cd ../stackoverflow-top-qa
$ python3 stackoverflow.py [N] [LABEL]
```
