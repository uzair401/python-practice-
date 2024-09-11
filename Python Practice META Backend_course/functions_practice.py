# Lambda Functions 

numbers = [1,2,4,3,5,56]

square = map(lambda x: x**2, numbers)

print(list(square))
# def calculate_grades(scores):
#     dict={}
#     for key, value in scores.items():
#         if value >= 90:
#             dict[key] = 'A'
#         elif value >= 80:
#             dict[key] = 'B'
#         elif value >= 70:
#             dict[key] = 'C'
#         elif value >= 60:
#             dict[key] = 'D'
#         elif value >= 50:
#             dict[key] = 'E'
#         elif value <= 50:
#             dict[key] = 'F'
#     return dict
    

# student_scores = {
#     "Ali": 90,
#     "Sara": 76,
#     "Umar": 65,
#     "Ayesha": 82
# }
# print(calculate_grades(student_scores))


# def get_min_max_sum(numbers):
#     min_num = numbers[0]
#     max_num = numbers[0]
#     total_sum = sum(numbers) 
    
#     for num in numbers:
#         if num < min_num:
#             min_num = num
#         elif num > max_num:
#             max_num = num
    
#     return min_num, max_num, total_sum

# nums = [10, 20, 30, 40, 50]
# print(get_min_max_sum(nums)) 