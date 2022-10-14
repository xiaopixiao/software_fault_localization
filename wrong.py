import re
from math import *

global block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, \
       block14, block15, block16, block17, block18, block19, block20, block21, block22, block23, block24, block25, \
       block26, block27, block28, block29, block30, block31, block32, block33, block34, block35, block36, block37, \
       block38, block39, block40
block1 = 0
block2 = 0
block3 = 0
block4 = 0
block5 = 0
block6 = 0
block7 = 0
block8 = 0
block9 = 0
block10 = 0
block11 = 0
block12 = 0
block13 = 0
block14 = 0
block15 = 0
block16 = 0
block17 = 0
block18 = 0
block19 = 0
block20 = 0
block21 = 0
block22 = 0
block23 = 0
block24 = 0
block25 = 0
block26 = 0
block27 = 0
block28 = 0
block29 = 0
block30 = 0
block31 = 0
block32 = 0
block33 = 0
block34 = 0
block35 = 0
block36 = 0
block37 = 0
block38 = 0
block39 = 0
block40 = 0

# 将算式从字符串处理成列表，解决横杠是负号还是减号的问题
def formula_format(formula):
    """
    :param formula: str
    """
    global block1
    block1 = 0
    formula = re.sub(' ', '', formula)  # 去掉算式中的空格s
    # 以 '横杠数字' 分割， 其中正则表达式：(\-\d+\.?\d*) 括号内：
    # \- 表示匹配横杠开头；\d+ 表示匹配数字1次或多次；\.?表示匹配小数点0次或1次;\d*表示匹配数字0次或多次。
    formula_list = [i for i in re.split('(-[\d+,π,e]\.?\d*)', formula) if i]
    final_formula = []  # 最终的算式列表
    block1 = 1
    for item in formula_list:
        # 算式以横杠开头，则第一个数字为负数，横杠为负号
        if len(final_formula) == 0 and re.match('-[\d+,π,e]\.?\d*$', item):
            global block2
            block2 = 0
            final_formula.append(item)
            block2 = 1
            continue
        # 如果当前的算式列表最后一个元素是运算符['+', '-', '*', '/', '('， '%'， '^'], 则横杠为减号
        if len(final_formula) > 0:
            if re.match('[\+\-\*\/\(\%\^]$', final_formula[-1]):
                global block3
                block3 = 0
                final_formula.append(item)
                block3 = 1
                continue
        # 按照运算符分割开
        global block4
        block4 = 0
        item_split = [i for i in re.split('([\+\-\*\/\(\)\%\^\√])', item) if i]
        final_formula += item_split
        block4 = 1
    return final_formula


# 判断是否是运算符，如果是返回True
def is_operator(e):
    """
    :param e: str
    :return: bool
    """
    global block5
    block5 = 0
    opers = ['+', '-', '*', '/', '(', ')', '%', '^', '√', 'sin', 'arcsin', 'ln']
    block5 = 1
    return True if e in opers else False  # 在for循环中嵌套使用if和else语句


# 比较连续两个运算符来判断是压栈还是弹栈
def decision(tail_op, now_op):
    """
    :param tail_op: 运算符栈的最后一个运算符
    :param now_op: 从算式列表取出的当前运算符
    :return: 1代表弹栈运算，0代表弹出运算符栈最后一个元素'('，-1表示压栈
    """
    global block6
    block6 = 0
    # 定义4种运算符级别
    rate1 = ['+', '-']
    rate2 = ['*', '/', '%']
    rate3 = ['^', '√', 'sin', 'arcsin', 'ln']
    rate4 = ['(']
    rate5 = [')']
    block6 = 1

    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3 or now_op in rate4:
            global block7
            block7 = 1
            return -1  # 说明当前运算符优先级高于运算符栈的最后一个运算符，需要压栈
        else:
            global block8
            block8 = 1
            return 1  # 说明当前运算符优先级等于运算符栈的最后一个运算符，需要弹栈运算

    elif tail_op in rate2:
        if now_op in rate3 or now_op in rate4:
            global block9
            block9 = 1
            return -1
        else:
            global block10
            block10 = 1
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            global block11
            block11 = 1
            return -1
        else:
            global block12
            block12 = 1
            return 1

    elif tail_op in rate4:
        if now_op in rate5:
            global block13
            block13 = 1
            return 0  # '('遇上')',需要弹出'('并丢掉')',表明该括号内的算式已计算完成并将结果压入数字栈中
        else:
            global block14
            block14 = 1
            return -1  # 只要栈顶元素为'('且当前元素不是')'，都应压入栈中


# 传入两个数字，一个运算符，根据运算符不同返回相应结果
def calculate(n1, n2, operator):
    """
    :param n1: float
    :param n2: float
    :param operator: + - * / % ^
    :return: float
    """
    global block14
    block14 = 1
    result = 0
    if operator == '+':
        global block15
        block15 = 0
        result = n1 + n2
        block15 = 1
    if operator == '-':
        global block16
        block16 = 0
        result = n1 - n2
        block16 = 1
    if operator == '*':
        global block17
        block17 = 0
        result = n1 * n2
        block17 = 1
    if operator == '/':
        global block18
        block18 = 0
        if n2 == 0:
            print('Error:除数为0.')
            exit(0)
        result = n1 / n2
        block18 = 1
    if operator == '%':
        global block19
        block19 = 0
        result = n1 % n2
        block19 = 1
    if operator == '^':
        global block20
        block20 = 0
        result = n1 * n2     #错误代码块
        block20 = 1
    return result


# 括号内的算式求出计算结果后，计算√()、sin()或arcsin()
def gaojie(op_stack, num_stack):
    if op_stack[-1] == '√':
        global block21
        block21 = 0
        op = op_stack.pop()
        num2 = num_stack.pop()
        if num2 < 0:
            print("Error:√内小于0.")
            exit(0)
        num_stack.append(sqrt(num2))
        block21 = 21
    elif op_stack[-1] == 'sin':
        global block22
        block22 = 0
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(sin(num2))
        block22 = 1
    elif op_stack[-1] == 'arcsin':
        global block23
        block23 = 0
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(asin(num2))
        block23 = 1
    elif op_stack[-1] == 'ln':
        global block24
        block24 = 0
        op = op_stack.pop()
        num2 = num_stack.pop()
        if num2 < 0:
            print("Error:ln内小于0.")
            exit(0)
        num_stack.append(log(num2))
        block24 = 1


# 负责遍历算式列表中的字符，决定压入数字栈中或压入运算符栈中或弹栈运算
def final_calc(formula_list):
    """
    :param formula_list: 算式列表
    :return: 计算结果
    """
    global block25
    block25 = 0
    num_stack = []  # 数字栈
    op_stack = []  # 运算符栈
    block25 = 1
    for item in formula_list:
        global block26
        block26 = 0
        operator = is_operator(item)
        block26 = 1
        # 压入数字栈
        if not operator:
            # π和e转换成可用于计算的值
            if item == 'π':
                global block27
                num_stack.append(pi)
                block27 = 1
            elif item == '-π':
                global block28
                num_stack.append(-pi)
                block28 = 1
            elif item == 'e':
                global block29
                num_stack.append(e)
                block29 = 1
            elif item == '-e':
                global block30
                num_stack.append(-e)
                block30 = 1
            else:
                global block31
                num_stack.append(float(item))  # 字符串转换为浮点数
                block31 = 1
        # 如果是运算符
        else:
            while True:
                # 如果运算符栈为空，则无条件入栈
                if len(op_stack) == 0:
                    global block32
                    op_stack.append(item)
                    block32 = 1
                    break
                # 决定压栈或弹栈
                global block33
                tag = decision(op_stack[-1], item)
                block33 = 1
                # 如果是-1，则压入运算符栈并进入下一次循环
                if tag == -1:
                    global block34
                    op_stack.append(item)
                    block34 = 1
                    break
                # 如果是0，则弹出运算符栈内最后一个'('并丢掉当前')'，进入下一次循环
                elif tag == 0:
                    global block35
                    op_stack.pop()
                    if op_stack == []:
                        break
                    gaojie(op_stack, num_stack)  # '('前是'√'、'sin'或'arcsin'时，对括号内算式的计算结果作相应的运算
                    block35 = 1
                    break
                # 如果是1，则弹出运算符栈内最后一个元素和数字栈内最后两个元素
                elif tag == 1:
                    if item in ['√', 'sin', 'arcsin']:
                        global block36
                        op_stack.append(item)
                        block36 = 1
                        break
                    global block37
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    # 将计算结果压入数字栈并接着循环，直到遇到break跳出循环
                    num_stack.append(calculate(num1, num2, op))
                    block37 = 1
    # 大循环结束后，数字栈和运算符栈中可能还有元素的情况
    while len(op_stack) != 0:
        global block38
        op = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(calculate(num1, num2, op))
        block38 = 1
    global block39
    result = str(num_stack[0])
    block39 = 1
    # 去掉无效的0和小数点，例：1.0转换为1
    if result[len(result) - 1] == '0' and result[len(result) - 2] == '.':
        global block40
        result = result[0:-2]
        block40 = 1
    return result


if __name__ == '__main__':
    #formula = "2 * ( 3 - 5 * ( - 6 + 3 * 2 / 2 ) )"
    fo = open('test_case.txt', "r", encoding='utf-8')
    s = fo.read()
    fo.close()
    s_ls = s.split('\n')
    po = open('answer_wrong.txt', 'w')
    for i in s_ls:
        formula = i
        formula_list = formula_format(formula)
        #print(formula_list)
        result = final_calc(formula_list)
        print("算式：", formula)
        result = eval(result)
        #print("计算结果：", result)
        print("计算结果：{0:.5f}".format(result))
        po.write('result:{0:.5f}  block:'.format(result))
        for i in range(1, 41):
            if eval('block{}'.format(i)) == 1:
                print(i)
                po.write('{},'.format(i-1))
        po.write('\n')
        block1 = 0
        block2 = 0
        block3 = 0
        block4 = 0
        block5 = 0
        block6 = 0
        block7 = 0
        block8 = 0
        block9 = 0
        block10 = 0
        block11 = 0
        block12 = 0
        block13 = 0
        block14 = 0
        block15 = 0
        block16 = 0
        block17 = 0
        block18 = 0
        block19 = 0
        block20 = 0
        block21 = 0
        block22 = 0
        block23 = 0
        block24 = 0
        block25 = 0
        block26 = 0
        block27 = 0
        block28 = 0
        block29 = 0
        block30 = 0
        block31 = 0
        block32 = 0
        block33 = 0
        block34 = 0
        block35 = 0
        block36 = 0
        block37 = 0
        block38 = 0
        block39 = 0
        block40 = 0

    # formula_list = formula_format(formula)
    # result = final_calc(formula_list)
    # result = eval(result)
    # print("算式：", formula)
    # print("计算结果：{0:.5f}".format(result))