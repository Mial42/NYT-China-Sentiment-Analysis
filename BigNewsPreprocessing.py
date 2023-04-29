import csv


csv.field_size_limit(131072 * 2)

acceptable_publications = set(['Washington Post', 'Vox', 'Reuters', 'The New York Times', 'CNBC', 'Business Insider', 'Axios', 'Economist', 'Fox News', 'The Hill'])
acceptable_years = set(['2016','2017','2018','2019','2020'])
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
    #print(row[1] in acceptable_years)
    #print(row[9])
    if row[1] in acceptable_years and row[9] in acceptable_publications:

      if 'China' in row[6] or 'Chinese' in row[6]:
        writer.writerow(row)
