import csv
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn

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

file_data = open("trainewdata.txt", "r")
file_ans = open("new_label1_word_train.txt", "w")

for line in file_data:
    image_no = line.split('\t')[0].strip()
    sentence = line.split('\t')[1].strip()
    noun = line.split('\t')[2].strip()
    file_label = open("labels.txt","r")
    similarity = 0.0
    scene = str()
    seg_no = str()
    for label in file_label:
        label_img_no = label.split('\t')[0].strip()
        label_img_segno = label.split('\t')[1].strip()
        label_scene_no  = label.split('\t')[2].strip()
        if str(label_img_no)==str(image_no):
            file_wlist = open("wlist.txt","r")
            for wlist in file_wlist:
                scene_no = wlist.split('\t')[0].strip()
                scene_word = wlist.split('\t')[1].strip()
                if str(scene_no)==str(label_scene_no):
                    word = str()
                    for w in scene_word:
                        if w == "-":
                            word = word+" "
                        else:
                            word = word+w
                    similarity1 = sentence_similarity(word, noun)
                    if similarity1>=similarity:
                        similarity = similarity1
                        scene = word
                        seg_no = label_img_segno
    if similarity>=0.20:
        file_ans.write(image_no+'\t'+seg_no+'\t'+scene+'\t'+noun+'\t'+sentence+'\t'+str(similarity)+'\n')
    else:
        file_label1 = open("labels.txt","r")
        similarity1 = 0.0
        scene1 = str()
        seg_no1 = str()
        img_no = str()
        for label1 in file_label1:
            label_img_no_1 = label1.split('\t')[0].strip()
            label_img_segno_1 = label1.split('\t')[1].strip()
            label_scene_no_1  = label1.split('\t')[2].strip()
            file_wlist_1 = open("wlist.txt","r")
            flag = 0
            for wlist1 in file_wlist_1:
                scene_no1 = wlist1.split('\t')[0].strip()
                scene_word1 = wlist1.split('\t')[1].strip()
                if scene_no1==label_scene_no_1:
                    flag = 1
                    word = str()
                    for w in scene_word1:
                        if w == "-":
                            word = word+" "
                        else:
                            word = word+w
                    similarity2 = sentence_similarity(word, noun)
                    if similarity2>=similarity1:
                        similarity1 = similarity2
                        scene1 = word
                        seg_no1 = label_img_segno_1
                        img_no = label_img_no_1
                elif flag==1:
                    break
        file_ans.write(img_no+'\t'+seg_no1+'\t'+scene1+'\t'+noun+'\t'+sentence+'\t'+str(similarity1)+'\n')
