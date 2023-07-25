# https://huggingface.co/ClueAI/PromptCLUE-base
# 加载模型
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("ClueAI/PromptCLUE-base")
model = T5ForConditionalGeneration.from_pretrained("ClueAI/PromptCLUE-base")

import torch
device = torch.device('cpu')
#device = torch.device('cuda')
model.to(device)
def preprocess(text):
  return text.replace("\n", "_")

def postprocess(text):
  return text.replace("_", "\n")

def answer(text, sample=False, top_p=0.8):
  '''sample：是否抽样。生成任务，可以设置为True;
  top_p：0-1之间，生成的内容越多样'''
  text = preprocess(text)
  encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=768, return_tensors="pt").to(device) 
  if not sample:
    out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128, num_beams=4, length_penalty=0.6)
  else:
    out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=64, do_sample=True, top_p=top_p)
  out_text = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
  return postprocess(out_text[0])

text = """
    信息抽取：\
    据新华社电广东省清远市清城区政府昨日对外发布信息称,日前被实名举报涉嫌勒索企业、说“分分钟可以搞垮一间厂”的清城区环保局局长陈柏,已被免去清城区区委委员\
    问题：机构名，人名，职位\
    答案："""
print(answer(text, sample=False))