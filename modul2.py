x = [[123], '0123', '123', 123, -123.0, 'a1Z', 0, 000, '777L', 'ZZZZ', '000ZZZZ', 'ZZZZ', 'qweasd', '123123123123123123123', 123123123123123123123, 123123123123123123123, 'bnh34521', 'bnh34521']
n = [4, 5, 3, 4, 11, 36, 10, 10, 10, 36, 36, 35, 33, 11, 11, 10, 31, 11]
m = [3, 6, 5, 1, 16, 16, 2, 2, 2, 13, 13, 13, 36, 16, 16, 10, 14, 14]
a = [False, 102, False, '000000000000000000000000000', False, '32E7', 0, 0, 1100001001, '46A672', '46A672', False, 'HGPEYJ', '2C09BC518E8048D23A', '2C09BC518E8048D23A', 123123123123123123123, '119337DC2BC', False]

code_list = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16, "H" : 17, "I" : 18, "J" : 19, "K" : 20, "L" : 21, "M" : 22, "N" : 23, "O" : 24, "P" : 25, "Q" : 26, "R" : 27, "S" : 28, "T" : 29, "U" : 30, "V" : 31, "W" : 32, "X" : 33, "Y" : 34, "Z" : 35}

def convert_n_to_m(x, n, m):
    if isinstance(x, str) or (isinstance(x, int) and x >= 0):
        
        if x is 0:
            return '0'

        def convert_from_n(num, n):
            num = str(num)

            if num[len(num)-1] == 'L':
                num2 = ''
                for l in range(len(num)-1):
                    num2 += num[l]
                num = num2
            if n == 10:
                return str(num)

            sum = 0
            for i in range(len(num)):
                if code_list[num[i]] >= n:
                    return False
                sum += n**i*code_list[num[len(num)-i-1]]

            return sum

        def convert_to_m(num, m):           

            if num == False:
                return num

            if m == 1:
                return '0' * num
            elif m == 10:
                return num

            def division_rest(num, m):
                num = int(num)

                if num < m:
                    for e in code_list:
                        if code_list[e] == num % m:
                            return str(e)
                else:
                    for e in code_list:
                        if code_list[e] == num % m:
                            return str(division_rest(num / m, m)) + str(e)                   
                    
            return division_rest(num, m)

        if isinstance(x, str):
            x = x.upper()
        if isinstance(x, int):
            x = str(x)

        return convert_to_m(convert_from_n(x, n), m)

    return False

for i in range(len(x)):
    print(convert_n_to_m(x[i], n[i], m[i]))
    # if convert_n_to_m(x[i], n[i], m[i]) == a[i]:
    #     print('v    ' + str(a[i]) + '   ' + str(convert_n_to_m(x[i], n[i], m[i])))
    # elif int(convert_n_to_m(x[i], n[i], m[i])) == a[i]:
    #     print('+    ' + str(a[i]) + '   ' + str(convert_n_to_m(x[i], n[i], m[i])))
    # else:
    #     print('X    ' + str(a[i]) + '   ' + str(convert_n_to_m(x[i], n[i], m[i])))
