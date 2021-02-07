# Dictionaries assignment 2 of Day 2

dict= {"Name": "Ubaid", "Age": 25, "profession": "Student", "location": "Navi Mumbai"}


x= dict.get("Name")
print(x)

dict.popitem()
print(dict)

dict.copy()
print(dict)

x = dict.setdefault("JOB", "Developer")
print(x)

dict.update({"hobby" : 'Reading'})
print(dict)