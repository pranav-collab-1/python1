a = input("Enter the string: ")
dic = {}

for ch in a:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1

for ch, count in dic.items():
    print(f"{ch} -> {count}")
