def yoo():
  try:
    a = [2,4,6,8]
    i = int(input("Enter the index: "))
    return (f"{a[i]} is what you needed?")
     
  except:
    return("Some error occured!")
     
  finally:
    print("I am always executed..")
  # print("yooo")
  
x = yoo()
print(x)
