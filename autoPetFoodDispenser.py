import time
from datetime import datetime
import sys, os, cv2
from tflite_support.task import core, vision
from grove.grove_servo import GroveServo

def moveServo(servo):
	servo.setAngle(179)
	time.sleep(5)
	servo.setAngle(1)
	time.sleep(3)
		

count = 0
servo = GroveServo(18)
# text표현관련 parameters
_TEXT_COLOR = (255, 255, 255)
_FONT_ = cv2.FONT_HERSHEY_PLAIN
_FONT_SIZE = 1
_FONT_THICKNESS = 1

# classyfi() 모델, 분류목록, 분류할 이미지를 입력하면 가장 가능성있는 분류명, 가능성를 리턴
def classify(model, labels, image): # -> (label, probability)
    
    # classifier에 사용할 모델 설정
    classifier_options = vision.ImageClassifierOptions(
        base_options=core.BaseOptions(file_name=model))
    classifier = vision.ImageClassifier.create_from_options(classifier_options)
    
    # 텐서플로우 이미지로 변환
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    tensor_image = vision.TensorImage.create_from_array(rgb_image)
    
    # 분류 실행
    result = classifier.classify(tensor_image)
    
    # 결과 정리
    category = result.classifications[0].categories[0]
    category_name = labels[category.index]
    probability = round(category.score, 2)
    
    return (category_name, probability)

def main():
	
	checkFoodGive = 0

	# 모델파일 지정
	model = './model/model.tflite'
	# 레이블 파일을 읽어 리스트로
	f = open('./model/labels.txt', 'r')
	labels = f.readlines()
	f.close()

	# 비디오 캡쳐 시작
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224) # 가로 224px
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224) # 세로 224px
   

	while cap.isOpened():
		success, image = cap.read()
		
		# 캡쳐 오류시 프로그램 종료
		if not success: 
			sys.exit('ERROR: Please verify your webcam settings.')
		# 이미 좌우 반전
		image = cv2.flip(image, 1)

		# image로 분류 실행
		prediction = classify(model, labels, image)
		
		report_text = prediction[0]+str(prediction[1]*100)+'%'
		
		# text 배치
		cv2.putText(image, report_text, (10,20), _FONT_,
				  _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)
		# 이미지 표시하기
		cv2.imshow('rock-scissors-paper', image)

		# ESC 키가 눌리면 루프 종료
		if cv2.waitKey(1) == 27:
			break
	
		currentTime = datetime.now()
		print(currentTime.hour)
		#lunctime
		if currentTime.hour >= 14 and currentTime.hour <= 16:
			print(prediction[0])
			if checkFoodGive == 1:
				continue
				
			elif prediction[0] == labels[0]:
				dogProb = prediction[1] * 100
				if dogProb > 95:
					print(count)
					if count > 3:
						print("dog detected for 5 seconds")
						moveServo(servo)
						checkFoodGive = 1
					count += 1
					#time.sleep(1)
			else:
				count = 0
			#setting while loop to second


	cap.release() # 영상 캡쳐 중지
	cv2.destroyAllWindows() # 윈도우 닫기

if __name__=='__main__':
    main()
