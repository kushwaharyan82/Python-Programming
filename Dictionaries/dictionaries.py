student = {
    "name": "Aryan",
    "age": 19,
    "course": "BTech AI/ML",
    "skills": ["Python", "SQL", "DSA"]
}

print("Student:", student)
print("Name:", student["name"])
print("Course:", student["course"])

student["age"] = 20
student["city"] = "Jaipur"

print("Updated student:", student)

print("Skills:")
for skill in student["skills"]:
    print("-", skill)
