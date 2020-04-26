import shutil # modules that allows you to copy, move, rename, and delete files

# Copy and move files

shutil.copy('c:\\users\\Matt\\Desktop\\hello.txt', 'c:\\users\\Matt\\Desktop\\new') # copies a file to another location

shutil.copy('c:\\users\\Matt\\Desktop\\hello.txt', 'c:\\users\\Matt\\Desktop\\new\\poopdolla.txt') # copies a file to another location and renames the file

shutil.copytree('c:\\users\\Matt\\Desktop\\new', 'c:\\users\\Matt\\Desktop\\new\\new_backup') # copies entire folder contents to a new folder

shutil.move('c:\\users\\Matt\\Desktop\\hello.txt', 'c:\\users\\Matt\\Desktop\\new') # moves file from one location to another

shutil.move('c:\\users\\Matt\\Desktop\\new\\hello.txt', 'c:\\users\\Matt\\Desktop\\new\\heythere.txt') # to rename a file, move it to the same location but with a different name


# Deleting Files and Directories
import os
os.getcwd() # gets the current directory the program is running from
os.unlink('bacon.txt') # used to delete a file in the current directory

os.rmdir('c:\\users\\Matt\\Desktop\\new\\new_backup') # removes a directory. will only remove an empty directory

# Delete a folder and all of its content
import shutil
shutil.rmtree('c:\\users\\Matt\\Desktop\\new\\new_backup')

# Delete files with a specific extension
import os
os.chdir('c:\\users\\Matt\\Desktop') # changes the directory the program needs to work out of
for filename in os.listdir():
  if filename.endswith('.txt'):
    #os.unlink(filename) # comment this line and print the variable below it. run the program to make sure the filename variable grabs the files you expect. if it does, comment out the print and uncomment the unlink
    print(filename)


# Move files to recycle bin instead of permanently deleting
# this requires "send2trash" module to be installed via pip (pip install send2trash) via cmd line or pwsh
import send2trash
send2trash.send2trash('c:\\users\\Matt\\Desktop\\important.txt')

# Walking a Directory Tree
import os
for foldername, subfolders, filenames in os.walk('c:\\users\\Matt\\Desktop'): # walks this parent directory to find all folders, subfolders, and files. os.walk is used in for loops and returns 3 values
  print('The folder is ' + foldername)
  print('The subfolders in ' + foldername + ' are: ' + str(subfolders))
  print ('the files in ' + foldername + ' are: ' + str(filenames))
  print()

# example on how to use the values from os.walk to make mass changes on files and folders
  for subfolder in subfolders: 
    if 'fish' in subfolder:
      os.rmdir(subfolder)

  for file in filenames:
    if file.endswith('.txt'):
      shutil.copy(os.join(foldername, file), os.join(foldername, file + '.backup'))