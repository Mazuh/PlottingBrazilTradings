# -*- coding: utf-8 -*-
from csv import reader

from matplotlib import pyplot, patches

with open('dataset.csv') as csv_file:
    buffered_reader = reader(csv_file, quotechar=',')
    buffered_reader.next()

    for row in buffered_reader:
        if row[-1] == '4' and row[1].upper() == 'BRAZIL':
            year = row[3]
            imports = row[4]
            exports = row[5]
            pyplot.plot(int(year), float(imports), 'bo')
            pyplot.plot(int(year), float(exports), 'ro')

for year in range(1800, 1870):
    pyplot.plot(year, 0, 'o')

red_patch = patches.Patch(color='red', label=u'Exportação')
blue_patch = patches.Patch(color='blue', label=u'Importação')
pyplot.legend(handles=[red_patch, blue_patch])

pyplot.title(u'Importações e exportações do Brasil')
pyplot.ylabel(u'Valor (em bilhões de US$)')
pyplot.xlabel(u'Ano (desde a quebra do Pacto Colonial até 2014)')

#pyplot.savefig('foo.png')
pyplot.show()
