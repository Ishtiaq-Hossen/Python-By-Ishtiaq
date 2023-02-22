

'''

=====================================
    :(        :(          :(
=====pyhton dictionary concepts======>>> by Ishtiaq 
    :(        :(          :(    
=====================================
'''

#====first we will declaring the dictionary====
student={'name':"Ishtiaq",'age':29,'situation':['valo','kharap']}

'''
here name,age,situation are keys
and Ishtiaq,29,valo are a values

'''
#===we can see data type by using type(variable_name) function===
print("data type name:",type(student))

#====individuals key's value showing ===/
print(student['situation'])
print(student['name'])
#===student dictionary keys, values & items showing====/

print("keys are: ",student.keys())
print("values are: ",student.values())
print("items are: ",student.items())

#=====showing student======/

print(student)


#====dictionary updating======/
student.update({'name':"Arman",'age':20,'Phone':'+880100000'})
print(student)

#====poping/deleting a key and storing it's value in another variable
'''
# popping & storing 
age=student.pop('age')
print(age)
'''


#only deleting
del student['age']
print(student)

'''
#only popping
student.pop('age')
'''
#====searching a key ,if it's not found it will show "not found"===
print(student.get('name',"not found"))
print(student)

#====showing how many key's in the dictionary=
print(len(student))

#====showing key & value line by line==
for key,value in student.items():
    print(key,value)



