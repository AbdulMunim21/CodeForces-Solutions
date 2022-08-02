test_cases = eval(input())
answers = []

for i in range(test_cases):
    difference = []
    first_line = input()
    first_line = first_line.split(" ")
    n = int(first_line[0])
    H = int(first_line[1])
    M = int(first_line[2])
    for i in range(n):
        line = input()
        line = line.split(" ")
        h = int(line[0])
        m = int(line[1])
        if h == H and m == M:
            difference.append("0 0")
        else:
            if M < m and H < h:
                minutes = m - M
                hours = h - H - 1
                difference.append(str(hours) + " " + str(minutes))
            elif M < m and H > h:
                minutes = m - M
                hours = 24 - H + h
                difference.append(str(hours) + " " + str(minutes))
            elif M > m and H < h:
                minutes = 60 - M + m
                hours = h - H - 1
                difference.append(str(hours) + " " + str(minutes))
            elif M > m and H > h:
                minutes = 60 - M + m
                if len(str(minutes)) == 1:
                    hours = 24 - H + h
                else:
                    hours = 24 - H + h - 1
                difference.append(str(hours) + " " + str(minutes))
    difference.sort()
    answers.append(difference[0])


for val in answers:
    print(val)
