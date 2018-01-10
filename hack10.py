string_entries=int(input())
for i in range(string_entries):
    word=input().strip().split(" ")
    print(word)
length=len(word)
def even():
  for c in range(0,length):
    s=word[c]

    leng=len(s)
    l=[]
    for i in range(0,leng-1,2):
      n=s[i]
      l.append(n)

    S = " ".join(str(x) for x in l)
    print (S)
    c=c+1
def odd():
    for c in range(0, length):
        s = word[c]

        leng = len(s)
        l = []
        for i in range(1, leng, 2):
            n = s[i]
            l.append(n)

        S = " ".join(str(x) for x in l)
        print(S)
        c = c + 1

print (even())
print (odd())



