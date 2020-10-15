def frequency(l):
  check = []
  fD = {}
  minF = 0
  maxF = 0
  for i in range(len(l)):
    count = 0
    if l[i] not in check:
      check.append(l[i])
      for j in range(i+1,len(l)):
        if l[j] == l[i]:
          count+=1
      fD[l[i]] = count
      if i ==0:
        minF = count
        maxF = count
      elif count < minF:
        minF = count
      elif count > minF:
        maxF = count
  min = []
  max = []
  for f in fD:
    if fD[f] == minF:
      min.append(f)
    if fD[f] == maxF:
      max.append(f)
  output = (sorted(min), sorted(max))
  return(output)
