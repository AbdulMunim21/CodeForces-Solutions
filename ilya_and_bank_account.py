bank_state = input()
bank_state_int = int(bank_state)

if int(bank_state[0: len(bank_state) - 2] + bank_state[-1]) > bank_state_int:
    if int(bank_state[0: len(bank_state) - 2] + bank_state[-1]) < int(bank_state[0: len(bank_state) - 1]):
        print(int(bank_state[0: len(bank_state) - 1]))
    else:
        print(int(bank_state[0: len(bank_state) - 2] + bank_state[-1]))
elif int(bank_state[0: len(bank_state) - 1]) > bank_state_int:
    if int(bank_state[0: len(bank_state) - 1]) <int(bank_state[0: len(bank_state) - 2] + bank_state[-1]) :
        print(int(bank_state[0: len(bank_state) - 2] + bank_state[-1]))
    else:
        print(int(bank_state[0: len(bank_state) - 1]))
else:
    print(bank_state_int)