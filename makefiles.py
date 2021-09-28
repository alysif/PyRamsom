for i in range(1,11):
    file = open('file{}.txt'.format(i), 'w')
    file.write('file{}'.format(i))
    file.close()