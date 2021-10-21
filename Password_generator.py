import string,random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_num = input("hwo many characters for password? ->  ")


while True:
    try:
        characters_num = int(characters_num)
        if characters_num < 6:
            print("you need at least 6 character")
            characters_num = input("please enter another num? ->  ")
        else:
            break
    except:
        print("please Enter the numbers only ")
        characters_num = input("please enter another num? ->  ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_num * (30/100))
part2 = round(characters_num * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
print(password)