import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    N = len(docs)

    doc_lens = np.array([len(doc) for doc in docs])

    avgdl = np.mean(doc_lens)

    df = Counter()

    for doc in docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] += 1

    scores = np.zeros(N)

    for i, doc in enumerate(docs):
        score = 0.0
        doc_counter = Counter(doc)

        for term in query_tokens:
            if term not in df:
                continue 
            tf = doc_counter[term]
            if tf == 0:
                continue 

            idf = math.log(1 + (N - df[term] + 0.5)/(df[term] + 0.5))

            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * (doc_lens[i]/avgdl))

            score += idf * (numerator/denominator)

        scores[i] = score

    return scores