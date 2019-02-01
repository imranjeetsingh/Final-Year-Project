# import nltk
# # nltk.download('wordnet')
# from nltk.corpus import wordnet
# # Let's compare the noun of "ship" and "boat:"

# w1 = wordnet.synset('Ranjeet run') # v here denotes the tag verb
# w2 = wordnet.synset('sprint')
# print(w1.wup_similarity(w2))
import csv

file_data = open("trainnew.txt","r")
file_ans  = open("trainewdata.txt","w")
for f in file_data:
        data = int(f.split('\t')[0])
        sentence = f.split('\t')[1]
        noun = f.split('\t')[2].strip()
        # print(sentence)
        # break
        # print(data)
        # break
        file_tr = open("trainnew.csv", "r")
        file_tr_new = csv.reader(file_tr, delimiter='\t')
        i=0
        for index in file_tr_new:
                if i==0:
                        i=i+1
                        continue
                cmp_index = index[0].split(',')[2]
                img_no    = index[0].split(',')[0].split('/')[2].split('.')[0]
                if str(cmp_index) == str(data):
                        file_ans.write(img_no+'\t'+sentence+'\t'+noun+'\n')
                        break
                # print(cmp_index,img_no)
                # break
        # break

# i = 1
# temp = 0
# for f in file_tr_new:
#         # if temp == 1:
#         #     break
#         # if i == 1:
#         #     i = i+1
#         #     continue
#         tr_word = f[4]
#         sentence_num = f[0]
#         print(tr_word,sentence_num)
#         # # print(sentence_num)
#         # if tr_word == word_detail:
#         #     file_set = open("setall_data.txt", "r")
#         #     # i=1
#         #     for sen in file_set:
#         #         index = sen.split('\t')[0]
#         #         sentence = sen.split('\t')[1].strip()
#         #         if index == sentence_num:
#         #             file_ans.write(word_detail + '\t')
#         #             file_ans.write(sentence+'\t' + str(similarity))
#         #             file_ans.write('\n')
#         #             if temp == 1:
#         #                 break
#         #         if temp == 1:
#         #             break


