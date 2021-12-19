# my_file = open("TZ.txt", "w+")
# my_file.write()
# my_file.close()
# print(my_file)


def write(self, array, name):
    my_file = open(name, "w")
    for i in array:
        my_file.write(str(i) + " ")
    my_file.close()


s = [7, 678, 6050, 3, 0.1, 700]
# while True:
#     print("Введите числа для списка")
#     text = input()
#     s.append(text)
#     if not text:
#         break
#
# s.remove('')
print(s)

mini = s[0]
for i in range(len(s)):
    if mini >= s[i]:
        mini = s[i]
print("Наименьшее значение:", mini)

maxi = s[0]
for i in range(len(s)):
    if maxi <= s[i]:
        maxi = s[i]
print("Наибольшее значение:", maxi)


result = 0
for x in s:
    result = result + x
print("Сумма списка:", result)

product = 1
for y in s:
    product *= y
print("Произведение списка:", product)

#sorted_s = sorted(s)
#result = sorted_s[0]
#print(sorted_s)
#print("Наименьшее значение:", result)
