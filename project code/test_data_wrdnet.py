import csv
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
# file_xml_data  = open("xml_data.txt","r")
# for img in file_xml_data:
#         xml_img_no = img.split(' ', 1)[0]
#         xml_word   = img.split(' ', 1)[1].strip()
#         print(xml_img_no,xml_word)


def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = 0
        for ss in synsets2:
            best_score = max(best_score, synset.path_similarity(ss))
        # best_score = max([synset.path_similarity(ss) for ss in synsets2])

        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1

    # Average the values
    if count == 0:
        return 0
    score /= count
    return score


# Reading file label.txt, wlist.txt, xml_data.txt

file_labels = open("labels_test.txt", "r")
file_ans = open("test_label_word_xml_landmark_test.txt", "w")
# # file_word_list  = open("wlist.txt","r")
# # for word in file_word_list:
# #     word_index     = word.split('\t', 1)[0]
# #     word_match     = word.split('\t', 1)[1].strip()
# #     print(word_index, word_match)
for line in file_labels:
    image_no = line.split('\t', 2)[0]
    segment_no = line.split('\t', 2)[1]
    word_list_match_no = line.split('\t', 2)[2].strip()
#     print(image_no, segment_no, word_list_match_no)
    # file_ans.write(image_no+'\t'+segment_no+'\t')
    file_word_list = open("wlist.txt", "r")
    similarity = 0
    word_detail = str()
    word11=str()
    sen_no = {}
    # word_match  = str()
    for word in file_word_list:
        word_index = word.split('\t', 1)[0]
        word_match = word.split('\t', 1)[1].strip()
        if str(word_index) == str(word_list_match_no):
            # file_ans.write(word_match+'\t')
            file_xml_data = open("final_test_demo.txt", "r")
            # traj_detail = 0
            for img in file_xml_data:
                xml_img_no = img.split('\t', 1)[0]
                xml_word = img.split('\t', 1)[1].split('\t',1)[0].strip()
                xml_word1 = img.split('\t',1)[1].split('\t',1)[1].strip()
                # xml_img_no = img.split('\t', 1)[0]
                # xml_word1 = img.split('\t', 1)[1].strip()
                # xml_word =  img.split('\t',1)[2].strip()
                # xml_sen   = img.split('\t',1)[2].strip()
                # xml_sen  = img.split('\t',1)[2].strip()
                # print(xml_img_no,xml_word)

                if str(image_no) == str(xml_img_no):
                    word1 = str()
                    for w in word_match:
                        if w == "-":
                            word1 = word1+" "
                        else:
                            word1 = word1+w
                    word2 = str()
                    for w in xml_word:
                        if w == "-":
                            word2 = word2+" "
                        elif w == ",":
                            continue
                        else:
                            word2 = word2+w
                    
                    similarity1 =sentence_similarity(word2, word1)
                    if(similarity1>=similarity):
                        similarity = similarity1
                        word_detail = xml_word
                        sen_no      = xml_word1
    # if similarity>=0.20:
    if similarity!=0:
        file_ans.write(image_no+'\t'+segment_no+'\t'+str(word_detail)+'\t'+str(sen_no)+'\n')
    # elif similarity!=0:
        # file_ans.write(image_no+'\t'+segment_no+'\t'+str(word_detail)+'\t'+str(sen_no)+'\t'+str("0")+'\n')

                #     file_ans.write(word1+" "+word2+"\n")
                #    word_match = word_match.split()
                #    print(word1)
    
    # file_ans.write(image_no+'\t'+segment_no+'\t'+word_detail+str(similarity)+'\n')
    # # print(word_detail,similarity)
    # file_ans.write(word_detail+'\t'+str(similarity)+'\n')
    # if word_detail==None:
    #     file_set = open("setall_data.txt","r")
    #                                 # i=1
    #         for setf in file_set:
    #             index = sen.split('\t')[0]
    #             sentence = sen.split('\t')[1].strip()
    #             if index == :
    #                 file_ans.write(word_detail + '\t')
    #                 file_ans.write(sentence+'\t'+ str(similarity))
    #                 file_ans.write('\n')
    #     continue
    # file_tr = open("TRAJECTOR.tsv","r")
    # file_tr_new = csv.reader(file_tr,delimiter='\t')
    # i=1
    # # print(word2,word_match)
    # temp=0
    # for f in file_tr_new:
    #     if temp==1:
    #         break
    #     if i==1:
    #         i=i+1
    #         continue
    #     tr_word = f[4].strip()
    #     sentence_num = f[0].strip()
    #                             # print(sentence_num)
    #     # word11 = str()
    #     # for w in tr_word:
    #     #         if w == "-" or w ==',':
    #     #             word11 = word11+" "
    #     #         else:
    #     #             word11 = word11+w
    #     # tr_word = word11
    #     if str(tr_word)==str(word_detail.strip()):
    #         file_set = open("setall_data.txt","r")
    #                                 # i=1
    #         for sen in file_set:
    #             index = sen.split('\t')[0]
    #             sentence = sen.split('\t')[1].strip()
    #             if index == sentence_num:
    #                 # file_ans.write(image_no+'\t'+segment_no+'\t')
    #                 if similarity >= 0.20:
    #                     file_ans.write(image_no+'\t'+segment_no+'\t'+word_detail+'\t'+sentence+'\t'+str(similarity)+'\t'+"1"+'\n')
    #                 else:
    #                     file_ans.write(image_no+'\t'+segment_no+'\t'+word_detail+'\t'+sentence+'\t'+str(similarity)+'\t'+"0"+'\n')
    #                 temp=1
    #                 if temp==1:
    #                     break
    #             if temp==1:
    #                 break
        
    #         # break
    #             # break
    #         # file_ans.write("\n")
