import datetime

def main():
    # 初始化
    error_List = []
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    id_number = input("请输入18位中国居民身份证号码：")

    # 长度校验
    if len(id_number) != 18:
        error_List.append("长度不等于18位")

    # 字符校验
    if len(id_number) == 18:
        try:
            if id_number[17] in ("X", "x"):
                int(id_number[:17:1])
            else:
                int(id_number)
        except ValueError:
            error_List.append("含有非数字的字符")

    # 日期校验
    if len(id_number) == 18:
        try:
            birth_date = datetime.datetime.strptime(id_number[6:14:1], "%Y%m%d")
            if birth_date > datetime.datetime.now():
                Eerror_List.append("无效的出生日期")
        except ValueError:
            error_List.append("无效的出生日期")

    # 权位校验
    if len(id_number) == 18:
        total_sum = 0
        for x in range(17):
            total_sum += factors[x] * int(id_number[x])
    
        if check_codes[total_sum % 11] != id_number[17].upper():
            error_List.append("权位校验错误")

    # 5.输出结果
    print("-" * 30)
    if len(error_List) > 0:
        print("身份证格式无效，具体如下：")
        for error in error_List:
            print(f"  ·{error}")
    else:
        print("提示:身份证格式有效！")

        # 输出信息
        print()
        print("身份证信息:")
        if int(id_number[16]) % 2 == 0:
            print("性别:女")
        else:
            print("性别:男")
        print(f"出生日期{birth_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
