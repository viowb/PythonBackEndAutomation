import json
#covert json into dictionary and extract the data
json_string = '{"account name": "Jones", "age": 25,  "gender": "female", "is_admin": true, "languages": ["Java", "JS", "Python"]}'

#json.loads mthd parse json string, returns it as dictionary
string_data = json.loads(json_string)
print(string_data)
print(type(string_data))

#from the dictionary, extract account name, age, gender, admin
print(string_data["account name"])
print(string_data["age"])
print(string_data["gender"])
print(string_data["is_admin"])

print(string_data["languages"])
#print second language on the list
print(string_data["languages"][0])
print(string_data["languages"][1])
print(string_data["languages"][2])


#*********************************************************************

#parse content in json file into dictionary
#open file and read
with open("C:\\Users\\viowb\\PycharmProjects\\company.json") as f:
#json.load(f)
    data = json.load(f)
    print(data)
#print itt as dictionary
    print(type(data))
#extract the data get company name, username, address and role
    print(data["company"])
    print(data["user"]["name"])
    print(data["user"]["age"])
    print(data["user"]["email"])
    print(data["user"]["address"])
    print(data["user"]["address"]["zip"])
    print(data["user"]["address"]["zip"][3])
    #assert (data["user"]["address"]["zip"][3]) == 4
    print(data["roles"][0])
    print(data["roles"][1])

#*************************************************************************

 #compare 2 json schemas

with open("C:\\Users\\viowb\\PycharmProjects\\company.json") as f:
#json.load(f)
    data2 = json.load(f)
    print(data == data2)