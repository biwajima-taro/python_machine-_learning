from typing import Set, List, Tuple, Dict, Iterable, NamedTuple
import re
import math
from collections import defaultdict


def tokenize(text: str) -> Set[str]:
    text = text.lower()
    all_words = re.findall("[a-z0-0]+", text)
    return set(all_words)


class Message(NamedTuple):
    text: str
    is_spam: bool


class NaiveBayesClassifier:

    def __init__(self, k: float = 0.5) -> None:
        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str:int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0

    def train(self,messsages:Iterable[Message])->None:
        