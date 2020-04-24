import os
totalSize = 0
for filename in os.listdir('d:\\projects\\python') :  # uses os.listdir to list files and folders in the directory
  if not os.path.isfile(os.path.join('d:\\projects\\python', filename)) :
    continue
  totalSize = totalSize + os.path.getsize(os.path.join('d:\\projects\\python', filename))
print (totalSize / 1024)