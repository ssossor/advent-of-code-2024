import re

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
regex = r"mul\([0-9]+,[0-9]+\)"

file = open("input_3.txt", "r").read()

my_list=re.findall(regex, file)

result = 0

for i in my_list:
    tmp = i[4:-1].split(",")
    result += int(tmp[0]) * int(tmp[1])

print(result)

test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

test = file

regex_do = r"do\(\)"
regex_dont = r"don't\(\)"

comp_mul = re.compile(regex)
it_mul = comp_mul.finditer(test)
list_mul = list(it_mul)

comp_do = re.compile(regex_do)
it_do = comp_do.finditer(test)
list_do = list(it_do)

comp_dont = re.compile(regex_dont)
it_dont = comp_dont.finditer(test)
list_dont = list(it_dont)

enabled = True
result = 0

while list_mul != []:
    if list_do == [] or list_dont == []:
        if list_do == [] and list_dont == []:
            if enabled:
                tmp = list_mul[0].group()[4:-1].split(",")
                result += int(tmp[0]) * int(tmp[1])
            list_mul.pop(0)
        elif list_do == []:
            if list_mul[0].span()[0] < list_dont[0].span()[0]:
                if enabled:
                    tmp = list_mul[0].group()[4:-1].split(",")
                    result += int(tmp[0]) * int(tmp[1])
                list_mul.pop(0)
            else:
                enabled = False
                list_dont.pop(0)
        elif list_dont == []:
            if list_mul[0].span()[0] < list_do[0].span()[0]:
                if enabled:
                    tmp = list_mul[0].group()[4:-1].split(",")
                    result += int(tmp[0]) * int(tmp[1])
                list_mul.pop(0)
            else:  
                enabled = True
                list_do.pop(0)

    elif list_mul[0].span()[0] < list_do[0].span()[0] and list_mul[0].span()[0] < list_dont[0].span()[0]:
        if enabled:
            tmp = list_mul[0].group()[4:-1].split(",")
            result += int(tmp[0]) * int(tmp[1])
        list_mul.pop(0)
    elif list_do[0].span()[0] < list_dont[0].span()[0]:
        enabled = True
        list_do.pop(0)
    else:
        enabled = False
        list_dont.pop(0)
    
print(result)

