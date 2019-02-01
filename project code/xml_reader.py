from xml.dom import minidom
xmldoc = minidom.parse('sprl2017_train_v01.xml')
file_ans = open("Trajector_data.txt","w")
itemlist = xmldoc.getElementsByTagName('SCENE')
for item in itemlist:
    doc_no      = str(item.getElementsByTagName('DOCNO')[0].firstChild.data).split("/")[2].split(".")[0]
    sentence    = item.getElementsByTagName('SENTENCE')
    for sentences in sentence:
        # trajector = sentences.getElementsByTagName('TEXT')[0].firstChild.data
        # file_ans.write(doc_no+'\t'+trajector+'\n')
        # for item in trajector:
        #     data    = item.attributes['text'].value
        #     file_ans.write(doc_no+"\t")
        #     file_ans.write(data)
        #     file_ans.write("\n")
        trajector = sentences.getElementsByTagName('TRAJECTOR')
        sen       = sentences.getElementsByTagName('TEXT')[0].firstChild.data.strip()
        for item in trajector:
            data    = item.attributes['text'].value
            file_ans.write(doc_no+'\t')
            file_ans.write(data+'\t'+sen)
            file_ans.write("\n")
            # print(data)
        # print(trajector)

# from xml.dom import minidom
# xmldoc = minidom.parse('sprl2017_train_v01.xml')
# file_ans = open("Landmark_data.txt", "w")
# itemlist = xmldoc.getElementsByTagName('SCENE')
# for item in itemlist:
#     doc_no = str(item.getElementsByTagName('DOCNO')[
#                  0].firstChild.data).split("/")[2].split(".")[0]
#     sentence = item.getElementsByTagName('SENTENCE')
#     # print(doc_no)
#     for sentences in sentence:
#         trajector = sentences.getElementsByTagName('LANDMARK')
#         sen       = sentences.getElementsByTagName('TEXT')[0].firstChild.data.strip()
#         for item in trajector:
#                 try:
#                         data = item.attributes['text'].value
#                         file_ans.write(doc_no.strip()+'\t'+data.strip()+'\t'+sen.strip()+'\n')
#                         # file_ans.write(data+'\t'+sen+'\n')
#                 except:
#                         # file_ans.write(doc_no+'\t'+data+'\t'+""+'\n')
#                         pass
#                         # file_ans.write(doc_no+'\t')
#                         # file_ans.write(""+'\t'+sen+'\n')
#             # print(data)
