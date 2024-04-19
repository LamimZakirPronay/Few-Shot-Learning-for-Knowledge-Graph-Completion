from tqdm import tqdm
import json
import numpy as np
import primary
datapath = "../data/NELL"




datapath = "../data/NELL"
train_tasks = json.load(open(datapath + '/train_tasks.json'))
rel2candidates = json.load(open(datapath + '/rel2candidates_all.json'))
ent_embed = np.loadtxt(datapath + '/embed/entity2vec.' + 'TransE')
# ent_embed2 = np.loadtxt(datapath + '/embed/entity2vec.' + 'ComplEx')
# ent_embed=(ent_embed1+ent_embed2)/2
rel2id = json.load(open(datapath + '/relation2ids'))
ent2id = json.load(open(datapath + '/ent2ids'))
e1rel_e2 = json.load(open(datapath + '/e1rel_e2.json'))

task_pool = list(train_tasks.keys())
num_tasks = len(task_pool)

data = json.load(open(datapath + '/data.json', 'r'))


for rel in tqdm(task_pool):
  for e1 in data[rel].keys():
    data[rel][e1] = sorted(data[rel][e1].items(), key=lambda x: x[1], reverse=True)
    # data[rel][e1] = dict(sorted_items)


json.dump(data, open(datapath + '/data2.json', 'w'))
