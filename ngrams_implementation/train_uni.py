import json
from nltk.tokenize import word_tokenize

def read_file(path):
    file = open(path, "r", encoding="utf-8")
    content = file.read().lower()
    file.close()
    return content

def write_file(path, content):
    file = open(path,"w+")
    json.dump(content, file, sort_keys=True, indent=4)
    file.close()

text = read_file("ngrams_implementation/all_lyrics.txt")
text = text.replace("<start> ","").replace(" <end>","")
sentences = text.lower().split("\n")
temp = [(word_tokenize(i)+["<end>"]) for i in sentences]

tokens = []
for i in temp:
    tokens += i

vocab = set(tokens)
dict1 = { "TOKENS" : [] }
dict1["TOKENS"] = tokens
write_file("ngrams_implementation/JsonDumps/dict_1_temp.json", dict1)