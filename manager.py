from fastai2.basics import *
# import pickle

Wave = { 'L': 'Loading', 'W': 'Wave', 'U': 'Undefined', 'MB': 'MiniBoss', 'B': 'Boss' }
State = { 'O': 'Ongoing', 'V': 'Victory', 'L': 'Loose' }

filename = 'data.csv'
fieldnames = ['Name', 'Run', 'Wave', 'State', 'Button']
example = [{'Name': 'Example1.jpg', 'Run': 'TOA', 'Wave': 'L', 'State': 'O', 'Button': 'False' }, {'Name': 'Example2.jpg', 'Run': 'TOA', 'Wave': 'L', 'State': 'O', 'Button': 'False' }]

imagestemp = get_image_files('temp')
folder = 'Images'

import csv

# Create
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['Name', 'Run', 'Wave', 'State', 'Button']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'Name': 'Example2.jpg', 'Run': 'TOA', 'Wave': 'L', 'State': 'O', 'Button': 'False' })

# Write
def write(filename, fieldnames, data):
	with open(filename, 'a', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerows(data)

# Read
def read(filename):
	with open(filename, "rt") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row.join(', '))

data = []
for image in imagestemp:
	data.append({'Name': image.name, 'Run': 'Cairos', 'Wave': 'MB', 'State': 'O', 'Button': 'False' })

write(filename, fieldnames, data)