import simplejson as json
import os

if os.path.isfile("./age.json") and os.stat("./age.json").st_size != 0:
    old_file = open("./age.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"])
    data["age"] = data["age"] + 1
    print("new age is ", data["age"])
else:
    old_file = open("./age.json", "w+")
    data = {"name": "Rahul", "age": 27}
    print("Current age is",  data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))