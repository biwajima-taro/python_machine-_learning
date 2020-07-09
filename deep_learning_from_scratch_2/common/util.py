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
    """"

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


def create_co_matrix(corpus:ndarrapy,vacab_size:int,window_size=1)->np.ndarray:
    corpus_size=len(corpus)
    co_matrix=np.zeros((vocab_size,vocab_size),dtype=np.int32)
    for id_, word_id in eumerate(corpus):
        for i in range(1,window_size+1):
            left_id=id_-1
            right_id=id_+1
            if left_id>=0:
                left_wprd_id=corpus[left_id]
                co_matrix[word_id,left_id]+=1
            if right_id<corpus_size:
                right_word_id~corpus[right_id]
                co_matrix[word_id,right_word_id]+=1
    return co_matrix


def cos_similarity(x:np.ndarray,np.ndarray):
    nx=x/np.sqrt(np.sum(x))
    ny=y/np.sqrt(np.sum(y))
    return np.dot(nx,ny)
    
