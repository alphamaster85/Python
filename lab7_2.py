class Student(object):
    name = ''
    conf = {
        'exam_max': 0, # кількість балів, доступна за здачу екзамена
        'lab_max': 0, # кількість балів, доступна за виконання 1 практичної роботи
        'lab_num': 0, # кількість практичних робіт в курсі
        'k': 0.0, # частка балів від максимума, яку необхідно набрати для отримання сертифікату
    }
    labs = []
    lab_rat = 0
    exam = 0
    rating = 0.0

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        for i in range(self.conf['lab_num']):
            self.labs.append(0)

    def make_lab(self, m, n = None):

        if n == None:
            for i in range(len(self.labs)):
                if self.labs[i] == 0:
                    if m >= self.conf['lab_max']:
                        self.labs[i] = self.conf['lab_max']
                    else:
                        self.labs[i] = m                    
                    break
        else:
            if n < self.conf['lab_num']:
                if m >= self.conf['lab_max']:
                    self.labs[n] = self.conf['lab_max']
                else:
                    self.labs[n] = m
        
        self.lab_rat = 0
        for i in self.labs:
            self.lab_rat += i
        self.rating = (self.lab_rat + self.exam) / (self.conf['lab_max'] * self.conf['lab_num'] + self.conf['exam_max'])
        return self

    def make_exam(self, m):
        if m >= self.conf['exam_max']:
            self.exam = self.conf['exam_max']
        else:
            self.exam = m
        self.rating = (self.lab_rat + self.exam) / (self.conf['lab_max'] * self.conf['lab_num'] + self.conf['exam_max'])
        return self

    def is_certified(self):
        return (self.rating * 100, self.rating >= self.conf['k'])


conf = {
    'exam_max': 30,
    'lab_max': 7,
    'lab_num': 10,
    'k': 0.61,
}

oleg = Student('Oleg', conf)
oleg.make_lab(1)  # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(8,0)  # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(1)  # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(10,7)  # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(4,1)  # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(5)  # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(6.5)  # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
oleg.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print (oleg.is_certified()) # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print (oleg.is_certified()) # (62.5, True)