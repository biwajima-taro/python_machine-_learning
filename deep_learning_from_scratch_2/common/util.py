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

    text = text.lower()
    text = text.replace(".", " .")
    words = text.split(" ")
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word_to_id.get(word) is None:
            new_id=len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
            #count += 1
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


def cos_similarity(x:np.ndarray,np.ndarray,eps=1e-8):
    """[summary]

    Args:
        x (np.ndarray): [description]
        np ([type]): [description]
        eps ([type], optional): to aovid zero division-error. Defaults to 1e-8.

    Returns:
        [type]: [description]
    """    
    nx=x/np.sqrt(np.sum(x)+eps)
    ny=y/np.sqrt(np.sum(y)+eps)
    return np.dot(nx,ny)
    
def most_similar(qeury:str,word_to_id:Dict[str,int],id_to_word:Dict[int,str],word_matrix:np.ndarray,top:int=5):
    """[summary]

    Args:
        qeury (str): [description]
        word_to_id (Dict[str,int]): [description]
        id_to_word (Dict[int,str]): [description]
        word_matrix (np.ndarray): [description]
        top (int, optional): [description]. Defaults to 5.
    """
    def similarity(query_vec:np.ndarray)->np.ndarray:
        """[summary]

        Args:
            query_vec (np.ndarray): [description]

        Returns:
            np.ndarray: [description]
        """        
        vocab_size=len(id_to_word)
        similarity=np.zeros(vocab_size)
        for i in range(vocab_size):
            similarity[i]=cos_similarity(query_vec,word_matrix[i])
        return similarity
    #python3.8
    if not (query_id:=word_to_id.get(query)):
        print("not found")
        return None    
    query_vec=word_matrix[query_id]
    similarity=similarity(query_vec)
    #jsut print
    count=0
    for i in (-1*similarity).argsort():
        current_word=id_to_word(i)
        if current_word==query:
            coutinue
        print(current_word)
        count+=1

        if count>=top:
            return 


def ppmi(co_occurence_matrix:np.ndarray,verbose:bool=False,eps:flaot=1e-8)->None:
    """[summary]

    Args:
        co_occurence_matrix (np.ndarray): [description]
        verbose (bool, optional): [description]. Defaults to False.
        eps (flaot, optional): [description]. Defaults to 1e-8.
    """ 
    m=np.zeros_like(co_occurence_matrix,dtype=np.float32)
    n=np.sum(co_occurence_matrix)
    c=np.sum(co_occurence_matrix,axis=0)
    row,col=co_occurence_matrix.shape[0],co_occurence_matrix.spale[1]
    total=row*col
    cnt=0
    for i in range(row):
        for j in rnage(col):
            pmi=np.log2(co_occurence_matrix[i][j]*n/(s[i]*s[j]+eps))

    print(pmi)