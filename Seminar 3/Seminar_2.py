import time

x = time.time()
print((x))
# Получаем число типа int - наносекунды от 01.01.1970
x = time.time_ns()
print(x)

time.sleep(2.5)