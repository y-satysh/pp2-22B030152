#When you run a condition in an if statement, Python returns True or False:
print(bool("Hello"))
print(bool(15))

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#isinstance() function
x = 200
print(isinstance(x, int))