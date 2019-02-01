import nltk
import pprint
import sys
import xlrd 
import re
import xlsxwriter
import xlwt
from bllipparser import RerankingParser
from nltk.tree import Tree
rrp = RerankingParser.from_unified_model_dir('/home/codecook/.local/share/bllipparser/WSJ-PTB3')



sents=[]
def foo(s1):                           #function for adding '' to the beginning and end of string i.e parsed output
 return "%s" % s1 

file_ans = open("test_noun_data.txt","w")
with open('xml_test_data.txt',"r") as fr:
 sents=fr.readlines()
 #print line
 #sents=list(fr)

#for j in sents:
# print j
grammar =r"""
  NP:         
      {<PRP>}
      {<RB>?<DT>?<JJ>*<NN>+}  # Chunk sequences of DT, JJ, NN
      {<DT>?<JJ>*<NN>+}
      #{<CD><NNS>+}
      {<RB>?<CD>?<NNS>+}
      {<NP>?<CC>?<NP>}
      {<DT><NN>?<DT><NN>}
"""
 
cp = nltk.RegexpParser(grammar)  
# n=0
for i in sents:
    n=i.split('\t',1)[0]
    tag_sent=rrp.tag(i.split('\t',1)[1].strip())
    chunk=cp.parse(tag_sent)
    tree = chunk
    for node in tree:
     if type(node) is nltk.Tree:
      if node.label()=='NP':
        npnode=foo(node)
        npnew=nltk.Tree.fromstring(npnode,read_leaf=lambda x: x.split("/")[0])
        parse_sent=rrp.parse(i)
  #  for te in parse_sent[0].ptb_parse.sd_tokens():
        print n," ".join(npnew.leaves())
