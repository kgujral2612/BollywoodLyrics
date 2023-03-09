import re,json
file = open('all_lyrics.txt','r')
lines = file.read().split("\n")
file.close()

lst = []
for line in lines:
    match = re.search(r'(.{5}) <end>',line)
    word = re.search(r'([^\s]* [^\s]*) <end>',line)
    try:
        lst.append([match.group(1), word.group(1)])
    except:
        pass

diction = {}
for line in lst:
    if line[0] not in diction.keys():
        diction[line[0]] = [0,[]]
    diction[line[0]][0]+=1
    diction[line[0]][1].append(line[1])

out = []

imp = {}
for line in sorted(list(set([z[0] for z in diction.values()]))):
    if line>400:
        for j in diction.keys():
            if diction[j][0]==line:
                imp[j] = diction[j]

temp_list={}

for line in imp.keys():
    temp_list[line] = []    
    sett = sorted(list(set(imp[line][1])))
    if line!=' mein' and line!=' main':
        temp_list[line] = [(j+" _ "+str(diction[line][1].count(j))) for j in sett if diction[line][1].count(j)>39]

sett = sorted(list(set(imp[" main"][1])))
temp_list["ME"] = [(j+" _ "+str(diction[' main'][1].count(j))) for j in sett if diction[' main'][1].count(j)>39]
sett = sorted(list(set(imp[" mein"][1])))
temp_list["ME"] = temp_list["ME"] + [(j+" _ "+str(diction[' mein'][1].count(j))) for j in sett if diction[' mein'][1].count(j)>39]

f = open('ngrams_implementation/JsonDumps/rhymes.json','w+',encoding='utf-8')
json.dump(temp_list, f, indent=4)
f.close()