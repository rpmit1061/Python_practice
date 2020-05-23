coordinates = (1,2,3)
x,y,z = coordinates #Unpacking

#Dictionary in python
contact = {"name":"Jon smith",
           "Email":"jonsmith@gmail.com",
           "Phone":76985854585
           }
phone = input("Phone: ")
digits_maping = {
    "1":"one",
    "2":"Two",
    "3": "Three",
    "4":"Four"
}
output = ""
for ch in phone:
    output += digits_maping.get(ch, "!") + " "
print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(":"😢"
}
outputs = ""
for word in words:
    outputs += emojis.get(word,word) + " "
print(outputs)