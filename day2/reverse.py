# numbers.txt를 읽어서
with open('numbers.txt','r') as f:
    num = f.readlines()

print(type(num))
print(num)

# 리스트를 뒤집는다.
num.reverse()

# numbers_reverse.txt로 저장!!
with open('numbers_reverse.txt','w') as f:
    for input in num:
        f.write(input)