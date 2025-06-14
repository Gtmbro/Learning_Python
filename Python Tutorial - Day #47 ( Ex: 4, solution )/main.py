import random
import string



def code(words):
  encoded = []
  for word in words:
    if len(word)>=3:
  #Random characters:-
      r1 = ''.join(random.choices(string.ascii_lowercase,k=3))
      r2 = ''.join(random.choices(string.ascii_lowercase,k=3))
      new = r1 + word[1:] + word[0] + r2
      encoded.append(new)
    else:
      encoded.append(word[::-1])
  return(' '.join(encoded))

def decode(words):
  decoded = []
  for word in words:
    if len(word)>=9:
      pre = word[3:-3]
      new = pre[-1] + pre[:-1]
      decoded.append(new)
    else:
      decoded.append(word[::-1])
  return(' '.join(decoded))


Decision = int(input("Enter 1 for encoding and 2 for decoding:\n "))
coding = True if Decision == 1 else False

text = input("Enter your string:\n")
# words = text.split(' ')


if (coding):
  result = code(text.split())
  print("Encoded: ",result)
  
else:
  result = decode(text.split())
  print("Decoded: ",result)
  
  

