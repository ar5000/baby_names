import re, sys, os


def what_files():
    file_names = [f'data/{name}' for name in os.listdir(path='data/')]
    return file_names

def baby_names_parser(filename):
    print(f'File: {filename}')
    try: 
        with open(filename, 'r',encoding = 'utf-8') as f:
            ingest = f.read()

    except:
        print(f'Could not find {filename}')
        return False
    
    boy = {}
    girl = {}

    for rank, boy_name, girl_name in re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', ingest): # create tuples of the table rows (rank, boy_name, girl_name)
        boy[boy_name] = int(rank) # make the boy dict
        girl[girl_name] = int(rank) # make the girl dict
    
    names[re.search(r'Popularity\sin\s(\d{4})', ingest).group()[-4:]]= {"Male": boy, "Female": girl} #add a 'year' entry to the existing dict instead of returning something
    
    return {re.search(r'Popularity\sin\s(\d{4})', ingest).group(1):{"Male": boy, "Female": girl}}


def output_names(db,count=10):
        if db: # Output the names by Year / Gender in alphabetical order
            for year in db.keys():
                    print(f'\nYear: {year}')
                    for gender in db[year]:
                        print(f'\n\tGender: {gender}')
                        for name in sorted(db[year][gender], key=str.lower)[:count]: # only displaying the first 10
                            print(f'\t\t{name}: {db[year][gender][name]}')


def name_trend(name,gender,db):
    print(f'\n\n{name}-') #check the popularity of a specific name over time
    for year in db.keys():
        try:
            print(f'Year: {year} Rank: {db[year][gender][name]}')
        except:
            print("Name not found")


def main():
    global names
    names = { # before writing any other code, a data structure was decided
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

    print('Baby Name Popularity Parser')
    args = sys.argv[1:]
    
    if not args: # No arguments returns a list of files available for parsing then exits
        print(f'Current working directory is: {os.getcwd()}')
        print(f'Specify one or more of the following files:')
        [print(name) for name in what_files()]
        print('Or "--all" to recurse the data/ directory')
        exit()
    
    if args[0] == '--all': # "--all" walks the /data directory and returns all files
        print("You want the whole enchalada")
        files = os.listdir(path='data/')
        args = [] # need it clean for the new list of files
        for item in files:
            args.append('data/' + item)
        
    for filename in args: # can pass more than one filename
        year_add = baby_names_parser(filename)
        names.update(year_add)
    # print(names)

    output_names(names,count=50)

    # if names: # Output the names by Year / Gender in alphabetical order
    #     for year in names.keys():
    #         print(f'\nYear: {year}')
    #         for gender in names[year]:
    #             print(f'\n\tGender: {gender}')
    #             for name in sorted(names[year][gender], key=str.lower)[:50]: # only displaying the first 10
    #                 print(f'\t\t{name}: {names[year][gender][name]}')

    name_trend("Noah","Male",names)
    
    # print('\n\nNoah-') #check the popularity of a specific name over time
    # for year in names.keys():
    #     try:
    #         print(f'Year: {year} Rank: {names[year]["Male"]["Noah"]}')
    #     except:
    #         print("Name not found")

if __name__ == '__main__':
    main()