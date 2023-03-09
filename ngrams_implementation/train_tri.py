import json
from nltk.tokenize import word_tokenize

def train(lines):
    trigrams_dict = {}
    for line in lines:
        temp = ["<start>"] + word_tokenize(line) + [r"<end>"]*2
        for idx in range(len(temp)-2):
            z, x, y = temp[idx:idx+3]
            if tuple([x,y]) not in trigrams_dict.keys():
                trigrams_dict[tuple([x,y])]=[]
            trigrams_dict[tuple([x,y])].append(z)
    return trigrams_dict

f = open("all_lyrics.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

text = text.replace("<start> ","").replace(" <end>","")
text = text.replace("<start>","").replace("<end>","")

tokens = word_tokenize(text.lower())
vocab = set(tokens)

lines = text.lower().split("\n")
print(len(lines))
trigrams_dict = train(lines)

json_dict = {}
count = 1
for k in trigrams_dict.keys():
    json_dict["k"+str(count)] = list(k)
    json_dict["v"+str(count)] = trigrams_dict[k]
    count = count+1

fp = open("ngrams_implementation/JsonDumps/dict_3.json","w+")
json.dump(json_dict, fp)
fp.close()