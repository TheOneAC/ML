from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt


def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


def majority_vote(labels):
    #select the majority label
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners ==1:
        return winner
    else:
        return majority_vote(labels[:-1])

def distance(point, new_point):
    dis = sum([(x-y)**2
        for x, y in zip(point, new_point)
        ])
    return sqrt(dis)
def knn_classify(k, labeled_points, new_point):
    # ordeed by distance
    by_distance = sorted(labeled_points, key= lambda (point, _):distance(point, new_point))
    # k labels for k-min distance
    k_nearest_labels = [labele for _, labele in by_distance[:k]]
    return majority_vote(k_nearest_labels)


cities = [
    ([-122.3 , 47.53], "Python"),
    ([ -96.85, 32.85], "Java"),
    ([ -89.33, 43.13], "R"),
    ([-120.3 , 35.53], "Python"),
    ([ -46.85, 72.85], "Java"),
    ([ -39.33, 33.13], "R"),
    ([-234.3 , 87.53], "Python"),
    ([ -46.85, 72.85], "Java"),
    ([ -39.33, 53.13], "R"),
    ]


for k in [1, 3, 5, 7]:
    num_correct = 0
    for city in cities:
        location, actual_language = city
        other_cities = [other_city
            for other_city in cities
            if other_city != city]
        predicted_language = knn_classify(k, other_cities, location)
        if predicted_language == actual_language:
            num_correct += 1
    print k, "neighbor[s]:", num_correct, "correct out of", len(cities)