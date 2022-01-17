estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(propIn, listIn):
  for ele in listIn:
    print(ele[propIn])

iterateDictionary2("first_name", estudiantes)
iterateDictionary2("last_name", estudiantes)