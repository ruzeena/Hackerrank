'''s="Hacker"
n=len(s)
print (n)'''


class First:
    def __init__(self,input1):
      self.string = input1

    def value(self):
      n = len(self.string)
      l=[]
      for i in range(0,n-1,2):
        l.append(self.string[i])
      S="".join(str(x) for x in l)
      print (S)
      m=[]
      for i in range(1,n,2):
        m.append(self.string[i])
      S2="".join(str(x) for x in m)
      print (S2)
      S3=[]
      S3.append(S)
      S3.append(S2)
      print (S3)
      S4=" ".join(str(x) for x in S3)
      return (S4)


f1 = First("Hacker")
f2 = First("Rank")
print (f1.value())
print (f2.value())



