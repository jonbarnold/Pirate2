

print("arr,matey")
#looks like my change got reverted-
# Have pirate.py write a file
with open('map.txt', 'w') as fh:
  for i in range(10):
    fh.write("Walk " + str(i) + " paces left.")
