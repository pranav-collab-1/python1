text=input("Enter the Text:")
shifted =""
for ch in text:
    shifted += chr((ord(ch)+1))
print("Shifted string:",shifted)
