# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

print('Введите слово')
word = str(input()).upper()
onePoint = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
twoPoint = ['D', 'G' ,'Д', 'К', 'Л', 'М', 'П', 'У']
threePoint = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
fourPoint = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
fivePoint = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eightPoint = ['J', 'X', 'Ш', 'Э', 'Ю']
tenPoint = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

counter = 0
for i in range(len(word)):
    if str(word[i]) in onePoint:
        counter += 1
    if str(word[i]) in twoPoint:
        counter += 2
    if str(word[i]) in threePoint:
        counter += 3
    if str(word[i]) in fourPoint:
        counter += 4
    if str(word[i]) in fivePoint:
        counter += 5
    if str(word[i]) in eightPoint:
        counter += 8
    if str(word[i]) in tenPoint:
        counter += 10
print(counter)
