def parse(companies, name_file):

    names_set = set()
    for line in companies:
        line = line.strip('\n').split('|')
        if len(line) > 1:
            names_set.add(line[1])
    for name in names_set:
        name_file.write(str(name) + '\n')




def main():
    # download most updated unparsed list here: https://www.sec.gov/Archives/edgar/full-index/
    # and go to the most recent year.
    file = open('2020_company_list.idx', 'r')
    name_file = open('company_names.idx', 'w')
    companies = file.readlines()

    parse(companies, name_file)

main()
