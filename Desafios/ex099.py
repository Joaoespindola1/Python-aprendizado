def maior(* num):
    c = mnum = 0
    for i in num:
        print(f'{i} ',end='')
        if c == 0:
            mnum = i
        if i > mnum:
            mnum = i
        c += 1
    print(f'\nForam informados {len(num)} valores')
    print(f'O maior valor é {mnum}')
    print('-='*20)

maior(5, 6, 7, 2, 3)
maior(5, 9, 10, 15, 7, 3, 21)
maior(3)
maior()