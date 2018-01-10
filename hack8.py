a = int(input())

var1 = [arr_temp for arr_temp in input()]

var2 = [arr_temp for arr_temp in input()]
n = len(var1)
l = []
for i in range(0, n - 1, 2):
  l.append(var1[i])
S = "".join(str(x) for x in l)


m = []
for i in range(1, n, 2):
  m.append(var1[i])
S2 = "".join(str(x) for x in m)


S3 = []
S3.append(S)
S3.append(S2)


S4 = " ".join(str(x) for x in S3)
print (S4)
n = len(var2)
l = []
for i in range(0, n - 1, 2):
  l.append(var2[i])
S = "".join(str(x) for x in l)

m = []
for i in range(1, n, 2):
  m.append(var2[i])
S2 = "".join(str(x) for x in m)

S3 = []
S3.append(S)
S3.append(S2)

S4 = " ".join(str(x) for x in S3)
print (S4)





