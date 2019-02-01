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

file_labels = open("labels.txt", "r")
file_ans = open("label_word_xml.txt", "w")
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
    file_word_list = open("wlist.txt", "r")
    for word in file_word_list:
        word_index = word.split('\t', 1)[0]
        word_match = word.split('\t', 1)[1].strip()
        if str(word_index) == str(word_list_match_no):
            file_xml_data = open("xml_data.txt", "r")
            similarity = []
            for img in file_xml_data:
                xml_img_no = img.split(' ', 1)[0]
                xml_word = img.split(' ', 1)[1].strip()
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
                    similarity.append(sentence_similarity(word2, word1))
                #     file_ans.write(word1+" "+word2+"\n")
                #    word_match = word_match.split()
                #    print(word1)
            ans=0
            for i in similarity:
                    ans = max(ans,i)
            for i in similarity:
                    if i==ans:
                        file_ans.write(image_no+" "+segment_no+" "+str(1)+"\n")
                        # file_ans.write(str(1)+" ")
                    else:
                        file_ans.write(image_no+" "+segment_no+" "+str(0)+"\n")