class CombStr():

    def __init__(self, string):
        self.string = str(string)

    def count_substrings(self, length):
        if isinstance(length, int):
            if length <= 0:
                return 0
            elif length > len(self.string):
                return 0
            else:
                count = []
                count.append('')
                for l in range(length):
                    count[0] += self.string[l]
                for i in range(1, len(self.string)-length+1):
                    flag = False
                    for j in range(len(count)):
                        if self.string[i:i+length] == count[j]:
                            flag = True
                    if flag == False:
                        count.append(self.string[i:i+length])
                return len(count)

s0 = CombStr('qqqqqqweqqq%')
print (s0.count_substrings(0)) # 0
print (s0.count_substrings(1)) # 4
print (s0.count_substrings(2)) # 5
print (s0.count_substrings(5)) # 7
print (s0.count_substrings(15)) # 0