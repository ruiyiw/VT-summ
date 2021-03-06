from fast_bleu import BLEU, SelfBLEU

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# hyp = "save/gvt-128-pre/pre-trs-1000/hyp_e576.txt"
# ref = "save/gvt-128-pre/pre-trs-1000/ref_e576.txt"
# hyp = "save/trs-128/hyp_e.txt"
# ref = "save/trs-128/ref_e.txt"
# hyp = "tmp/gvt-64-pre/cvae_trs_e299/hyp_e1000.txt"
# ref = "tmp/gvt-64-pre/cvae_trs_e299/ref_e1000.txt"
# hyp = "save/gvt-128-nopre/hyp.txt"
# ref = "save/gvt-128-nopre/ref.txt"
hyp = "save/cvae_t2/hyp.txt"
ref = "save/cvae_t2/ref.txt"

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

weights = {'bigram': (1/2., 1/2.), 'trigram': (1/3., 1/3., 1/3.), '4gram': (1/4., 1/4., 1/4., 1/4), '5gram': (1/5., 1/5., 1/5., 1/5., 1/5)}

bleu = BLEU(r, weights)
score_b = bleu.get_score(h)

self_bleu = SelfBLEU(h, weights)
score_s = self_bleu.get_score()

print("D-2: {} D-3: {} D-4: {} D-5: {}".format(sum(score_b['bigram'])/len(h), sum(score_b['trigram'])/len(h), sum(score_b['4gram'])/len(h), sum(score_b['5gram'])/len(h),))
print("S-2: {} S-3: {} D-4: {} D-5: {}".format(sum(score_s['bigram'])/len(h), sum(score_s['trigram'])/len(h), sum(score_b['4gram'])/len(h), sum(score_b['5gram'])/len(h),))