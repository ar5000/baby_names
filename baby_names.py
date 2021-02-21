import re, sys, os


def baby_names_parser(filename):
    print(filename)
    try: 
        with open(filename, 'r',encoding = 'utf-8') as f:
            ingest = f.read()

    except:
        print(f'Could not find {filename}')
        return False

    # parsed_file = ingest
    # return parsed_file

    year = re.search(r'Popularity\sin\s(\d{4})', ingest).group()[-4:]    

    # <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
    raw_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', ingest)
    
    boy = {}
    girl = {}

    for line in raw_list:
        boy[line[1]] = int(line[0])
        girl[line[2]] = int(line[0])
    
    names[year]= {"Male": boy, "Female": girl}
    # print(names)

def main():
    global names
    names = {
    # '2004':{
    #     'boy':{
    #         "Alex": 4,
    #         "Graham": 3,
    #         "Kyle": 1,
    #         "Miguel": 5,
    #         "Steven": 2},
    #     'girl':{
    #         "Judy": 3,
    #         "Diane": 2,
    #         "Maria": 1,
    #         "Sarah": 5,
    #         "Katie": 4}
    #     },
    # '2005':{
    #     'boy':{
    #         "Alex": 3,
    #         "Graham": 4,
    #         "Kyle": 1,
    #         "Miguel": 2,
    #         "Steven": 5},
    #     'girl':{
    #         "Judy": 2,
    #         "Diane": 1,
    #         "Maria": 3,
    #         "Sarah": 5,
    #         "Katie": 4}
    #     }
    }

    print('Baby Name Parser')
    args = sys.argv[1:]
    if not args:
        print(f'Current working directory is: {os.getcwd()}')
        print(f'Files available for parsing are:')
        [print(f'data/{name}') for name in os.listdir(path='data/')]
        print('Or "--all" to recurse the entire data/ directory')
    elif args == '--all':
        args = os.listdir(path='data/')
        os.chdir('data/')
    else:
        for filename in args:
            baby_names_parser(filename)

        if names:
            for year in names.keys():
                print(f'\nYear: {year}')
                for gender in names[year]:
                    print(f'\n\tGender: {gender}')
                    for name in sorted(names[year][gender], key=str.lower)[:9]:
                        print(f'\t\t{name}: {names[year][gender][name]}')

if __name__ == '__main__':
    main()