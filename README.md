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

[Learn more](https://api.stackexchange.com/docs/) about latest API version.

## Requirement
* `stackoverflow API key` store in config file (i.e. `myconfig.cfg`) located in the same directory of this script.

As document said, an API key is NOT compulsory to retrieve question/answer, but for more quota of API calls.
> If an application does have an access_token, then the application is on a distinct user/app pair daily quota (default [size of 10,000](https://api.stackexchange.com/docs/throttle)).

[Register an API key](https://stackapps.com/apps/oauth/register).

## Setup
To run this project, spin up terminal locally:
```
$ cd ../stackoverflow-top-qa
$ python3 stackoverflow.py [N] [LABEL]
```
