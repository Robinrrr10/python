num = 12

if num < 10:
    print(num, " is less than 10")
elif num == 10:
    print(num, " is equal to 10")
else:
    print(num, " is greater than 10")

count = 1
while count<=10:
    print(count)
    count+=1

val = 1
while val <= 5:
    print(val)
    if val ==3:
        break;
    val += 1

ss = 0
while ss <= 5:
    ss += 1
    if ss ==3:
        continue
    print(ss)

val2 = 1
while val2 <= 5:
    print(val2)
    if val2 ==10:
        break;
    val2 += 1
else:
    print("No value of 10")

nu = [78, 21, 12, 91, 34, 67]
for i in nu:
    print("Each value is:", i)

print("Length is: ", len(nu))

for i in range(len(nu)):
    print("index ", i, " value is:", nu[i])

for k in range(10):
    print("k is:", k)

for kk in range(12, 15):
    print("kk is: ", kk)

allval = {"name": "Ram", "mark": 34, "major": True}

for kee in allval:
    print(kee)

for key, val in allval.items():
    print(key,":", val)

