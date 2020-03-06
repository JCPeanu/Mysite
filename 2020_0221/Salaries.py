class WorkRecord:
    name = 'unknown'
    week = None
    wage = 0
    def __init__(self, names):
        self.week = [0 for i in range(7)]
    def workHour(self, day, hours):
        self.week[day] = hours
    def setWage(self, wage):
        self.wage = wage
    def weekWage(self):
        dayWage = [self.wage * hours for hours in self.week]
        return sum(dayWage)

def read_file():
    with open('names.txt') as f:
        first = f.readline()
        for line in f:
            line = line.strip()
            tokens = line.split()
            wr = WorkRecord(tokens[0])
            for i in range(1, 7):
                wr.workHour(i, float(tokens[i]))
            wr.setWage(float(tokens[7]))
            print(wr.weekWage())
read_file()
'''def total(sts):
    total = 0
    chosen = []
    real_chosen = []
    for st in sts:
        total = 0
        hours = st.mon + st.tues + st.weds + st.thur + st.fri + st.sat
        total += hours
        chosen.append(st.names)
        chosen.append(total * st.wages)
    return chosen

def readsal():
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'
    with open('names.txt') as f1:
        line = f1.readline()
        line = line.strip()
        ts = line.split()
        print(fmt.format(ts[0], ts[1], ts[2], ts[3], ts[4], ts[5], ts[6], ts[7]))
        sts = []
        for line in f1:
            ts = line.split()
            st = Days(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]), float(ts[5]), float(ts[6]), float(ts[7]))
            sts.append(st)
            print('-'*50)
            print(total(sts))
readsal()'''
