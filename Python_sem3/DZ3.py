# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
#
things = {'палатка': 400, 'спальный мешок': 100, 'консерва': 50, 'нож': 50,
          'термос': 100, 'аптечка': 50, 'бутылка': 50, 'бинокль': 100, 'спички': 50,
          'ружье': 200, 'уголь': 100, 'ракетка': 100, 'одежда': 100, 'Велосипед': 2200}

weight_limit = 1100
temp_keys = []
temp_values = []
result = []
tools_keys = list(things.keys())
tools_values = list(things.values())

print(tools_keys)
print(tools_values)

for i in range(len(tools_keys)):
    if tools_values[i] <= weight_limit:
        temp_keys = []
        temp_values = []
        for j in range(i, len(tools_keys)):
            if sum(temp_values) + tools_values[j] <= weight_limit:
                temp_values.append(tools_values[j])
                temp_keys.append(tools_keys[j])
                print(temp_keys)