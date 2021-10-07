import csv

import xml.etree.cElementTree as et
tree = et.parse("covid_cases_xml.xml")
root = tree.getroot()

dateRep = []
countryterritoryCode = []
cases = []
deaths = []

for Dr in root.iter('dateRep'):
    dateRep.append(Dr.text)

for Ct in root.iter('countriesAndTerritories'):
    countryterritoryCode.append(Ct.text)

for Ca in root.iter('cases'):
    cases.append(Ca.text)

for D in root.iter('deaths'):
    deaths.append(D.text)


NAMEScol = ['Date Reported', 'Countries and Territories', 'cases', 'deaths']


length = len(dateRep)

with open("covid_cases.csv", newline="", mode="w") as csvGenerator:
    csv_buf = csv.writer(csvGenerator)

    csv_buf.writerow(NAMEScol)

    for count in range(length):
        rowSet = [dateRep[count], countryterritoryCode[count], cases[count], deaths[count]]
        csv_buf.writerow(rowSet)