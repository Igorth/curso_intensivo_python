import csv

filename = 'blogs.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_now = next(reader)

	print(header_now)