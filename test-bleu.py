import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import sentence_bleu

hyp = "save/trs/hyp.txt"
ref = "save/trs/ref.txt"

h = []
with open(hyp, 'r', encoding='utf-8') as hfile:
    for line in hfile:
        line = line.strip()
        token = sent_tokenize(line)
        h.append(token)

r = []
with open(ref, 'r', encoding='utf-8') as rfile:
    for line in rfile:
        line = line.strip()
        token = sent_tokenize(line)
        r.append(token)

score = 0
for i in range(len(h)):
    score += sentence_bleu(r, h)

print(score / len(h))