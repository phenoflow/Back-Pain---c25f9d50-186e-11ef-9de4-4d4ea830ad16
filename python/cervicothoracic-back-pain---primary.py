# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"N140100","system":"readv2"},{"code":"N141.00","system":"readv2"},{"code":"N140500","system":"readv2"},{"code":"N148300","system":"readv2"},{"code":"N141.11","system":"readv2"},{"code":"N148A00","system":"readv2"},{"code":"N140300","system":"readv2"},{"code":"N148400","system":"readv2"},{"code":"N144000","system":"readv2"},{"code":"N148.00","system":"readv2"},{"code":"N144011","system":"readv2"},{"code":"N148B00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('back-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cervicothoracic-back-pain---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cervicothoracic-back-pain---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cervicothoracic-back-pain---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
