students= []
def read_modules():
 return []
def do_add(students):
 currentStudent = {}
 currentStudent["name"]=input("enter name :")
 currentStudent["modules"]= read_modules()
 students.append(currentStudent)
#test
do_add(students)
do_add(students)
print (students)
