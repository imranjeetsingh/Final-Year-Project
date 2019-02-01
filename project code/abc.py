from __future__ import unicode_literals
import spacy
nlp = spacy.load('en')
file_image = open("training_image_features.txt","r")
file_ans   = open("ans_new.txt","w")
# file_
for f in file_image:
    img_no = f.split(' ')[0].split('.')[0]
    vector = f.split(' ')[1].split(',')
    # print(img_no)
    # print(vector)
    feature_vector=[]
    for v in vector:
        v=(round(float(v),8))
        v=("{:.8f}".format(v))
        # print(v)
        feature_vector.append(str(v))
    # print(feature_vector)
    # file_ans.write(str(feature_vector)+" ")
    file_feature = open("feature1.txt","r")
    for feature in file_feature:
        # print(feature)
        feature        = feature.split("\t")
        feature_img_no = feature[0]
        feature_seg_no = feature[1]
        feature_value  = feature[2]
        feature_scene  = feature[3].strip()
        # f  = []
        # count=0
        # for feature_val in feature_value:
        #     # feature = feature_val.strip()
        #     # print(feature_val)
        # #     if count%8==0:
        #     a = float(feature_val.strip())
        #     f.append(a)
        # print(len(f))
        #         # print("1")
        #     count=count+1
        # print(count)
        # # print(feature_value)
        # print(feature_scene)
        if str(img_no)==str(feature_img_no):
            # f=[]
            # f.append(str(feature_vector))
            file_ans.write(str(feature_vector)+'\t'+str(feature_value)+'\n')
    #     trajector=[]
    #     file_xml = open("xml_data.txt","r")
    #     for xml in file_xml:
    #         xml=xml.split("\t")
    #         tr_no = xml[0]
    #         tr_word = xml[1].strip()
    #         # print(tr_no,tr_word,img_no)
    #         # break
    #         if tr_no == img_no:
    #             # print(tr_no,tr_word,img_no)
    #             trajector.append(tr_word)
    #             # xml[1]
    #     # print(trajector)
    #     break
    # break
    # break
    # print(feature_vector)
# file_a=open("ran.txt","r")
# for i in file_a:
#     print(i)
#     break