file_read = open("trfinal.txt","r")
# ans = []
ans=[]
for f in file_read:
    a=f.split(',')[1].split('=')[1].split('[')[1].split(']')[0]
    ans.append(a)
print(ans[2459])
    # print(len(f))
    # for i in f:
        # print(i)
        # ans.append(i)
        # break
#     ans.append(int(fa) for fa in f)
#     # break
# print(len(ans))
# print(ans)

# file_read = open("final_test_demo.txt","r")
# ans = 0
# for f in file_read:
#     ans=ans+1
# #     f=f.split(",")
# #     # print(len(f))
# #     for i in f:
# #         # print(i)
# #         ans.append(i)
# #         # break
# # #     ans.append(int(fa) for fa in f)
# # #     # break
# print(ans)Best regards,
