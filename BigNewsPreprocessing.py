import csv


csv.field_size_limit(131072 * 2)

# Open the input and output CSV files
with open('big_news.csv', newline='', encoding='utf-8') as input_file, \
     open('china_articles.csv', 'w', newline='', encoding='utf-8') as output_file:
  
  # Create CSV reader and writer objects
  reader = csv.reader(input_file)
  writer = csv.writer(output_file)
  
  # Write the header row to the output file
  writer.writerow(next(reader))
  
  # Loop through the input file and write matching rows to the output file
  for row in reader:
    if 'China' in row[8] or 'Chinese' in row[8]:
      writer.writerow(row)
