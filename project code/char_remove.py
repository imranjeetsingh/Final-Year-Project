# import nltk
# from collections import defaultdict
# fp =open('feature1.txt', 'r')
# text = fp.read()
# print(text)
# print(" ".join(text.split())+'\n')
# file_set = open("setall_test.txt","r")
# file_ans = open("setall_test_data.txt","w")
# l=1
# for f in file_set:
#     file_ans.write(str(l)+'\t'+f)
#     l=l+1
# file_set = open("testnouns.txt","r")
# # file_ans = open("setall_test_data.txt","w")
# # l=1
# for f in file_set:
#     # file_ans.write(str(l)+'\t'+f)
#     l=f.split(' ',1)[0]
#     l1 = f.split(' ',1)[1]
#     print(l1)


# with open('xml_test_data.txt',"r") as fr:
#     sents=fr.readlines()
# for i in sents:
#     n=i.split('\t',1)[0]
#     tag_sent=i.split('\t',1)[1].strip()
#     print(n,tag_sent)
#     break
# p=1
# file_xml_data = open("testnouns.txt", "r")
# for img in file_xml_data:
#     xml_img_no = img.split(' ', 1)[0].split('\t',1)[0]
#     xml_word = img.split(' ', 1)[1].strip()
#     # xml_sen  = xml_word.split('\t',1)[1]
#     # xml_word = xml_word.split('\t',1)[0]
#     print(xml_img_no,xml_word)
#     if p==10:
#         break
#     p = p+1
    # print(xml_word)
    # print(xml_sen)
    # break
# file_data = open("testnouns.txt","r")
# file_ans  = open("test_demo.txt","w")
# l=1
# # prev = {}
# for f in file_data:
#     if l%2==0:
#         noun = f.split(' ',1)[1].strip()
#         # sen    = f.split(' ',1)[2].strip()
#         # print(noun)
#         file_ans.write(noun+'\n')
#         # file_ans.write()
#     else:
#         img_no = f.split('\t',1)[0]
#         sen    = f.split('\t',1)[1].strip()
#         # sen1    = f.split('\t',1)[2].strip()
#         file_ans.write(img_no+'\t'+sen+'\t')
#         # print(img_no,sen,se)
#     l=l+1
#     # break
#     # img_no = f.split(' ',1)[0].strip()
#     # sen    = f.split('\t',1)[1].strip()
#     # print(img_no,sen)
#     # print(l)
#     # if l==10:
#     #     break


# file_data = open("test_demo.txt","r")
# file_ans  = open("final_test_demo.txt","w")
# l=1
# prev = {}
# # prev = {}
# for f in file_data:
#     img_no = f.split('\t',1)[0].strip()
#     sen    = f.split('\t',1)[1].strip()
#     noun   = sen.split('\t',1)[1].strip()
#     sen    = sen.split('\t',1)[0].strip()
#     file_ans.write(img_no+'\t'+noun+'\t'+sen+'\n')
#     # if prev!=img_no:
#     #     l=1
#     #     prev=img_no
#     #     l=l+1
#     # else:
#     #     l=l+1

# file_xml_data = open("final_test_demo.txt", "r")
#             # traj_detail = 0
# for img in file_xml_data:
#     xml_img_no = img.split('\t', 1)[0]
#     xml_word1 = img.split('\t', 1)[1].split('\t',1)[0].strip()
#     xml_word = img.split('\t',1)[1].split('\t',1)[1].strip()
#     print(xml_img_no,xml_word1,xml_word)
#     break

