class Student:
    sid = 'unknown'
    name = 'unknown'
    gender = 'unknown'
    height = 0
    weight = 0
    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
    def set_height(self, h):
        self.height = h
    def set_weight(self, w):
        self.weight = w
    def info(self):
        fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
        return fmt.format(self.sid, self.name, self.gender, self.height, self.weight)
class BMIReport:
    name = 'unknwon'
    sts = []
    def __init__(self, name):
        self.name = name
    def add_student(self, st):
        self.sts.append(st)
    def remove_student(self, sid):
        remove = None
        for st in self.sts:
            if st.sid == sid:
                remove = st
                break
        self.sts.remove(remove)
    def save_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.name)
            f.write('\n')
            for st in self.sts:
                print(st.info())
                f.write(st.info())
                f.write('\n')
    def read_file(self, filename):
        with open (filename) as f:
            first = f.readline()
            self.name = first.strip()
            for line in f:
                ts = line.strip().split(',')
                st = Student(ts[0], ts[1], ts[2])
                st.set_height(float(ts[3]))
                st.set_weight(float(ts[4]))
                #print(st.info())
                self.add_student(st)
        #self.report.save_file()
    #self.read_file()
    def print_report(self):
        for st in self.sts:
            print(st.info())
def test1():
    report = BMIReport("Class A")
    report.read_file('BMI.txt')
    report.save_file('results.txt')
def test2():
    report = BMIReport('')
    report.read_file('BMI.txt')
    report.print_report()
def test3():
    report = BMIReport('')
    report.read_file("BMI.txt")
    report.remove_student("A01")
    st = Student("A10", "Easter", "M")
    st.set_height
    st.set_height(160)
    st.set_weight(65)
    report.add_student(st)
    report.save_file("results2.txt")
#test1()
#test2()
test3()