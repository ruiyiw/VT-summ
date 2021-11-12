path = "data/cnn_dm_data/"
vocab = {}
punctuation = '",.;:!?' + "'"
with open(path+"train.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0

with open(path+"train.source", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0

with open(path+"val.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0

with open(path+"val.source", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0

with open(path+"test.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0

with open(path+"test.source", 'r', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip().split()
        for w in line:
            if len(w) > 1 and w[0] in punctuation:
                w = w[1:]
            if len(w) > 1 and w[len(w)-1] in punctuation:
                w = w[0:len(w)-2]
            if not vocab.__contains__(w):
                vocab[w] = 0


with open(path+"vocab.txt", 'w', encoding='utf-8') as fout:
    for k in vocab.keys():
        fout.write(k)
        fout.write('\n')
    
        



