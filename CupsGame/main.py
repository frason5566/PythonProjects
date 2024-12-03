from random import shuffle

cups = ['R', 'B', 'O', 'Y', 'G']

shuffle(cups)

info = '''--Five Cups Game--
Red, Blue, Orange, Yellow, Green
Five cups in a row
Guess the order of those
Answer in R, B, O, Y and G
eg. OGYBR
Have Fun'''
print(info)
cnt = 1
correct = 0
good_ans = True
while correct != 5:
    correct = 0
    good_ans = True
    ans = input('\nGuess: ')
    if len(ans) == 1 and ans.lower() == 'q':
        print(f'The answer is {cups}')
        break
    elif len(ans) != 5:
        print('answer is not in length 5')
    else:
        ans = ans.upper()
        for i in range(5):
            if ans[i] not in cups:
                print(f'{ans[i]} is not a valid color')
                good_ans = False
                break
            else:
                if ans[i] == cups[i]:
                    correct += 1
        if good_ans and correct == 5:
            print(f'You made it with {cnt} guess! Congrat!')
        elif good_ans and correct != 5:
            print(f'{correct} with right color , give another try')
            cnt += 1
        elif not good_ans:
            print(f'Give another try')
