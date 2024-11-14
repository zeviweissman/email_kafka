from typing import Counter
import psql.repository.email_repository as email_repos
import psql.repository.sentences_repository as sentence_repos
from toolz import pipe, partial, first
import email_endpoint.app.utils.convert_utils as utils


def most_common_word():
    return pipe(
        sentence_repos.get_all_sentences(),
        partial(map, lambda sentence: sentence.sentence),
        "".join,
        str.split,
        Counter,
        Counter.most_common,
        first
    )

def get_most_common_word():
    word, count = most_common_word()
    return {
        'word':word, 'count':count
    }


def get_sentences_by_email_address(email_address):
    emails = email_repos.get_emails_by_email_address(email_address)
    return ". ".join([utils.email_model_to_sentences_joined(email) for email in emails])