from functools import reduce
from typing import List


def sentences_contain_word(sentences_list: List[str], word: str) -> bool:
    return any([word in string for string in sentences_list])

def email_contains_hostage(sentences_list: List[str]) -> bool:
    return sentences_contain_word(sentences_list, "hostage")


def email_contains_explosive(sentences_list: List[str]) -> bool:
    return sentences_contain_word(sentences_list, "explosi")


def move_sentence_by_word(sentences_list: List[str], word: str) -> List[str]:
    return reduce(lambda start, next: [next] + start if word in next else start + [next] ,sentences_list, [])

def move_hostage_sentences_to_the_top(sentences_list: List[str]) -> List[str]:
    return move_sentence_by_word(sentences_list, "hostage")


def move_explosive_sentences_to_the_top(sentences_list: List[str]) -> List[str]:
    return move_sentence_by_word(sentences_list, "explosi")