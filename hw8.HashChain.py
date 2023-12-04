import random
import hashlib

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def H(k):
  kb = str.encode(k)  
  return hashlib.sha256(kb).hexdigest()

seed = random.getrandbits(256)
print("Original Seed:", seed)

length = int(input("Enter length: "))

head = Node(str(seed)) 
tail = head

for i in range(length-1):
  tail.next = Node(H(tail.value))
  tail = tail.next

current = head
while current:
  print(current.value)  
  current = current.next