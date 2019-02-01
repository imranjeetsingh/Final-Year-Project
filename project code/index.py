file_ans = open("setall_test1.txt","w")
file_setall  = open("setall_test.txt", "r")
l=1
for line in file_setall:
 file_ans.write(str(l))
 file_ans.write(" ")
 file_ans.write(line)
 print(line)
 l=l+1
