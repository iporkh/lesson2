#Задание:

# Создать список с оценками учеников разных классов школы вида 
#[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school_scores = [
		
		{
		'school_class': '5А',
		'scores': [4, 3, 4, 5, 3, 3]
	},
		
		{
		'school_class': '5Б',
		'scores': [4, 4, 5, 5, 2, 4]
	},
		
		{
		'school_class': '5В',
		'scores': [5, 5, 5, 3, 2]
	}
	
]


    # avg_sum = 0

        for each_class in school_scores:
        		
        	my_sum = 0

        	for score in each_class.get('scores'):
        	   my_sum += score

        	   class_pupils = len(each_class.get('scores'))
        	   
               print(my_sum / class_pupils)
        			

        
	
# for score in school_scores.get.('scores'):
# 	print(round((sum(score)) / len(score), 1))


# print(school_scores[0])	
# print(school_scores[0]['scores'])
# print(sum(school_scores[0]['scores']))
# print(round((sum(school_scores[0]['scores'])) / len(school_scores[0]['scores']), 1))
# print(round((sum(school_scores[1]['scores'])) / len(school_scores[1]['scores']), 1))
# print(round((sum(school_scores[2]['scores'])) / len(school_scores[2]['scores']), 1))

