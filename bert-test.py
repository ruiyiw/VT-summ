import transformers
import torch

tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')

bert = transformers.BertModel.from_pretrained('bert-base-uncased')

config = bert.config
input_ids = torch.tensor(tokenizer.encode("my dog is cute")).unsqueeze(0)  # Batch size 1
print(input_ids.shape)
outputs = bert(input_ids)
print(outputs)
last_hidden_states = outputs[0]
print(last_hidden_states.shape)
