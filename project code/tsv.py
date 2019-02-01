import csv
file_open = open("sentwrdindex.csv", "r")
# for file in file_open:
# file = csv.reader(file_open,delimiter='\t')
# ans = open("trajector_data.txt","w")
# i=0
# for file in file:
#     # print(file[4])
#     i = i+1
#     if i==1:
#         continue
#     ans.write(file[0])
#     ans.write(" ")
#     ans.write(file[4])
#     ans.write("\n")

# file_tr = open("TRAJECTOR.tsv", "r")
file_tr_new = csv.reader(file_open, delimiter='\t')
# for f in file_tr_new:
#                 tr_word = f[4]
#                 sentence_num = f[1]
#                 if tr_word == word_detail:
#                     file_set = open("setall_data.txt", "r")
#                     i = 1
#                     for sen in file_set:
#                         if i == 1:
#                             i = i+1
#                             continue
#                         index = sen.split('\t')[0]
#                         sentence = sen.split('\t')[1]
#                         if index == sentence_num:
#                             file_ans.write(word_detail + ' ')
#                             file_ans.write(sentence)
# file_ans = open("new_ans.txt","w")

# # <LANDMARK id="L1" start="7" end="9" text="it"/>
# l=1
# for f in file_tr_new:
#     if int(f[5])==1:
#         ans=("{}".format(f[1]))
#         # a = (""{}"".format)
#         file_ans.write("<LANDMARK id=L"+str(l)+" start="+str(f[2])+" end="+str(f[3])+" text="+ans+"/>"+'\n')
#         l=l+1

file_ans = open("new_ans_tr.txt","w")
file_read = open("quote.txt","r").read().strip()
# print(file_read)
# ans=[]
# ans.append("")
# print(ans)
# <LANDMARK id="L1" start="7" end="9" text="it"/>
# l=1
# for f in file_tr_new:
#     if int(f[5])==1:
#         # '%s %s' % ('one', 'two')
#         # ans=('%s'%(""))
#         # print(ans)
#         # a = (""{}"".format)
#         file_ans.write("<LANDMARK id="+file_read+str("L")+str(l)+file_read+" start="+file_read+str(f[2])+file_read+" end="+file_read+str(f[3])+file_read+" text="+file_read+f[1].strip()+file_read+"/>"+'\n\n'+f[0]+'\n\n')
#         l=l+1

l=1
for f in file_tr_new:
    if int(f[4])==1:
        # '%s %s' % ('one', 'two')
        # ans=('%s'%(""))
        # print(ans)
        # a = (""{}"".format)
        file_ans.write("<TRAJECTOR id="+file_read+str("T")+str(l)+file_read+" start="+file_read+str(f[2])+file_read+" end="+file_read+str(f[3])+file_read+" text="+file_read+f[1].strip()+file_read+"/>"+'\n\n'+f[0]+'\n\n')
        l=l+1















# filer = open("setall_ans.txt","r")
# i=1;
# for f in filer:
#     if i>2:
#         break;
#     print(f)
#     i=i+1


# from __future__ import unicode_literals
# import spacy
# nlp = spacy.load('en')

# file_setall  = open("testnouns.txt", "r")
# file_ans = open("test_noun_vector.txt","w")

# # l=0
# for line in file_setall:
#  l=line.split(' ', 1)[0]
#  setall_data = line.split(' ', 1)[1]
#  setall_data=setall_data.strip()
#  line_set = unicode(setall_data)
#  doc = nlp(line_set)
#  file_ans.write(l)
#  file_ans.write("\n")
# #  file_ans.write(doc)
#  ans = []
#  for doc in doc.vector:
#   ans.append(round(float(doc),8))
#  #print(setall_data)
#  file_ans.write(str(ans))
#  file_ans.write("\n")
# #  file_trajector = open("trajector_data.txt","r")
# #  for lines in file_trajector:
# #   lines.split()
# #   k=lines.split(' ', 1)[0]
# #   word = str()
# #   if str(k)==str(l):
# #    word=lines.split(' ', 1)[1].strip()
# #    word_set = str(word)
# #    doc1 = nlp(word_set)
# #    ans1 = []
# #    for doc in doc1.vector:
# #     ans1.append(round(float(doc),8))
# #  #print(setall_data)
# #    file_ans.write(str(ans1))
# #    file_ans.write("\n")
# #    #print(word)
