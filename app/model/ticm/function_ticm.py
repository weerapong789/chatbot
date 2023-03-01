import pythainlp
import pandas as pd
from pythainlp import sent_tokenize, word_tokenize
import glob

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
        if word in content:
            return 1
        else:
            return 0

def search_similar_txt(text_file,text) :
    search_result = []
    words = word_tokenize(text, keep_whitespace=True)
    pair = [''.join([x,y]) for x,y in zip(words[:-1], words[1:])]
    tree = [''.join([x,y,z]) for x,y,z in zip(words[:-2], words[1:-1], words[2:])]
    words = words + pair + tree
    for word in words :
        search_result.append(search_str(f'{text_file}', word))
    confidence = sum(search_result)/len(words)
    # print(words)
    # print(search_result)
    # print(text_file,'confident :',confidence)
    return text_file, confidence

result_select_text_files = []
result_select_text_confidence = []


questions = 'เพราะเหตุใดความเสี่ยงจากการลงทุนผ่านกองทุนรวมอาจต่ำกว่าการลงทุนตรงด้วยตนเอง'

select_text_files = []
cut_words= ['อย่างไร','ใคร','หมายถึงอะไร']
question = question.replace('คืออะไร','คือ')
for cut_word in cut_words :
    question = question.replace(cut_word,' ')
    text_paths = glob.glob('model/context/*.txt')
    
  confidences = []
  for text_path in text_paths :
    # question = 'NP คืออะไร'
    text_file,confidence = search_similar_txt(text_path,question)
    confidences.append(confidence)

  max_confidence = max(confidences)
  for index,confidence in enumerate(confidences):
    if confidence == max_confidence:
      select_text_files.append(text_paths[index].split('/')[-1])

  print(f'question : {question}')
  print(f'number_of_files : {len(select_text_files)} , confidence : {max_confidence}, select_text_files : {select_text_files} ')
  result_select_text_files.append(select_text_files)
  result_select_text_confidence.append(max_confidence)


