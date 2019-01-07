def signs1(m, n):
    def calc_step(level, current):
        if level > n:
            return current == m
        res = calc_step(level + 1, current + level)
        if res:
            return '+' + str(level) + str(res)
        res = calc_step(level + 1, current - level)
        if res:
            return '-' + str(level) + str(res)

    res = calc_step(2, 1)
    if res:
        return '1' + res[:-4]
    return False

print (signs1(3, 5))  # 1-2+3-4+5
print (signs1(2, 20)) # 1+2+3+4+5+6+7+8+9+10+11+12+13-14+15-16-17-18-19-20
# print (signs1(2, 30)) # False
# print (signs1(3, 30)) # 1+2+3+4+5+6+7+8+9+10+11+12+ 13+14+15+16+17+18+19+20-21-22-23+24-25-26-27-28-29-30

def signs2(m, n):
    def calc_step(level, current):
        if level > n:
            return current == m
        sum_of_next = 1.0 * (level + n) / 2 * (n - level + 1)
        if m > current + sum_of_next or m < current - sum_of_next :
            return False
        res = calc_step(level + 1, current + level)
        if res:
            return '+' + str(level) + str(res)
        res = calc_step(level + 1, current - level)
        if res:
            return '-' + str(level) + str(res)

    res = calc_step(2, 1)
    if res:
        return '1' + res[:-4]
    return False

def signs3(m, n):
    def calc_step(level, current):
        if level < 1:
            return current == m
        sum_of_next = 1.0 * (level + 1) / 2 * (level)
        if m > current + sum_of_next or m < current - sum_of_next :
            return False
        res = calc_step(level - 1, current + level)
        if res:
            return '+' + str(level) + str(res)
        res = calc_step(level - 1, current - level)
        if res:
            return '-' + str(level) + str(res)

    res = calc_step(n-1, n)
    if res:
        return str(n) + res[:-4]
    return False

def signs4(m, n):
    def add_1_to_binary_number(s):
        digit = n-2
        while s[digit] != '0':
            if s[digit] == '1':
                s = s[:digit] + '0' + s[digit+1:]
            digit -= 1
        s = s[:digit] + '1' + s[digit+1:]
        return s

    s = '0' * (n-1)
    s_final = '1' * (n-1)
    while s != s_final:
        # generate next position
        s = add_1_to_binary_number(s)
        # calculate sum
        res = n
        res_str = str(n)
        for j in range(0, n-1):
            sequence_element = n-1-j
            string_element = int(s[j])
            res = res + sequence_element * int(s[string_element]) - sequence_element * (1-string_element)
            res_str += '+'*string_element + '-'*(1-string_element) + str(sequence_element)
        if res == m:
            return res_str
    return False

# 1.5sec, 22740 combinations
counter = 0
n = 8
print 'v7, recursion bactracking'

def output_desk(p):
    if p == None:
        return
    for i in range(n):
        row = ''
        for j in range(n):
            flag = False
            for ii in range(n):
                if p[ii][0] == i and p[ii][1] == j:
                    flag = True
            row += '1'*int(flag) + '0'*(1-int(flag))
        print row

def is_ok(p):
    global counter
    counter += 1
    for i in range(n):
        for j in range(n):
            if i != j and \
                (p[i][0] == p[j][0] or p[i][1] == p[j][1] \
                or p[i][0]+p[i][1] == p[j][0]+p[j][1] \
                or n-p[i][0]+p[i][1] == n-p[j][0]+p[j][1]):
                return False
    return True  

def find_position():
    def try_queen(pos):
        if len(pos) == n:
            if is_ok(pos):
                return pos
            else:
                return False
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if pos[i][1] == pos[j][1]:
                    return False
        for current_queen_pos in range(0,n):
            pos_new = pos[:]
            pos_new.append((len(pos), current_queen_pos))
            res = try_queen(pos_new)
            if res:
                return res

    start_position = []
    return try_queen(start_position)

p = find_position()
print (counter)
print (p)
output_desk(p)