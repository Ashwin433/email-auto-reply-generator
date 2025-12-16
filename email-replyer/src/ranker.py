def score(text, slots_filled):
    """
    Higher score is better.
    Reward filled slots, slightly penalize long replies.
    """
    return (slots_filled * 2) - (len(text) * 0.01)


def rank_candidates(candidates, filled_counts):
    scored = []

    for text, s in zip(candidates, filled_counts):
        scored.append((text, score(text, s)))

    scored.sort(key=lambda x: x[1], reverse=True)

    return [text for text, _ in scored]
