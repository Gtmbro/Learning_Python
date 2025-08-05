class Cart:
  def __init__(self, user_name, user_surname, item_list):
    self._user_name = user_name
    self._user_surname = user_surname
    self.item_list = item_list.copy()

  def __call__(self):
    print (f"Cart list of {self._user_name} {self._user_surname}:-")

  def __str__(self):
    result = []
    for rank, item in enumerate(self.item_list, start=1):
      result.append(f"{rank}. {item}")
    return "\n".join(result) #To return a single string for printing..

  def __len__(self):
    return (len(self.item_list))

  def __setitem__(self, index, item):
    if isinstance(index, int) and 0 <= index < len(self.item_list):
      self.item_list[index] = item
    else:
      raise IndexError("Invalid index in __setitem__")
    
  def __getitem__(self, index):
    return self.item_list[index]

  def __eq__(self, other):
    return self._user_name == other._user_surname

# --- Testing ---
user1 = Cart("John", "Smith", ["Mango", "Apple", "Banana"])
user2 = Cart("Will", "Hacck", ["Papaya", "Orange", "Strawberry"])
user1()  

print(str(user1))

print(len(user1))  

user1[1] = "Orange"
print(user1[1])  

print()

user2() 

print(str(user2))

print(len(user2))  

user2[1] = "Orange"
print(user2[2])  

print()
print(f"Both users are same..\n{user1 == user2}") 
