def check_password(password):
    password1 = input()
    if password == password1:

        def fibonachy(a):
            x = 1
            y = 1
            while x <= a:
                print(x)
                z = x + y
                x = y
                y = z

        n = int(input())
        fibonachy(n)
    else:
        print('None')
        print('В доступе отказано')


password = input()
check_password(password)
