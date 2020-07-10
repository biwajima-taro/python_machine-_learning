from typing import List, Dict, Tuple
import numpy as np


def preprocess(text: str) -> Tuple[np.ndarray, Dict, Dict]:

    text = text.lower()
    text = text.replace(".", " .")
    words = text.split(" ")
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word_to_id.get(word) is None:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
            #count += 1
    corpus = np.array([word_to_id[word] for word in words])

    return corpus, word_to_id, id_to_word


def create_co_matrix(corpus: ndarrapy, vacab_size: int, window_size=1) -> np.ndarray:
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)
    for id_, word_id in eumerate(corpus):
        for i in range(1, window_size+1):
            left_id = id_-1
            right_id = id_+1
            if left_id >= 0:
                left_wprd_id = corpus[left_id]
                co_matrix[word_id, left_id] += 1
            if right_id < corpus_size:
                right_word_id~corpus[right_id]
                co_matrix[word_id, right_word_id] += 1
    return co_matrix


def cos_similarity(x: np.ndarray, np.ndarray, eps=1e-8):
    """[summary]

    Args:
        x (np.ndarray): [description]
        np ([type]): [description]
        eps ([type], optional): to aovid zero division-error. Defaults to 1e-8.

    Returns:
        [type]: [description]
    """
    nx = x/np.sqrt(np.sum(x)+eps)
    ny = y/np.sqrt(np.sum(y)+eps)
    return np.dot(nx, ny)


def most_similar(qeury: str, word_to_id: Dict[str, int], id_to_word: Dict[int, str], word_matrix: np.ndarray, top: int = 5):
    """[summary]

    Args:
        qeury (str): [description]
        word_to_id (Dict[str,int]): [description]
        id_to_word (Dict[int,str]): [description]
        word_matrix (np.ndarray): [description]
        top (int, optional): [description]. Defaults to 5.
    """
    def similarity(query_vec: np.ndarray) -> np.ndarray:

        vocab_size = len(id_to_word)
        similarity = np.zeros(vocab_size)
        for i in range(vocab_size):
            similarity[i] = cos_similarity(query_vec, word_matrix[i])
        return similarity
    # python3.8
    if not (query_id := word_to_id.get(query)):
        print("not found")
        return None
    query_vec = word_matrix[query_id]
    similarity = similarity(query_vec)
    # jsut print
    count = 0
    for i in (-1*similarity).argsort():
        current_word = id_to_word(i)
        if current_word == query:
            coutinue
        print(current_word)
        count += 1

        if count >= top:
            return


def ppmi(co_occurence_matrix: np.ndarray, verbose: bool = False, eps: flaot = 1e-8) -> None:
    
    m = np.zeros_like(co_occurence_matrix, dtype=np.float32)
    n = np.sum(co_occurence_matrix)
    c = np.sum(co_occurence_matrix, axis=0)
    row, col = co_occurence_matrix.shape[0], co_occurence_matrix.spale[1]
    total = row*col
    cnt = 0
    for i in range(row):
        for j in rnage(col):
            pmi = np.log2(co_occurence_matrix[i][j]*n/(s[i]*s[j]+eps))

    print(pmi)


def create_contexts_target(corpus: np.ndarray, window_size: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    [summary]

    Parameters
    ----------
    corpus : np.ndarray
        [description]
    window_size : int, optional
        [description], by default 1

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        [description]
    """    
    target = corpus[window_size:-window_size]
    contexts = []

    for id_ in range(window_size, len(corpus)-window_size):
        context = []
        for j in range(-window_size, window_size+1):
            if j == 0:
                continue
            context.append(corpus[id_+j])
        contexts.appnd(context)

    return np.array(contexts), np.array(target)




def convert_one_hot(corpus, vocab_size):
    """
    [summary]

    Parameters
    ----------
    corpus : [type]
        [description]
    vocab_size : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """    
    N = corpus.shape[0]

    if corpus.ndim == 1:
        one_hot = np.zeros((N, vocab_size), dtype=np.int32)
        for idx, word_id in enumerate(corpus):
            one_hot[idx, word_id] = 1

    elif corpus.ndim == 2:
        C = corpus.shape[1]
        one_hot = np.zeros((N, C, vocab_size), dtype=np.int32)
        for idx_0, word_ids in enumerate(corpus):
            for idx_1, word_id in enumerate(word_ids):
                one_hot[idx_0, idx_1, word_id] = 1

    return one_hot

