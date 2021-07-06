# Stackoverflow Top Questions & Answers ― Crawler
A script get the highest voted questions from StackOverflow.com and print its best anwser url.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Requirement](#requirement)
* [Setup](#setup)
* [Demo](#demo)

## General info
This tool is a part of project I learnt about crawler.

## Technologies
Project is created with:
* Python version: 3.8.10
* Stack Exchange API version: 2.3

[Learn more](https://api.stackexchange.com/docs/) about latest API version.

## Requirement
* `stackoverflow API key` store in config file (i.e. `myconfig.cfg`) located in the same directory of this script.

As document said, an API key is NOT compulsory to retrieve question/answer, but for more API quota in this case.
> If an application does have an access_token, then the application is on a distinct user/app pair daily quota (default [size of 10,000](https://api.stackexchange.com/docs/throttle)).

[Register an API key](https://stackapps.com/apps/oauth/register).

## Setup
To run this project, spin up terminal locally:
``` bash
$ cd ../stackoverflow-top-qa
$ python3 stackoverflow.py [N] [LABEL]
```

## Demo
```
$ python3 stackoverflow.py 4 python
```
1. What does the &quot;yield&quot; keyword do?

   [https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do#231855](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do#231855)

2. What does if __name__ == &quot;__main__&quot;: do?

   [https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185](https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185)

3. Does Python have a ternary conditional operator?

   [https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator#394814](https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator#394814)

4. What are metaclasses in Python?

   [https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python#6581949](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python#6581949)
