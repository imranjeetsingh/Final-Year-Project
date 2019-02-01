from __future__ import unicode_literals
import spacy
import nltk
from collections import defaultdict

nlp = spacy.load('en')
file_image = open("training_image_features.txt","r")
file_ans   = open("ans1_new_landmark_vector.txt","w")
# file_
for f in file_image:
    img_no = f.split(' ')[0].split('.')[0].strip()
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
    file_data = open("new_label1_word_train.txt","r")
    for data in file_data:
        data_img_no = data.split('\t')[0].strip()
        data_seg_no = data.split('\t')[1].strip()
        data_trajector = data.split('\t')[3].strip()
        data_sentence = data.split('\t')[4].strip()
        data_similarity = data.split('\t')[5].strip()
        if img_no==data_img_no:
            file_feature = open("features.txt","r")
            flag = 0
            feature_value = str()
            for feature in file_feature:
                # print(feature)
                feature        = feature.split("\t")
                feature_img_no = feature[0].strip()
                feature_seg_no = feature[1].strip()
                if feature_img_no==data_img_no and feature_seg_no==data_seg_no:
                    feature_value  = feature[2].strip()
                feature_scene  = feature[3].strip()
                if str(data_img_no)==str(feature_img_no) and data_seg_no==feature_seg_no:
                    file_traj = open("Trajector_new_data.txt","r")
                    for tr in file_traj:
                        tr_img_no = tr.split('\t')[0].strip()
                        trajector = tr.split('\t')[1].strip()
                        sen = tr.split('\t')[2].strip()
                        if tr_img_no==feature_img_no and trajector==data_trajector and data_sentence==sen:
                            flag = 1
                            break
                if flag==1:
                    break
            text_trajector = unicode(data_trajector)
            doc = nlp(text_trajector)
            ans_traj = []
            feature_value = " ".join(feature_value.split())
            for doc in doc.vector:
                ans_traj.append(str(round(float(doc),8)))
                # ans_traj = " ".join(d for d in ans_traj)
                # file_ans.write(image_vector+'\t'+feature_value+'\t'+ans+'\t')
            text_sentence = unicode(data_sentence)
            doc = nlp(text_sentence)
            ans_sen = []
            for doc in doc.vector:
                ans_sen.append(str(round(float(doc),8)))
            # ans1 = " ".join(d for d in ans1)
                # file_ans.write(ans1+'\t'+text_indicato)
            final_traj = " ".join(d for d in ans_traj)
            final_sen = " ".join(d for d in ans_sen)
            if data_similarity>0.20 and flag==1:
                file_ans.write(image_vector+'\t'+feature_value+'\t'+final_traj+'\t'+final_sen+'\t'+str(1)+'\n')
            else:
                file_ans.write(image_vector+'\t'+feature_value+'\t'+final_traj+'\t'+final_sen+'\t'+str(0)+'\n')
                           
                            




                    # file_text1 = open("label_word_xml_landmark_test.txt","r")
                    # for file_text in file_text1:
                    #     text_img_no = file_text.split("\t")[0]
                    #     text_segment_no = file_text.split("\t")[1].strip()
                    #     text_trajector = file_text.split("\t")[2].strip()
                    #     text_sentence  = file_text.split("\t")[3].strip()
                    #     text_indicato  = file_text.split("\t")[4].strip()
                    #     if text_img_no == feature_img_no and text_segment_no == feature_seg_no:
                    #         text_trajector = unicode(text_trajector)
                    #         doc = nlp(text_trajector)
                    #         ans = []
                    #         for doc in doc.vector:
                    #             ans.append(str(round(float(doc),8)))
                    #         feature_value = " ".join(feature_value.split())
                    #         ans = " ".join(d for d in ans)
                    #         file_ans.write(image_vector+'\t'+feature_value+'\t'+ans+'\t')
                    #         text_sentence = unicode(text_sentence)
                    #         doc = nlp(text_sentence)
                        #     ans1 = []
                        #     for doc in doc.vector:
                        #         ans1.append(str(round(float(doc),8)))
                        #     ans1 = " ".join(d for d in ans1)
                        #     file_ans.write(ans1+'\t'+text_indicato)
                        # # f=[]
                    # f.append(str(feature_vector))