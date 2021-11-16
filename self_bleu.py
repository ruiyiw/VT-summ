from fast_bleu import BLEU, SelfBLEU

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

hyp = "save/trs-128/hyp.txt"
ref = "save/trs-128/ref.txt"

h = []
with open(hyp, 'r', encoding='utf-8') as hfile:
    for line in hfile:
        line = line.strip()
        # token = sent_tokenize(line)
        word = word_tokenize(line)
        # print(word)
        h.append(word)

r = []
with open(ref, 'r', encoding='utf-8') as rfile:
    for line in rfile:
        line = line.strip()
        # token = sent_tokenize(line)
        word = word_tokenize(line)
        r.append(word)

weights = {'unigram': (1), 'bigram': (1/2., 1/2.), 'trigram': (1/3., 1/3., 1/3.)}

bleu = BLEU(r, weights)
score_b = bleu.get_score(h)

self_bleu = SelfBLEU(h, weights)
score_s = self_bleu.get_score()

print("D-1: {} D-2: {} D-3: {}".format(sum(score_b['unigram'])/len(h), sum(score_b['bigram'])/len(h), sum(score_b['trigram'])/len(h)))
print("S-1: {} S-2: {} S-3: {}".format(sum(score_s['unigram'])/len(h), sum(score_s['bigram'])/len(h), sum(score_s['trigram'])/len(h)))