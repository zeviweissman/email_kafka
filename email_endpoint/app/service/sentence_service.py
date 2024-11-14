from typing import Counter

import psql.repository.sentences_repository as sentence_repos
from toolz import pipe, partial, first


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