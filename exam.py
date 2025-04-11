res = list()
sta = 1
end = 10
num = 4
test_list = list(range(100))

for mx in range(100):
    sta = test_list[mx]
    if not sta % 16:
        end += test_list[sta]
        break
    end += 1

low = (end - sta) // num
for x in range(num - 1):
    res.append([sta + x * low, sta + (x + 1) * low])
    res.append([sta + (x + 1) * low, end])

print(res[-1])