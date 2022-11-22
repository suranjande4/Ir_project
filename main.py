import re
import string
from collections import defaultdict
import pickle


def code(x):
      dict = {'a': 123,
              'b': 312,
              'c': 1,
              'd': 123,
              'e': 1,
              'f': 5,
              'g': 120,
              'h': 392,
              'i': 3,
              'j': 0,
              'k': 31,
              'l': 3,
              'm': 9292,
              'n': 92,
              'o': 12,
              'p': 412,
              'q': 124,
              'r': 9,
              's': 7,
              't': 5,
              'u': 33,
              'v': 33,
              'w': 333,
              'x': 21,
              'y': 120,
              'z': 8}

      result = ""
      x=x.replace("\n","")
      for i in x:
            result = result + str(dict[i])
      result = result.replace("13", "123")
      result = result.replace("32", "312")
      return result
#dexin axin


with open('ListMeds.txt') as f:
    medicines = f.read()

medicines = re.sub(r'[\(\[].*[\)\]]', '', medicines).lower()
valid_letters = string.ascii_letters + '\n'
medicines = ''.join([x for x in medicines if x in valid_letters])


with open('ListMeds_cleaned.txt', 'w') as f:
    f.write(medicines)

f.close()
hashed=defaultdict(set)
f1=open('ListMeds.txt')
for m,line in zip(medicines.split('\n'),f1):
    line=line.replace("\n","")
    hashed[code(m)].add(line)
hashed=dict(hashed)
pp=sorted(hashed)
pp=set(pp)



with open('test.txt','wb') as handle:
    pickle.dump(hashed,handle)



with open('test.txt','rb') as f3:
    b=pickle.loads(f3.read())


inp=input("Enter Text:- ")
h=code(inp)
a=str(b.get(h))
if a=='None':
    print(h + 'No Match Found')
else:
    print(h,a)



