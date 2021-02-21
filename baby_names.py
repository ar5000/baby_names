import re, sys, os

# def scrub_html(text):
#     return re.sub(r'</?.*?>', '', text)

# text = "<p class>hello hi</p class><a> new text </a>"

# print(scrub_html(text))

def baby_names_parser(filename):
    print(filename)
    # with open(filename, 'r',encoding = 'utf-8') as f:
    #     ingest = f.read()

    # tickers = re.findall(r'[A-Z]{1,4}:\s?\d+\.\d{2,}', text)    


    

def main():

    names = {
    '2004':{
        'boy':{
            "Alex": 4,
            "Graham": 3,
            "Kyle": 1,
            "Miguel": 5,
            "Steven": 2},
        'girl':{
            "Judy": 3,
            "Diane": 2,
            "Maria": 1,
            "Sarah": 5,
            "Katie": 4}
        },
    '2005':{
        'boy':{
            "Alex": 3,
            "Graham": 4,
            "Kyle": 1,
            "Miguel": 2,
            "Steven": 5},
        'girl':{
            "Judy": 2,
            "Diane": 1,
            "Maria": 3,
            "Sarah": 5,
            "Katie": 4}
        }
    }

    print('Baby Name Parser')
    args = sys.argv[1:]
    if not args:
        print(f'Current working directory is: {os.getcwd()}')
        print(f'Files available for parsing are:')
        [print(f'data/{name}') for name in os.listdir(path='data/')]

    
    # baby_names_parser()
    
    for filename in args:
        baby_names_parser(filename)

    for year in names.keys():
        print(f'\nYear: {year}')
        for gender in names[year]:
            print(f'\nGender: {gender}')
            for name in sorted(names[year][gender], key=str.lower):
                print(f'{name}: {names[year][gender][name]}')

if __name__ == '__main__':
    main()