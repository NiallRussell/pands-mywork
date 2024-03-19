# Write a program that will read in the data for the data structure above, ie reads in a student’s name, 
#then keeps reading in their modules and grades(until the user enters a blank module name), You can break this up into two parts:
#a. Just read in the module names until the user enters blank, b. Then read in the grade as well
#b. This program can just read in one student (and their module details).
#6. If you want to go a step further, read in multiple students (until the student_name is blank. 

students = [{
    "name":"Mary", 
           "courses": [
               {
                    "course_name":"Programming",
                    "grade":45    
               },
               {
                   "course_name":"History",
                   "grade":99
               }
           ]
},           {
    "name": "John",
            "courses":[
               {
                    "course_name":"Analytics",
                    "grade":55    
               },
               {
                   "course_name":"Psychology",
                   "grade":76
               }
           ]}
]


for student in students:
    #for course in student["courses"]:
        print ("{}".format(student["name"]))

print (students["name"])
for student in students:
        for course in student["courses"]:
                print ("{}:\t{}:\t{}".format(student["name"], course["course_name"], course["grade"]))



name = input("Enter the students name: ")
modules = []
student = {}
student["name"] = name
courseName = str(input("Enter the name of the module: "))
while courseName != "":
    module = {}
    module["courseName"] = courseName
    module["grade"] = int(input("Enter the grade for {}: ".format(courseName)))
    modules.append(module)
    student["modules"] = modules
    module = {}
    courseName = input("Enter the name of the module: ")
print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t{} \t: {}".format(module["courseName"], module["grade"]))