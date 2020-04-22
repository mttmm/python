print ('How many cats do you own?')
numCats = input()
if int(numCats) >=0:
  try:
    if int(numCats) >= 4:
      print ('That is a lot of cats')
    else:
      print ('That is not that many cats')
  except ValueError:
    print('You did not enter a number')
else:
  print ('It is not possible to have negative cats, is it?')