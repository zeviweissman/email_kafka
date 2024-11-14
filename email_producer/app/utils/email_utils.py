from typing import List

def email_contains_hostage(sentences_list: List[str]):
    return "hostage" in "".join(sentences_list)

def email_contains_explosive(sentences_list: List[str]):
    return "explosi" in "".join(sentences_list)
