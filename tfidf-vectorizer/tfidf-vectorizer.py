import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here

    N = len(documents)

    term_frequencies = []
    document_frequencies = Counter()

    for doc in documents:
        words = doc.lower().split()
        tf = Counter(words)
        term_frequencies.append(tf)

        document_frequencies.update(set(words))

    vocabulary = sorted(document_frequencies.keys())
    vocab_index = {word: i for i, word in enumerate(vocabulary)}

    idf = {}
    for word in vocabulary:
        df = document_frequencies[word]
        idf[word] = math.log(N / df) if df > 0 else 0.0

    tfidf_matrix = np.zeros((N, len(vocabulary)))
    
    for doc_idx, tf in enumerate(term_frequencies):
        for word, count in tf.items():
            if word in vocab_index:
                col_idx = vocab_index[word]
                doc_length = sum(tf.values())  # total words in document
                tfidf_matrix[doc_idx, col_idx] = (count / doc_length) * idf[word]

    return tfidf_matrix, vocabulary

    
        