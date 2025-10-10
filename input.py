print("学生信息")
student_name = input("请输入你的名字: ")
student_age = int(input("请输入你的年龄: "))
student_height = float(input("请输入你的身高（米）: "))
student_major = input("请输入你的专业: ")

print(f""""\n学生信息如下:"
名字:", student_name
年龄:", student_age, "岁"
身高:", student_height, "米"
专业:", student_major
""")