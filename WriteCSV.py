import csv


class WriteCSV:
    def __init__(self):
        a = 1

    def write(self, data, number):
        if data[1] is not 'empty' and int(number) != 0:
            with open(r'\\fl-bartender-01\labels\vpdship\VPDLabel.csv', 'wt') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                print('Printing {} labels.'.format(number))
                for i in range(number):
                    filewriter.writerow(data)
        elif data[1] == 'empty':
            print('Unable to retrieve data using ' + data[0])
        else:
            print('No labels printed.')
