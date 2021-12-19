# Poo-po_tz
def write(self, array, name):
    my_file = open(name, "w")
    for i in array:
        my_file.write(str(i) + " ")
    my_file.close()


s = [7, 678, 6050, 3, 0.1, 700]
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
