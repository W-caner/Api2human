# # import nltk
# # from nltk.tokenize import sent_tokenize
# # import numpy as np
# # import random
# # import json
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model = AutoModelForSeq2SeqLM.from_pretrained('/wangcan/T5/model-t5-base/checkpoint-74500/')
# tokenizer = AutoTokenizer.from_pretrained('/wangcan/T5/model-t5-base/checkpoint-74500/')

# temperature = 0.9
# num_beams = 2
# max_gen_length = 512

# # with open('/wangcan/GPT/dataset/test.json') as f:
#     # datasets = f.readlines()
# # for data in datasets:
#     # data = json.loads(data)
#     # abstract, label = data['information'], data['label']

# # abstract = "desc:Deletes the specified local network gateway#name:resourceGroupName#type:string"
# inputs = tokenizer([abstract], max_length=512, return_tensors='pt')

# title_ids = model.generate(
#     inputs['input_ids'], 
#     num_beams=num_beams, 
#     temperature=temperature, 
#     max_length=max_gen_length, 
#     early_stopping=True
# )
# title = tokenizer.decode(title_ids[0].tolist(), skip_special_tokens=True, clean_up_tokenization_spaces=False)
# # print(title)