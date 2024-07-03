import random

answer_number=random.randint(1,100)

guess=int(input("1-100사이의 숫자를 입력하세요."))
print(guess)

if answer_number == guess:
    print("정답입니다!")
elif answer_number < guess:
    print("DOWN"),
elif answer_number > guess:
    print("UP")


count=0

count=count+1
print(f"{count}번째 시도입니다.")