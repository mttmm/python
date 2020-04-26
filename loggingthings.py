import logging
logging.basicConfig (filename='c:\\users\\Matt\\Desktop\\errors\\debug.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # disables all logging at the critical level or lower. Critical is the highest level, so this will disable all logging. comment this out to re-enable logging to debug

logging.debug('Start of program')
def factorial(n):
  logging.debug('Start of factorial (%s)' % (n))
  total = 1
  for i in range (1, n + 1):
    total *=i
    logging.debug(' i is %s, total is %s' % (i, total))

  logging.debug(' Return value is %s' % (total))
  return total

print (factorial(5))

logging.debug('End of program')