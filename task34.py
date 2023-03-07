phrases = [i.replace('-','') for i in (input('Введите фразу: ').split())]

count_of_syllables = []

for phrase in phrases:
    count = 0
    for letter in phrase:
        if letter in 'уеаоэяиюё':
            count += 1
    count_of_syllables.append(count)

flag = True
for i in range(len(count_of_syllables) - 1):
    if count_of_syllables[i] != count_of_syllables[i + 1]:
        flag = False

if flag:
    print('Парам пам-пам')
else:
    print('Пам парам')
            