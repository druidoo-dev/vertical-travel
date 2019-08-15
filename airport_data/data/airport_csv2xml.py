# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import csv

csvFile = 'airport_data.csv'
xmlFile = 'airport_data.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
xmlData.write('<openerp>' + "\n")
# there must be only one top-level tag
xmlData.write('  ' + '<data noupdate="1">' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write(
            '    <record forcecreate="True" id="%s" model="res.partner">\n'
            % rowNum
        )
        for i in range(len(tags)):
            row[i] = row[i].replace('&', '&amp;')
            xmlData.write(
                '      <field name="%s">%s</field>\n' % (tags[i], row[i])
            )
        xmlData.write('    ' + '</record>' + "\n")
    rowNum += 1

xmlData.write('  ' + '</data>' + "\n")
xmlData.write('</openerp>' + "\n")
xmlData.close()
