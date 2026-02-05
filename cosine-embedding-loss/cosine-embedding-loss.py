def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    dot_prod = sum(a*b for a,b in zip(x1, x2))
    norm_a = math.sqrt(sum(a*a for a in x1))
    norm_b = math.sqrt(sum(b*b for b in x2))

    cosine = dot_prod/(norm_a*norm_b)

    if label == 1:
        loss = 1 - cosine
    else:
        loss = max(0, cosine-margin)

    return loss
    