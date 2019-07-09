import os

# 1. dummy 폴더로 들어간다.
os.chdir('./dummy')
print(os.getcwd())

# 2. 하나하나씩 파일명을 변경한다. -> 반복문

files = os.listdir('.')
for i in range(0,501):
   print(files[i])
#print(type(files))
#for file in files:
#    os.rename(file, f'SAMSUNG_{file}')
#for file in files:
#    os.rename(file,file.replace('SAMSUNG','SAFFY'))