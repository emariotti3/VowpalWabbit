import csv

with open('../home/eugenia/phraug2/train.csv', 'r') as infile, open('../home/eugenia/phraug2/train_vw.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['Prediction ', 'UserId', 'ProfileName', 'ProductId', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Id', 'Time', 'Summary', 'Text']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)
