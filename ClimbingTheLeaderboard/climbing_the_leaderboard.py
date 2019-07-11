from bisect import bisect

def climbingLeaderboard(scores, alice):
    # convert scores to dict - scores: rank
    rankings = generate_rankings(scores)
    
    scores.reverse()
    alices_rankings = []
    for alices_score in alice:
        alices_rankings.append(get_alices_ranking(scores, alices_score, rankings))
    
    return alices_rankings
    
def generate_rankings(scores):
    rank = 1
    rankings = {}
    for score in scores:
        if score in rankings:
            continue
        rankings[score] = rank
        rank += 1
    return rankings

def get_alices_ranking(scores_in_ascending_order, alices_score, rankings):
    if alices_score in rankings:
        return rankings[alices_score]

    index = bisect(scores_in_ascending_order, alices_score) - 1
    if index == -1:
        return len(rankings) + 1
    
    return rankings[scores_in_ascending_order[index]]
