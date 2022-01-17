dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictIn):
  for prop in dictIn:
    print(f"{len(dictIn[prop])} {prop.upper()}")
    for ele in dictIn[prop]:
      print(ele)
    print("--------")

printInfo(dojo)