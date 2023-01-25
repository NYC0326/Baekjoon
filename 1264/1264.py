vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    string = input()
    if string == '#':
        break
    else:
        cnt = 0
        for alphabet in string:
            if alphabet.lower() in vowel:
                cnt+=1
        print(cnt)