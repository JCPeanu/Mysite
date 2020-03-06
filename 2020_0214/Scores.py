class Student:
    def __init__(self, name, math, eng, chi, bio):
        self.name = name
        self.math = math
        self.eng = eng
        self.chi = chi
        self.bio = bio
    def info(self):
        fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
        return fmt.format(self.name, self.math, self.eng, self.chi, self.bio)
def print_scores(sts):
    for st in sts:
        print(st.info())

def select_math_larger_equal(sts, math):
    chosen = []
    for st in sts:
        if st.math >= math:
            chosen.append(st)
    return chosen
def select_chinese_less(sts, chi):
    chosen = []
    for st in sts:
        if st.chi <= chi:
            chosen.append(st)
    return chosen
def avg(sts):
    sum = 0
    num = 0
    for st in sts:
        num += 1
        sum += st.bio
    return round(sum/num)
def select_biology_higher_avg(sts, avg):
    chosen = []
    for st in sts:
        if st.bio >= avg:
            chosen.append(st)
    return chosen

def select_english_lowest(sts):
    lowest = sts[0]
    for st in sts:
        if st.eng < lowest.eng:
            lowest = st
    return lowest
def select_avg_highest(sts):
    highest = sts[0]
    for st in sts:
        if st.eng > highest.eng:
            highest = st
    return highest

def read_scores():
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    with open('scores.txt') as f1:
        line = f1.readline()
        line = line.strip()
        ts = line.split()
        print(fmt.format(ts[0], ts[1], ts[2], ts[3], ts[4]))
        sts = []
        for line in f1:
            ts = line.strip().split()
            st = Student(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            sts.append(st)
        print('-'*50)
        print('select math score larger equal:')
        chosen_sts = select_math_larger_equal(sts, 85)
        print_scores(chosen_sts)
        print('-'*50)
        print('select chinese score less equal:')
        chosen_sts = select_chinese_less(sts, 85)
        print_scores(chosen_sts)
        print('-'*50)
        print('select the biology score higer than average:')
        chosen_sts = select_biology_higher_avg(sts, avg(sts))
        print_scores(chosen_sts)
        print('-'*50)
        print('select the lowest english score')
        lowest_sts = select_english_lowest(sts)
        print(lowest_sts.info())
        print('-'*50)
        print('select the highest average:')
        highest_sts = select_avg_highest(sts)
        print(highest_sts.info()) 
        
        

read_scores()