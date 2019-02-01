file_read = open("Trajector_data.txt","r")
file_ans  = open("Trajector_new_data.txt","w")
for f in file_read:
    num = f.split('\t')[0].strip()
    noun = f.split('\t')[1].strip()
    sen = f.split('\t')[2].strip()
    # sen = sen.lower()
    file_ans.write(num+'\t'+noun.lower()+'\t'+sen.lower()+'\n')