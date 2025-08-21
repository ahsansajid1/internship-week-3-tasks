import json

student = [
    {"name" : "Ahsan", "age": 21, "marks": 88},
    {"name" : "Ali",  "age": 19,  "marks": 78},
    {"name" : 'Umair', "age": 18, "marks": 66}
]


with open ("student.json" , "w")as f:
    json.dump(student,f,indent=4)

print("Student Record Saved Succesfully ")

with open("student.json","r")as f:
    loaded_student = json.load(f)

print(" Student Records from File:")
for s in loaded_student:
    print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")