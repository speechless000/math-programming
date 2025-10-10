my_name = "你的名字"
my_age = 18
my_height = 1.75
my_major = "统计学"
is_college_student = True
student_name = "张伟"
student_age = 20
student_height = 1.80
is_freshman = False 

print("个人信息")
print("姓名", my_name)
print("年龄", my_age)
print("身高", my_height)
print("专业", my_major)
print("是否是大学生", is_college_student)

print(" 数据类型 ")
print(f"{student_name} 的类型: {type(student_name)}")
print(f"{student_age} 的类型: {type(student_age)}")
print(f"{student_height} 的类型: {type(student_height)}")
print(f"{is_freshman} 的类型: {type(is_freshman)}")

math_score = 85
english_score = 92
statistics_score = 88
total_score = math_score + english_score + statistics_score
average_score = total_score / 3
print("总分:", total_score)
print("平均分:", average_score)
print("数学成绩:", math_score)
print("英语成绩:", english_score)
print("统计学成绩:", statistics_score)

print(f"数学成绩的数据类型: {type(math_score)}")
print(f"英语成绩的数据类型: {type(english_score)}")
print(f"统计学成绩的数据类型: {type(statistics_score)}")
print(f"总分的数据类型: {type(total_score)}")
print(f"平均分的数据类型: {type(average_score)}")
print("变量练习结束")