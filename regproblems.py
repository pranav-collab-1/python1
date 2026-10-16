import re
##print("\\d") 
##print(r"\d")
##print(re.fullmatch(r"\d+", "Ro2out5"))
##
##text = "I am learning Python"
##m = re.search(r"Python", text)
##print(m.group() if m else "Not found")
##
##text = "abc 123 xyz 456"
##m = re.search(r"\d+", text)
##print(m.group())


print(r"\d")
print(r"\d{10}")
print(re.findall(r"\d+", "Ro2out5"))


text = "The box contains 12 red pens, 5 blue pens"
integers = [int(x) for x in re.findall(r"\d+", text)]
print(integers)

print(re.findall(r"\d+\.\d+", "Ro2out5.08"))

print(re.findall(r"\d+\@\D+", "student mail is 123@gmail.com"))


print(re.findall(r"\d+", "mobile number is 9100148528"))
print(re.findall(r"\d+", "mobile number"))
