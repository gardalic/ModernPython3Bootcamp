# Try to get the "emojis" centered
# The bottom row is 11 emojis to center the odd numbers
# Advanced: get user input on how many 

bottom = 11 # If user input is added, replace with input + 1
exit_flag = 'n'
start = int(bottom / 2)

# for i in range(0, bottom):
for i in range(1, start + 2):
    chr_list = []

    for j in range(0, bottom):
        if j in range(start - (i - 1), start + i):
            emoji = "*"
        else:
            emoji = " "

        chr_list.append(emoji)

    if " " in chr_list or exit_flag == 'n':
        print(''.join(chr_list))

        if " " not in chr_list:
            exit_flag = 'y' # Exit flag assignment
    else:
        break
