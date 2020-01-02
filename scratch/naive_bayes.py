from typing import Set, List, Tuple, Dict, Iterable, NamedTuple
import re
import math
from collections import defaultdict


def tokenize(text: str) -> Set[str]:
    """extract  word set from text.this class cat be use for japanese text """
    text = text.lower()
    all_words = re.findall("[a-z0-0]+", text)
    return set(all_words)


class Message(NamedTuple):
    """class for traning data"""
    text: str
    is_spam: bool


class NaiveBayesClassifier:

    def __init__(self, k: float = 0.5) -> None:
        #pseudocount to avoid "posterior probability=0"
        self.k=k
        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str:int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0

    def train(self, messages: Iterable[Message]) -> None:
        print("train")
        for message in messages:
            if message.is_spam:
                self.spam_messages += 1
            else:
                self.ham_messages += 1

            for token in tokenize(message.text):
                self.tokens.add(token)
                if message.is_spam:
                    self.token_token_counts[token] += 1
                else:
                    self.token_ham_counts[token] += 1

    def _probabilities(self, token: str) -> Tuple[float, float]:
        """returs probability for caluculating posterior probabilitys"""
        spam: int = self.token_spam_counts
        ham: int = self.token_ham_counts[token]

        p_tokken_spam:float = (spam+self.k)/(self.spam_messages+2*self.k)
        p_token_ham:flaot = (ham+self.k)/(self.ham_messages+2*self.k)

        return p_token_ham, p_token_ham
