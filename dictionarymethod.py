student= {
    "name" : "Rahul Kumar",
    "subject" : {
        "phy" :97,# no duplicate in dictionary
        "chem":98,
        "math":95 
    }
}
print(student.keys())
print(list(student.keys()))#we can typecast to list
print(student.values())
print(student.items())
print(student.get("subject"))
student.update({"city":"delhi"})# newdic={"city":"delhi"} and update late
print(student)