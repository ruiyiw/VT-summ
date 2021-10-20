import transformers
import torch

tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')

bert = transformers.BertModel.from_pretrained('bert-base-uncased')

config = bert.config
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
outputs = bert(input_ids)
last_hidden_states = outputs[0]
print(last_hidden_states.shape)
