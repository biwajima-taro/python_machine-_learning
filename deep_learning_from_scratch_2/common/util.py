from typing import List, Dict, Tuple
import numpy as np


def preprocess(text: str) -> Tuple[np.ndarray, Dict, Dict]:
    
    """
    
    [summary]

    Args:
        text (str): [description]

    Returns:
        Tuple[np.ndarray,Dict,Dict]: [description]
    """
    a=""""

    text = text.lower()
    text = text.replace(".", " .")
    words = text.split(" ")
    word_to_id = {}
    id_to_word = {}
    count = 0
    for word in words:
        if word_to_id.get(word) is None:
            word_to_id[word] = count
            id_to_word[count] = word
            count += 1
    corpus = np.array([word_to_id[word] for word in words])

    return corpus, word_to_id, id_to_word


def create_co_matrix(corpus:ndarrapy)