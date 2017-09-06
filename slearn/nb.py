import  re
from collections import defaultdict

def tokenize(message):
    message= message.lower()
    all_words = re.findall("[a-z0-9']+",message)
    return set(all_words)

def count_words(trainning_set):
    counts= defaultdict(lambda: [0,0])
    for message, is_spam in trainning_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] +=1
    return counts

def word_probabilities(counts, total_spams,total_no_spams, k=0.5):
    return[
        (w,(spam + k)/(total_spams + 2*k),
        (non_spam + k)/(total_no_spams + 2 * k))
        for w, (spam,non_spam) in counts.iteritems()]
def spam_probability (word_probs, message):
    message_words = tokenize(message)
    log_prob_of_spam = log_prob_of_nospam = 0.0
    for word, prob_of_spam, prob_of_nospam in word_probs:
        if word in message_words:
            log_prob_of_nospam += math.log(prob_of_nospam)
            log_prob_of_spam += math.log(prob_of_spam)
        else
            log_prob_of_nospam +=math.log(1 - prob_of_nospam)
            log_prob_of_spam += math.log(1 - prob_of_spam)
    prob_of_spam = math.exp(log_prob_of_spam)
    prob_of_nospam = math.exp(log_prob_of_nospam)
    return prob_of_spam/(prob_of_nospam + prob_of_spam)

class NaiveBayesClassifier:
    def __init__(self,k=0.5):
        self.k = k
        self.word_probs =[]
    def train(self, training_set):
        num_spams = len(is_spam for message, is_spam in training_set if is_spam)
        num_non_spams = len(training_set) - num_spams
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts,num_spams,num_non_spams,self.k)
    def classify(self, message):
        return spam_probability(self.word_probs, message)
)
