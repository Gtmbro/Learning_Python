class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  #__add__ method overloaded '+' operator.
  def __add__(self, other):
    return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(1,3,5)
v2 = Vector(2,4,8)

print(v1+v2)
print(type(v1)) #Type of v1 or v2
