from utils.data_loader import prepare_data_seq
from utils import config
from model.seq2seq import SeqToSeq
if config.v2:
    from model.SVT import CvaeTrans
else:
    from model.GVT import CvaeTrans
from model.common_layer import evaluate,evaluate_tra, count_parameters, make_infinite, get_kld
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.init import xavier_uniform_
from copy import deepcopy
from tqdm import tqdm
import os
import time 
import numpy as np
import math
from tensorboardX import SummaryWriter
import logging

# data_loader_tra, data_loader_val, data_loader_tst, vocab, program_number = prepare_data_seq(batch_size=config.batch_size)
data_loader_tra, data_loader_val, data_loader_tst, vocab = prepare_data_seq(batch_size=config.batch_size) # data_loader with batch
logging.info("dataloader size - tra: {} dev: {} tst: {}".format(data_loader_tra.__len__(), data_loader_val.__len__(), data_loader_tst.__len__()))
