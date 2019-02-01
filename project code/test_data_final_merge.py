from __future__ import unicode_literals
import spacy
import nltk
from collections import defaultdict

nlp = spacy.load('en')
file_image = open("test_image_feature.txt","r")
file_ans   = open("test_ans_vector.txt","w")
# file_

file_tr = open("trfinal.txt","r")
# ans = []
tr=[]
for f in file_tr:
    a=f.split(',')[1].split('=')[1].split('[')[1].split(']')[0]
    tr.append(a)
# print(len(ans))

file_lm = open("lmfinal.txt","r")
# ans = []
lm=[]
for f in file_lm:
    a=f.split(',')[1].split('=')[1].split('[')[1].split(']')[0]
    lm.append(a)
lm_tr_index=0
for f in file_image:
    img_no = f.split(' ')[0].split('.')[0]
    vector = f.split(' ')[1].split(',')
    # print(vector)
    # break
    # print(img_no)
    # print(vector)
    feature_vector=[]
    for v in vector:
        v=(round(float(v),8))
        v=("{:.8f}".format(v))
        # print(v)
        feature_vector.append(str(v))
    # print(feature_vector)
    # break
    image_vector = " ".join(f for f in feature_vector)
    # print(image_vector)
    # file_ans.write(image_vector+" ")
    file_feature = open("features_test.txt","r")
    for feature in file_feature:
        # print(feature)
        feature        = feature.split("\t")
        feature_img_no = feature[0]
        feature_seg_no = feature[1]
        feature_value  = feature[2]
        feature_scene  = feature[3].strip()
        if str(img_no)==str(feature_img_no):
            file_text1 = open("test_label_word_xml_landmark_test.txt","r")
            for file_text in file_text1:
                text_img_no = file_text.split("\t")[0]
                text_segment_no = file_text.split("\t")[1]
                text_trajector = file_text.split("\t")[2]
                text_sentence  = file_text.split("\t")[3]
                # text_indicato  = file_text.split("\t")[4]
                if text_img_no == feature_img_no and text_segment_no == feature_seg_no:
                    file_ans.write(text_trajector.strip()+'\t'+text_sentence.strip()+'\t'+tr[lm_tr_index]+'\t'+lm[lm_tr_index]+'\n')
                    lm_tr_index=lm_tr_index+1
                    # text_trajector = unicode(text_trajector)
                    # doc = nlp(text_trajector)
                    # ans = []
                    # for doc in doc.vector:
                    #     ans.append(str(round(float(doc),8)))
                    # feature_value = " ".join(feature_value.split())
                    # ans = " ".join(d for d in ans)
                    # file_ans.write(image_vector+'\t'+feature_value+'\t'+ans+'\t')
                    # text_sentence = unicode(text_sentence)
                    # doc = nlp(text_sentence)
                    # ans1 = []
                    # for doc in doc.vector:
                    #     ans1.append(str(round(float(doc),8)))
                    # ans1 = " ".join(d for d in ans1)
                    # file_ans.write(ans+'\n')
                # f=[]
            # f.append(str(feature_vector))
