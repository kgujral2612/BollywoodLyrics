import json
from nltk.tokenize import word_tokenize

def train(lines):
    bigrams_dict = {}
    for line in lines:
        temp = ["<start>"] + word_tokenize(line) + ["<end>"]
        for idx in range(len(temp)-1):
            x, y = temp[idx:idx+2]
            if y not in bigrams_dict.keys():
                bigrams_dict[y]=[]
            bigrams_dict[y].append(x)
    return bigrams_dict

f = open("all_lyrics.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

text = text.replace("<start> ","").replace(" <end>","")
text = text.replace("<start>","").replace("<end>","")

lines = text.split("\n")
total_sen = len(lines)
print(total_sen)

print(len(lines))
bigrams_dict = train(lines)

fp = open("ngrams_implementation/JsonDumps/dict_2.json", "w+")
json.dump(bigrams_dict, fp, sort_keys=True, indent=4)
fp.close()