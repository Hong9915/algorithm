S = str(input())

alpabet=[-1]*26

for i in range(len(S)):
    if S[i]=='a' and alpabet[0]==-1:
        alpabet[0]=i
    elif S[i]=='b' and alpabet[1]==-1:
        alpabet[1]=i
    elif S[i]=='c' and alpabet[2]==-1:
        alpabet[2]=i
    elif S[i]=='d' and alpabet[3]==-1:
        alpabet[3]=i
    elif S[i]=='e' and alpabet[4]==-1:
        alpabet[4]=i
    elif S[i]=='f' and alpabet[5]==-1:
        alpabet[5]=i
    elif S[i]=='g' and alpabet[6]==-1:
        alpabet[6]=i
    elif S[i]=='h' and alpabet[7]==-1:
        alpabet[7]=i
    elif S[i]=='i' and alpabet[8]==-1:
        alpabet[8]=i
    elif S[i]=='j' and alpabet[9]==-1:
        alpabet[9]=i
    elif S[i]=='k' and alpabet[10]==-1:
        alpabet[10]=i
    elif S[i]=='l' and alpabet[11]==-1:
        alpabet[11]=i
    elif S[i]=='m' and alpabet[12]==-1:
        alpabet[12]=i
    elif S[i]=='n' and alpabet[13]==-1:
        alpabet[13]=i
    elif S[i]=='o' and alpabet[14]==-1:
        alpabet[14]=i
    elif S[i]=='p' and alpabet[15]==-1:
        alpabet[15]=i
    elif S[i]=='q' and alpabet[16]==-1:
        alpabet[16]=i
    elif S[i]=='r' and alpabet[17]==-1:
        alpabet[17]=i
    elif S[i]=='s' and alpabet[18]==-1:
        alpabet[18]=i
    elif S[i]=='t' and alpabet[19]==-1:
        alpabet[19]=i
    elif S[i]=='u' and alpabet[20]==-1:
        alpabet[20]=i
    elif S[i]=='v' and alpabet[21]==-1:
        alpabet[21]=i
    elif S[i]=='w' and alpabet[22]==-1:
        alpabet[22]=i
    elif S[i]=='x' and alpabet[23]==-1:
        alpabet[23]=i
    elif S[i]=='y' and alpabet[24]==-1:
        alpabet[24]=i
    elif S[i]=='z' and alpabet[25]==-1:
        alpabet[25]=i


print(" ".join(map(str,alpabet)))