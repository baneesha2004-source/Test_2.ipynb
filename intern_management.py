# intern_management.py

for i in range(2):
    print(i+1)

student_dict={}
student_dict['name']=input("Enter your name: ")
student_dict['cgpa']=float(input("Enter your cgpa: "))
student_dict['location']=str(input("Enter your location: "))
print(student_dict)

projects=[]
proj1=input("Enter your project name: ")
proj2=input("Enter your project name: ")

projects.append(proj1)
projects.append(proj2)
#projects.extend([proj1,proj2])
print(projects)
student_dict['projects']=projects

skills=set(input("enter skills separated by space:").split())
print(skills)

student_dict['skills']=skills
student_dict["roll no"]=12345