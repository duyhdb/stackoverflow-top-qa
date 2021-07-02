#!/usr/bin/env python3

"""What this script does:
    - Get N most-voted questions from stackoverflow.com
with specific label.
    - Print the title of question & its best anwser url.

How to use:
    $ python3 stackoverflow.py [N] [LABEL]
    
Requirement:
    - A API token and store it in a config file (i.e. sample.cfg).
"""

import argparse
import configparser
import os

import requests


def parse_token() -> str:
    """Return API access token (from file)"""
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), "sample.cfg")
    config.read(config_file)

    return config['stackoverflow']['access_token']


def best_answer_url(session, question, token: str) -> str:
    answer_url = "https://api.stackexchange.com/2.2/questions/{}/answers"
    answer_params = {
        "pagesize": 1,
        "order": "desc",
        "sort": "votes",
        "site": "stackoverflow",
        "key": token,
    }

    q_id = question['question_id']
    q_title = question['link'].split("/")[-1]

    with session:
        ans = session.get(answer_url.format(q_id), params=answer_params).json()
    best_answer_id = ans['items'][0]["answer_id"]

    return ("https://stackoverflow.com/questions"
            f"/{q_id}/{q_title}#{best_answer_id}")


def questions(session, question_url: str, question_params: dict) -> dict:
    """Return all questions in a page"""
    with session:

        return session.get(question_url, params=question_params).json()


def top_questions(n: int, tag: str, token: str):
    """
    Yield top question-titles and its best answer-URL
    - Paging API if needed large number of questions.

    :param n: numbers of question.
    :param tag: label of question.
    :param acces_token: registered API key (for more quota per day).
        See more at: https://stackapps.com/apps/oauth/register
    :yield Tuple:
    """
    q_url = "https://api.stackexchange.com/2.2/questions"
    q_params = {
        "order": "desc",
        "sort": "votes",
        "tagged": tag,
        "site": "stackoverflow",
        "key": token,
        "page": 1,
    }

    sess = requests.Session()

    # No paging needed when less than 30 results.
    if 0 <= n <= 30:  # 30 is default `page_size`.
        q_params['pagesize'] = n

        # Retrieve best answer's URL and question titles.
        for question in questions(sess, q_url, q_params)['items']:
            yield question['title'], best_answer_url(sess, question, token)

    # Paging when needed more than 30 results.
    # https://api.stackexchange.com/docs/paging
    else:
        n_count = 0
        while True:
            questions_per_page = questions(sess, q_url, q_params)

            # Retrieve best answer's URL and question titles.
            for question in questions_per_page['items']:
                yield question['title'], best_answer_url(sess, question, token)

                # Stop yielding when got enough result.
                n_count = n_count + 1
                if n == n_count:
                    return

            # To next page.
            if questions_per_page['has_more']:
                q_params['page'] += 1
            else:
                break


def main() -> None:
    # Parse arguments.
    parser = argparse.ArgumentParser(
        description="Get the most voted questions & anwser on Stack Overflow."
    )
    parser.add_argument("n", type=int, help="Number of questions.")
    parser.add_argument("tag", type=str, help="Tag of questions.")
    args = parser.parse_args()

    # Parse API token (from file) for 10_000 quota per day instead of 300.
    # https://api.stackexchange.com/docs/throttle
    access_token = parse_token()

    # Show most voted questions & best answer's URLs.
    for index, (question, answer) in enumerate(
            top_questions(args.n, args.tag, access_token), start=1):
        print(f"\n{index}. {question}\n> {answer}\n")


if __name__ == "__main__":
    main()
