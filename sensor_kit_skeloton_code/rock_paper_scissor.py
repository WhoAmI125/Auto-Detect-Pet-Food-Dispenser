import random

def addup(value):
	
	if value < 0:
		print("인류의 멸망")

random_array = ["가위", "바위", "보"]
tries = 0

while(1):
	if tries == 3:
		break
	computer_hand = random.choice(random_array)
	
	human_hand = input("가위바위보 : ")

	while(human_hand not in random_array):
		human_hand = input("가위바위보 : ")

	print("당신의 선택은\n" + human_hand)

	print("컴퓨터의 선택은! : " + computer_hand)

	result = 0

	if(human_hand == "가위"):
		if(computer_hand == "바위"):
			result -= 1
		elif(computer_hand == "보"):
			result += 1
		else:
			result += 0
	elif(human_hand == "바위"):
		if(computer_hand == "보"):
			result -= 1
		elif(computer_hand == "가위"):
			result += 1
		else:
			result += 0
	elif(human_hand == "가위"):
		if(computer_hand == "보"):
			result -= 1
		elif(computer_hand == "바위"):
			result += 1
		else:
			result += 0
	tries += 1
	

addup(tries)
