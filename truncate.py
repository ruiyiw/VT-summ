# # from utils.data_loader import prepare_data_seq
# # from utils import config
# # from model.seq2seq import SeqToSeq
# # if config.v2:
# #     from model.SVT import CvaeTrans
# # else:
# #     from model.GVT import CvaeTrans
# # from model.common_layer import evaluate,evaluate_tra, count_parameters, make_infinite, get_kld
# # import torch
# # import torch.nn as nn
# # import torch.nn.functional as F
# # from torch.nn.init import xavier_uniform_
# # from copy import deepcopy
# # from tqdm import tqdm
# # import os
# # import time 
# # import numpy as np
# # import math
# # from tensorboardX import SummaryWriter
# # import logging

# # # data_loader_tra, data_loader_val, data_loader_tst, vocab, program_number = prepare_data_seq(batch_size=config.batch_size)
# # data_loader_tra, data_loader_val, data_loader_tst, vocab = prepare_data_seq(batch_size=config.batch_size) # data_loader with batch
# # logging.info("dataloader size - tra: {} dev: {} tst: {}".format(data_loader_tra.__len__(), data_loader_val.__len__(), data_loader_tst.__len__()))
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
# import logging

# # sentence = "Hello world . Hello world ! Hello world ?"
# # token = sent_tokenize(sentence)
# # print(token)
# # text = token[0]+token[1]
# # print(text)
path = "data/cnn_dm_data/"

count = 0
empty = []
with open(path+"train.source", 'r', encoding='utf-8') as fin:
    for line in fin:
        # line = line.strip().split()
        line = line.strip()
        token = sent_tokenize(line)
        # if len(token) == 1:
        #     # text.append(token[0])
        # elif len(token) > 1:
        #     # text.append(token[0]+token[1])
        if len(token) == 0:
            empty.append(count)
        count += 1

# with open(path+"train.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')


count = 0
target = []
with open(path+"train.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        if count not in empty:
            line = line.strip()
            target.append(line)
    count += 1

with open(path+"train.target.pre", 'w', encoding='utf-8') as fout:
    for t in target:
        fout.write(t)
        fout.write('\n')


# with open(path+"train.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')

# logging.info("Train", count)

# count = 0
# text = []
# with open(path+"val.source", 'r', encoding='utf-8') as fin:
#     for line in fin:
#         # line = line.strip().split()
#         line = line.strip()
#         token = sent_tokenize(line)
#         if len(token) == 1:
#             text.append(token[0])
#             count += 1
#         elif len(token) > 1:
#             text.append(token[0]+token[1])
#             count += 1

# with open(path+"val.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')

# logging.info("Val", count)

# count = 0
# text = []
# with open(path+"test.source", 'r', encoding='utf-8') as fin:
#     for line in fin:
#         # line = line.strip().split()
#         line = line.strip()
#         token = sent_tokenize(line)
#         if len(token) == 1:
#             text.append(token[0])
#             count += 1
#         elif len(token) > 1:
#             text.append(token[0]+token[1])
#             count += 1

# with open(path+"test.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')

# logging.info("Test", count)

path = "data/cnn_dm_data/"
count = 0
with open(path+"train.source.pre", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Train source", count)

count = 0
with open(path+"val.source.pre", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Val source", count)

count = 0
with open(path+"test.source.pre", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Test source", count)

count = 0
with open(path+"train.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Train target", count)

count = 0
with open(path+"val.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Val target", count)

count = 0
with open(path+"test.target", 'r', encoding='utf-8') as fin:
    for line in fin:
        count += 1
print("Test target", count)