'''Use ctrl+/ to comment out selected lines'''

boys = 'Amrit,Prashanna,Bishesh,Amit'
print(len(boys))
print(boys[6:15])  #Explanation: boys[index of 1st letter(6):position after last letter(14+1=15)]

girl = 'Ichchhya'
print(len(girl))
print(girl[:-5])  #girl[from index 0 to before index len(girl)-5=index 2]
print(girl[-3:8]) #girl[from index len(girl)-3 to before index 8=7 ]
print(girl[-3:-1]) #girl[from index len(girl)-3 to before index len(girl)-1=7 ]
