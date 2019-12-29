from collections import Counter
def mode(x:List([float])->List[float]:
    counts=Counter(x)
    max_count=max(count.values())
    #count.items() consists of list of tuple (key,value)
    return [for x_i,count in count.items()if count==max_count]