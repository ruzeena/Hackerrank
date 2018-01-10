n = int(input().strip())
if n in range(2,21):
  for i in range(1, 11):
    print (n,"*",i,"=",n*i)
    i = i + 1

