print("学生信息")
student_name = input("请输入你的名字: ")
student_id = input("请输入你的学号: ")
student_age = int(input("请输入你的年龄: "))
student_height = float(input("请输入你的身高（米）: "))
student_major = input("请输入你的专业: ")
student_gpa = float(input("请输入你的GPA: "))
is_college_student = input("你是大学生吗？(是/否): ")
if is_college_student == "是":
    is_college_student = "是"
else:
    is_college_student = "否"

math_score = float(input("请输入你的数学成绩: "))
english_score = float(input("请输入你的英语成绩: "))
statistics_score = float(input("请输入你的统计学成绩: "))
total_score = math_score + english_score + statistics_score
average_score = total_score / 3

print(f"""\n个人信息"
姓名：{student_name}
学号：{student_id}
年龄：{student_age}岁
专业：{student_major}
GPA：{student_gpa}

📊 成绩单：
  数学：{math_score}分
  英语：{english_score}分  
  编程：{statistics_score}分
  总分：{total_score}分
  平均：{average_score:.1f}分
是否是大学生：{is_college_student}
""")   
