print("reformat number")
num=input("Enter number: ")
x = ""
y = ""
a = 0

for i in num:
    if i.isdigit() :
        x += i

for i in x:
    a += 1
    if a % 3 == 0 and a != len(x) :
        i += "-"
    y += i

if y[-2] == "-":
    y = y[:-2]  + y[-1]
    y = y[:-2] + "-" + y[-2] + y[-1]

print(y)
print("jumlah strip for number")
strip = 0
for character in y:
    if (character in "-"):
        strip += 1
print("strip:", strip)









