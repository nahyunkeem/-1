import random

user_choice=input("가위,바위,보중 하나를 선택하세요.")
print("당신의 선택은 ",user_choice,"입니다!")

choices=['가위','바위','보']
computer_choice=random.choice(choices)
print("컴퓨터의 선택은",computer_choice,"입니다!")

if user_choice == computer_choice:
    print("비겼습니다!")
elif (user_choice == "가위" and computer_choice == "보") or \
    (user_choice == "바위"and computer_choice == "가위") or (user_choice == "보" and computer_choice == "바위"):
    print("당신이 이겼습니다!")
else:
    print("당신이 졌습니다")