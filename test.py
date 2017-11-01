from streamlib import F2
cm = F2() # create a instance of CountMin, see document for more detail
cm.processBatch([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4])
for i in range(5):
   print('Estimated frequency of', i, 'is', cm.estimate())

