# from utils.data_loader import prepare_data_seq
# from utils import config
# from model.seq2seq import SeqToSeq
# if config.v2:
#     from model.SVT import CvaeTrans
# else:
#     from model.GVT import CvaeTrans
# from model.common_layer import evaluate,evaluate_tra, count_parameters, make_infinite, get_kld
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch.nn.init import xavier_uniform_
# from copy import deepcopy
# from tqdm import tqdm
# import os
# import time 
# import numpy as np
# import math
# from tensorboardX import SummaryWriter
# import logging

# # data_loader_tra, data_loader_val, data_loader_tst, vocab, program_number = prepare_data_seq(batch_size=config.batch_size)
# data_loader_tra, data_loader_val, data_loader_tst, vocab = prepare_data_seq(batch_size=config.batch_size) # data_loader with batch
# logging.info("dataloader size - tra: {} dev: {} tst: {}".format(data_loader_tra.__len__(), data_loader_val.__len__(), data_loader_tst.__len__()))
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# sentence = "Hello world . Hello world ! Hello world ?"
# token = sent_tokenize(sentence)
# print(token)
# text = token[0]+token[1]
# print(text)
path = "data/cnn_dm_data/"
text = []
with open(path+"train.source", 'r', encoding='utf-8') as fin:
    for line in fin:
        # line = line.strip().split()
        line = line.strip()
        token = sent_tokenize(line)
        print(token)
        if len(token) == 1:
            text.append(token[0])
        else:
            text.append(token[0]+token[1])

with open(path+"train.source.pre", 'w', encoding='utf-8') as fout:
    for t in text:
        fout.write(t)
        fout.write('\n')


# text = []
# with open(path+"val.source", 'r', encoding='utf-8') as fin:
#     for line in fin:
#         # line = line.strip().split()
#         line = line.strip()
#         token = sent_tokenize(line)
#         if len(token) < 2:
#             text.append(token[0])
#         else:
#             text.append(token[0]+token[1])

# with open(path+"val.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')


# text = []
# with open(path+"test.source", 'r', encoding='utf-8') as fin:
#     for line in fin:
#         # line = line.strip().split()
#         line = line.strip()
#         token = sent_tokenize(line)
#         if len(token) < 2:
#             text.append(token[0])
#         else:
#             text.append(token[0]+token[1])

# with open(path+"test.source.pre", 'w', encoding='utf-8') as fout:
#     for t in text:
#         fout.write(t)
#         fout.write('\n')