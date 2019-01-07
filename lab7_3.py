class SuperStr(str):

    def is_palindrom(self):
        rev = ''
        for let in self.lower():
            rev = let + rev
        return rev == self.lower()

    def is_repeatance(self, s):
        if isinstance(s, str):
            if s != '':
                return self == s*(len(self)//len(s))
            else:
                return False
        else:
            return False


s = SuperStr('123123123123')
print (s.is_repeatance('123')) # True
print (s.is_repeatance('123123')) # True
print (s.is_repeatance('123123123123')) # True
print (s.is_repeatance('12312')) # False
print (s.is_repeatance(123)) # False
print (s.is_palindrom()) # False
print (s) # 123123123123 (рядок)
print (int(s)) # 123123123123 (ціле число)
print (s + 'qwe') # 123123123123qwe
p = SuperStr('123_321')
print (p.is_palindrom()) # True
t = SuperStr('Andna')
print (t.is_palindrom()) # True