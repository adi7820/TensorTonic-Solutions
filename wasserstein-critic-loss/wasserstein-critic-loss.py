import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    real_scores = np.array(real_scores)
    fake_scores = np.array(fake_scores)

    real_score_mean = np.mean(real_scores)
    fake_score_mean = np.mean(fake_scores)

    loss = fake_score_mean - real_score_mean

    return float(loss)