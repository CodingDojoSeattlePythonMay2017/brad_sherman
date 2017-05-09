students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def names(val):
    for i in val:
        print (i['first_name'] + " " + i['last_name'])

names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],

 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def moreNames(users):
    for key, data in users.items():
        print (key)
        for index, value in enumerate(data):
            totalName = (value["first_name"] + " " + value["last_name"])
            totalNameLen = len(totalName) - 1
            print (f"{index + 1}" + " - " + f"{totalName}" + " - " + f"{totalNameLen}")

moreNames(users)
