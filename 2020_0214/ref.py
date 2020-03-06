def read():
    print('start reading ...')
    with open('test.txt') as f1, open('result.txt', 'w') as f2:
        total = 0
        for line in f1:
            line = line.strip()
            tokens = line.split()
            name, price, amount = tokens[0], float(tokens[1]), float(tokens[2])
            item_total = price * amount
            fmt = '{:10}{:<5}*{:5} = {:>5}\n'.format(name, price, amount, item_total)
            total += item_total
            print(fmt)
            f2.write(fmt)
        #print('-' * 40)
        #print('Total: {:>10}'.format(total))
        f2.write('-'*40+'\n')
        f2.write('Total: {:>10}\n'.format(total))
read()