def analyze_function_behavior(func, x_values):
    """
    分析函数行为 - 循环控制语句应用
    """
    print("=== 函数行为分析 ===")
    
    valid_points = 0
    undefined_points = 0
    
    for i, x in enumerate(x_values):
        # 使用continue跳过无效点
        if x is None:
            continue
        
        try:
            y = func(x)
            
            # 使用break在发现异常值时停止
            if abs(y) > 1000:  # 异常大的值
                print(f"⚠️  在 x={x} 发现异常值: {y}，停止分析")
                break
            
            print(f"f({x:.2f}) = {y:.4f}")
            valid_points += 1
            
        except (ValueError, ZeroDivisionError):
            print(f"f({x:.2f}) = undefined")
            undefined_points += 1
            # continue 会在这里自动执行
    
    else:
        # 如果循环正常结束（没有break），执行这里
        print(f"\n✅ 分析完成: {valid_points}个有效点, {undefined_points}个未定义点")
    
    return valid_points, undefined_points

# 测试函数
def complex_function(x):
    if x == 2:
        return 10000  # 模拟异常值
    return 1 / (x - 1) if x != 1 else float('inf')

test_values = [0, 0.5, 1, 1.5, 2, 2.5, 3]
valid, undefined = analyze_function_behavior(complex_function, test_values)