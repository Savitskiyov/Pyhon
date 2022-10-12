import re

input_str = '+ 95x^10 + 98x^9 + 82x^8 + 34x^7 + 78x^6 + 45x^5 + 2x^4 + 60x^3 + 44x^2 + 34x + 77 = 0'

pattern1 = r'([-+] \d*)(x\^*\d*)'

res1 = re.search(pattern1, input_str)
print(res1)
print(res1.groups())

res2 = re.match(pattern1, input_str)
print(res2)
print(res2.groups())

compile_pattern1 = re.compile(pattern1)
res3 = compile_pattern1.match(input_str)
print(res3)
print(res3.groups())

res4 = compile_pattern1.findall(input_str)
print(res4)

pattern2 = r'([-+] \d*)(x\^*\d*)|([-+] \d*).='
compile_pattern2 = re.compile(pattern2)
res5 = compile_pattern2.findall(input_str)
print(res5)

