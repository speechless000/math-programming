def check_student_eligibility():
    """检查学生资格"""
    print("=== 学生资格检查系统 ===")
    
    # 获取输入
    age = int(input("请输入年龄: "))
    has_id = input("是否有学生证? (y/n): ").lower() == 'y'
    grade = int(input("请输入成绩: "))
    
    print(f"\n年龄: {age}, 学生证: {has_id}, 成绩: {grade}")
    
    # 嵌套条件判断
    if age >= 18:
        if has_id:
            if grade >= 60:
                print("🎉 符合所有条件！可以参加活动")
            else:
                print("❌ 成绩不合格")
        else:
            print("❌ 需要学生证")
    else:
        print("❌ 年龄不符合要求")
    
    print("\n检查完成!")

def weather_advisor():
    """天气建议系统"""
    print("\n=== 天气建议系统 ===")
    
    temperature = int(input("当前温度(℃): "))
    is_raining = input("是否下雨? (y/n): ").lower() == 'y'
    is_weekend = input("是否是周末? (y/n): ").lower() == 'y'
    
    print(f"\n温度: {temperature}℃, 下雨: {is_raining}, 周末: {is_weekend}")
    
    # 复杂的嵌套条件
    if is_weekend:
        if not is_raining:
            if temperature > 25:
                print("🌞 适合去游泳！")
            elif temperature > 15:
                print("🌤️ 适合去公园散步")
            else:
                print("🧥 天气较冷，建议室内活动")
        else:
            print("🌧️ 下雨天，适合在家看书或看电影")
    else:
        print("📚 工作日，专心学习吧！")

if __name__ == "__main__":
    check_student_eligibility()
    weather_advisor()
    print("\n✅ 嵌套条件学习完成!")