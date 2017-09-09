import math
from collections import Counter

def entropy(class_probabilities):
    return sum( -p * math.log(p,2)
                for p in class_probabilities
                if p)
def class_probabilities(labels):
    total_count = len(labels)
    return [ count / total_count
             for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _,label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    total_count = sum(len(subsets) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)

inputs = [
({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'},
False),
({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'},
False),
({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'},
True),
({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'},
True),
({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'},
True),
({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'},
False),
({'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes'},
True),
({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, False),
({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'},
True),
({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}, True),
({'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes'}, True),
({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'},
True),
({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'},
True),
({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
]

