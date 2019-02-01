# TO read tsv file

#import csv
#file_open = open("LANDMARK.tsv","r")
#for file in file_open:
#file = csv.reader(file_open,delimiter='\t')
#ans = open("landmark_data.txt","w")
#i=0;
#for file in file:
# print(file[4])
 #i=i+1
 #if i==1:
  #continue
 #ans.write(file[0])
 #ans.write(" ")
 #ans.write(file[4])
 #ans.write("\n")


from __future__ import unicode_literals
import spacy
nlp = spacy.load('en')

file_setall  = open("setall_data.txt", "r")
file_ans = open("train_landmark.txt","w")

l=0
for line in file_setall:
 l=line.split(' ', 1)[0]
 setall_data = line.split(' ', 1)[1]
 setall_data=setall_data.strip()
 line_set = str(setall_data)
 doc = nlp(line_set)
 file_ans.write(l)
 file_ans.write("\n")
 ans = []
 for doc in doc.vector:
  ans.append(round(float(doc),8))
 #print(setall_data)
 file_ans.write(str(ans))
 file_ans.write("\n")
 file_trajector = open("landmark_data.txt","r")
 for lines in file_trajector:
  lines.split()
  k=lines.split(' ', 1)[0]
  word = str()
  if str(k)==str(l):
   word=lines.split(' ', 1)[1].strip()
   word_set = str(word)
   doc1 = nlp(word_set)
   ans1 = []
   for doc in doc1.vector:
    ans1.append(round(float(doc),8))
 #print(setall_data)
   file_ans.write(str(ans1))
   file_ans.write("\n")
   #print(word)
