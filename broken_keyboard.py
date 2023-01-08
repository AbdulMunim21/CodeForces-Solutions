test_cases = eval(input())
word_ok = True
output_list = []
words_list = []

for i in range(test_cases):
    length = int(input())
    word = input()
    print('YES' if length % 3 != 2 and not False in [word[i * 3 + 1] == word[i * 3 + 2] for i in range(length // 3)] else 'NO')

    # else:
    #     try:
    #         for i in range(1, length, 2):
    #             if word[i] != word[i+1]:
    #                 output_list.append("NO")
    #                 word_ok = False
    #                 break

    #         if word_ok:
    #             output_list.append("YES")

    #     except Exception as err:
    #         print(err)
    #         output_list.append("NO")

