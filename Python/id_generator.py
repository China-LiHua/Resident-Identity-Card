from random import randint
from datetime import datetime
def main():
    while True:
        input_value = input("请问你要生成多少串伪身份证号码：")
        if is_int(input_value):
            if int(input_value) <= 0:
                print("请输入大于0的整数")
                print("-"*40)
            else:
                break
        else:
            print("错误，请输入整数！")
            print("-"*40)
    for x in range(int(input_value)):
        print(f"{x+1}. {generate_id()}")
    print("生成完成！")

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False
        
def generate_id():
    # 初始化
    id_card_number = ""
    checksum = 0
    check_code = ""
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    # 1.随机地址码 
    for x in range(6):
        id_card_number += str(randint(0, 9))

    # 2.随机年份
    id_card_number += f"{randint(1900, datetime.now().year):04d}"

    # 3.随机月份
    if id_card_number[6:10] == str(datetime.now().year):
        id_card_number += f"{randint(1, datetime.now().month):02d}"
    else:
        id_card_number += f"{randint(1, 12):02d}"

    # 4.随机日
    if id_card_number[10:12] == str(datetime.now().month) and id_card_number[6:10] == str(datetime.now().year):
        id_card_number += f"{randint(1, datetime.now().day):02d}"
    elif id_card_number[10:12] == "02" and (int(id_card_number[6:10]) % 400 == 0 or (int(id_card_number[6:10]) % 4 == 0 and int(id_card_number[6:10]) % 100 != 0)):
        id_card_number += f"{randint(1,29):02d}"
    else:
        id_card_number += f"{randint(1,day[int(id_card_number[10:12])-1]):02d}"

    # 5.随机序号码
    id_card_number += f"{randint(0,999):03d}"

    # 6.生成校验码
    for x in range(17):
        checksum += int(id_card_number[x]) * factors[x]
    check_code = check_codes[checksum % 11]

    # 7.拼接校验码
    id_card_number += check_code
    return id_card_number

if __name__ == "__main__":
    main()
