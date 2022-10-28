without_handle = input("文章")
half_handle = without_handle.split()
if len(half_handle) > 1:
    print(len(half_handle[-2]))
else:
    print("0")

q_handle = without_handle.split("ld")
fin_handle = ""
for i in q_handle:
    fin_handle += i
ori = len(without_handle)
now = len(fin_handle)

print(int((ori - now)/2))
