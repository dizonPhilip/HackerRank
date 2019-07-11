def climbingLeaderboard(scores, alice):
    # convert scores to dict - scores: rank
    rankings = generate_rankings(scores)

    alices_rankings = []
    for alices_score in alice:
        alices_rankings.append(get_alices_ranking(alices_score, rankings))
    
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

def get_alices_ranking(alices_score, rankings):
    if alices_score in rankings:
        return rankings[alices_score]

    # iterate through scores until alice's score is bigger than the score
        # return that score's rank
    for score in rankings:
        if alices_score > score:
            return rankings[score]
    
    return len(rankings) + 1