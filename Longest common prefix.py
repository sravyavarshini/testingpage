strs=["flow","flower","flight"]
min=len(strs[0]);s="";c=0;ms=strs[0]
for i in strs:
  if len(i)<min:
    min=len(i)
    ms=i
k=0
for i in ms:
  c=0
  for j in strs:
    if i!=j[k]:
      break
    c=c+1
    if c==len(strs):
      s=s+i
    else:
      break
    k=k+1
print(s)
