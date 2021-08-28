def solution(number):
    a = 0
    if number <= 0:
        return 0
    else:
        for num in list(range(1, number)):

            if num % 3 == 0:
                a += num
            if num % 5 == 0:
                a += num
            # some shit code? but it helps
            if num % 3 == 0 and num % 5 == 0:
                a -= num

        print(a)
        print(list(range(1, number)))


solution(200)
