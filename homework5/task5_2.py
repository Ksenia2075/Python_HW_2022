# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся
# в отдельных текстовых файлах.
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


with open('RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('RLE.txt', 'r') as file:
    text = file.readline()
    text_compression = text.split()

enconding = ''
prev_char = ''
count = 1
for char in text:
    if char != prev_char:
        if prev_char:
            enconding += str(count) + prev_char
        count = 1
        prev_char = char
    else:
        count += 1
else:
    enconding += str(count) + prev_char

print(text)
print(enconding)
with open('RLE3.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{enconding}')

input('Для востонавления текста нажмите Enter')

with open('RLE3.txt', 'r', encoding='utf_8') as file:
    text = file.read()

number = ''
text_return = ''
for i in text:
    if i.isdigit():
        number = number + i
    else:
        text_return += int(number) * i
        number = ''

print(f'Востановленный текст представляет последовательность:\n{text_return}')

with open('RLE.txt', 'w', encoding='utf_8') as file:
    file.write(text_return)


