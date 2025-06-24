alpabet=input()
count=0

for i in range(alpabet.__len__()):
    if ("c=" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("c="," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("c-" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("c-"," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("dz=" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("dz="," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//3
    elif ("d-" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("d-"," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("lj" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("lj"," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("nj" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("nj"," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("s=" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("s="," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
    elif ("z=" in alpabet):
        string_len=alpabet.replace(" ", "")
        alpabet=alpabet.replace("z="," ")
        alpabet_temp= alpabet.replace(" ", "")
        remove_stirng=alpabet_temp.__len__()
        count+=(string_len.__len__()-remove_stirng)//2
alpabet= alpabet.replace(" ", "")
count+=alpabet.__len__()
print(count)
x = input()
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro_al:
    x = x.replace(i, 'a')
print(len(x))