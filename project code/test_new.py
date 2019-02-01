file_read = open("training_image_features.txt","r")
for f in file_read:
    # print(f)
    # if f is None:
    #     break
    s=f.split(' ',1)[1]
    print(s)
    # break