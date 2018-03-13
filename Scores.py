#Задание 1
print('Задание 1')
age=int(input('Введите ваш возраст:'))
if age<6:
	print('Вам нужно бы походить еще в садик')
elif age<17:
	print('Вам самое время поучиться в школе')
elif age<23:
	print('Вам пора получить высшее образование')
elif age<55:
	print('Вам пора на работу')
else:
	print('Пора готовиться к пенсии')



#Задание 2
print('Задание 2')

def two_strokes():
	first_stroke=input('Введите 1-ую строку')
	second_stroke=input('Введите 2-ую строку')
	if first_stroke==second_stroke:
		a=1
	elif len(first_stroke)>len(second_stroke):
		a=2
	elif second_stroke=="learn":
		a=3
	print(a)
	return a
two_strokes()


#Задание 3
print('Задание 3')

score_list=[{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [4,4,4,5,3]},
{'school_class': '4c', 'scores': [3,4,4,3,2]}]
avg_score_class=[]
avg_score_school=0
for scores in score_list:
	scores_class=scores.get('scores')
	scores_class=sum(scores_class)/len(scores_class)
	print('В классе {} средний балл равен {}'.format(scores.get('school_class'), scores_class))
	avg_score_class.append(scores_class)
avg_score_school=sum(avg_score_class)/len(avg_score_class)
print('В школе средний бал оставляет {}'.format(avg_score_school))


#Задание 4
print('Задание 4')

names_list=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
for names in names_list:
	if names == "Валера":
		print('Валера нашелся {}-ым в списке'.format(1+names_list.index(names)))

def find_person(name):
	names_list=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
	for names in names_list:
		if names == name:
			result='{} нашелся {}-ым в списке'.format(name,1+names_list.index(names))
	return result
print(find_person('Вася'))

def ask_user():
	while True:
		answer=input("Как дела? ")
		if answer=='Хорошо':
			break
	return answer
ask_user()

def get_answer():
	question=input("Введите свой вопрос: ")
	answers={"привет":"И тебе привет!", "как дела": "Хорошо", "пока":"И тебе не хворать"}
	bot=answers[question.lower()]
	return bot

def ask_user():
	while True:
		answer=get_answer()
		print(answer)
		if get_answer()=='пока':
			break
	return answer
ask_user()






#Задание 5
print('Задание 5')

