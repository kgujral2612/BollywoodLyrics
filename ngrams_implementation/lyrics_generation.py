import json
import math
import random


def list_of_random_nums(limit, size):
    counter = 0
    list_rand = []
    new = 0
    while (counter < size):
        new = random.randint(0, limit-1)
        if new not in list_rand:
            list_rand.append(new)
            counter = counter + 1
    return (list_rand)


# user input
print("Please enter a rhyme scheme. For eg: AABB, ABAB, ABCABC, AACBBC, etc: ")
rhyme_scheme = input()
print("Please enter the number of stanzas you'd like to generate: ")
stanza = int(input())
# identify types such as 'A', 'B', 'C', et cetera
types = list(set(i for i in rhyme_scheme))


def file_content(path):
    file = open(path, encoding="utf-8")
    content = json.load(file)
    file.close()
    return content


# get rhymes from json file
temp_list = file_content("ngrams_implementation/JsonDumps/rhymes.json")
# get n grams from files
dict1 = file_content("ngrams_implementation/JsonDumps/dict_1.json")
dict2 = file_content("ngrams_implementation/JsonDumps/dict_2.json")
dict3 = file_content("ngrams_implementation/JsonDumps/dict_3.json")
count = 1
maxima = max([int(i[1:]) for i in dict3.keys()])
dicttemp = {}
while (True):
    if count < maxima:
        dicttemp[tuple(dict3["k"+str(count)])] = dict3[("v"+str(count))]
        count = count + 1
    else:
        print("dict3 - ", str(count))
        dict3 = dicttemp
        dicttemp = {}
        break

new_keys = [i for i in temp_list.keys() if len(temp_list[i]) >= stanza]

rhyme_scheme_for_types = list_of_random_nums(len(new_keys), len(types))
n_dict_for_rhyme = {}
c = 0

for t in types:
    n_dict_for_rhyme[t] = new_keys[rhyme_scheme_for_types[c]]
    c += 1

main_dic_for_rhyme = {}
for line in types:
    main_dic_for_rhyme[line] = []
    stanza_endings = list_of_random_nums(
        len(temp_list[n_dict_for_rhyme[line]]), stanza)
    for last_two_words in stanza_endings:
        main_dic_for_rhyme[line].append(
            temp_list[n_dict_for_rhyme[line]][last_two_words])
rhyme = []
for line in range(stanza):
    for last_two_words in rhyme_scheme:
        rhyme.append(main_dic_for_rhyme[last_two_words][line])
    rhyme.append(" ")

print(rhyme)

sum_of_log = 0
total_pred = 0

for line in rhyme:
    if line != " ":
        last_two_words = (line.split())[0:2]
        #print("\n", last_two_words)
        ### last word prob ###
        total_last_words = len(dict2["<end>"])
        num_last_word = dict2["<end>"].count(last_two_words[1])
        prob_log = math.log(num_last_word/total_last_words)
        #print("P(last word)", prob_log)
        sum_of_log -= prob_log
        total_pred += 1

        ### second last word prob ###
        total_last_two_words = len(dict3[tuple([last_two_words[1], "<end>"])])
        num_last_two_words = dict3[tuple(
            [last_two_words[1], "<end>"])].count(last_two_words[0])

        prob_log = math.log(num_last_two_words/total_last_two_words)
        #print("P(second last word)", prob_log)
        sum_of_log -= prob_log
        total_pred += 1

#print("\nsum: ", sum_of_log)
#print("total_pred", total_pred)
#print(math.exp(sum_of_log/total_pred))


sent_sum_of_log = 0
sent_total_pred = 0

# generate lyrics and calculate perplexity

lyrics = []
final = []
for i in rhyme:
    if i == " ":
        lyrics.append(" ")
    else:
        while (True):
            if len(final) > 5 and len(final) < 11:
                lyrics.append((" ").join(final))
                final = []
                sum_of_log -= sent_sum_of_log
                total_pred += sent_total_pred
                break

            sent_sum_of_log = 0
            sent_total_pred = 0
            previous = (i.split())[0:2]
            final = previous

            predicted = ""
            check = []
            while (True):
                if predicted == "<start>":
                    break
                if tuple(previous) in dict3.keys():
                    predicted = random.choice(dict3[tuple(previous)])
                    deno = len(dict3[tuple(previous)])
                    num = dict3[tuple(previous)].count(predicted)
                    sent_sum_of_log += math.log(num/deno)
                    sent_total_pred += 1
                elif previous[1] in dict2.keys():
                    predicted = random.choice(dict2[previous[1]])
                else:
                    predicted = random.choice(dict1["TOKENS"])
                check = check+[previous]
                previous = [predicted, previous[0]]
                final = [predicted] + final


for i in lyrics:
    print(i)


print(" Perplexity:")
print(math.exp(sum_of_log/total_pred))
