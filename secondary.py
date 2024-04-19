from tqdm import tqdm
import json
import numpy as np 
datapath = "../data/NELL"

data = json.load(open(datapath + '/data.json', 'r'))

for rel in tqdm(task_pool):
  for e1 in data[rel].keys():
    data[rel][e1] = sorted(data[rel][e1].items(), key=lambda x: x[1], reverse=True)
    # data[rel][e1] = dict(sorted_items)

json.dump(data, open(datapath + '/data2.json', 'w'))