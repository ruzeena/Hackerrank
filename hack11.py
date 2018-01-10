input_string=input("Enter String")
length=len(input_string)

odd_list=[]
for i in range(0,length,2):
    odd_list.append(input_string[i])

odd_result = "".join(str(x) for x in odd_list)
even_list=[]
for i in range(1,length,2):
    even_list.append(input_string[i])

even_result = "".join(str(x) for x in even_list)

New_string=[]
New_string.append(odd_result)
New_string.append(even_result)
Final_result= " ".join(str(x) for x in New_string)
print(Final_result)


