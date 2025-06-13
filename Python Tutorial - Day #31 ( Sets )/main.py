
# []:-Square brackets, Used for lists, are ordered, mutable. They are also used for accessing elements within a sequence (indexing and slicing).
# ():-Parentheses, Used for tuples, are ordered, immutable. They also define the order of operations in expressions and are used when calling or defining functions.
# {}:- Curly brackets, Used for dictionaries and sets. Dictionaries store key-value pairs, while sets are unordered collections of unique elements.

# a = {1,2,6,4,3,5,4,2}
# print(a)
# print({100, 5, 1, 99, 7, 42})
# # Might print: {1, 100, 5, 99, 7, 42}

info = {"Boy",19,True,"Male",18.5}
# print(info)
for value in info: #Order is not maintained/fixed in sets
  print(value)

# boy = {} #dictionary
# boy = set() #set
# print(type(boy))
