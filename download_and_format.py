import urllib.request as ur 


duzy_lotek = 'https://app.lotto.pl/wyniki/?type=dl'
lotto_plus = 'https://app.lotto.pl/wyniki/?type=lp'


def get_content(url_):
    '''opens url and gets the content from the website
    returns content in bytes, *results need to be decoded 
    '''
    with ur.urlopen(url_) as w:
        return w.read()


def decode_content(content_):
    '''decodes the content, 
    uses utf-8 as it is the most commont type of coding,
    returns a string
    '''
    return content_.decode("utf-8")


def remove_delimiters(string_, delimiter_):
    '''takes a string and removes given delimiter,
    returns list of strings
    '''
    return string_.split(delimiter_)


def extract_date(content_list):
    '''takes a list of strings, in our case, 
    date is always at the very beginning of the list,
    returns string with date
    '''
    return content_list[0]


def convert_sort_results(content_list):
    '''extracts the results and converts them from str to int,
    so it can sort them asc,
    returns sorted list of ints
    '''
    results = content_list[1:-1]
    converted = []
    for each in results:
        converted.append(int(each))
    converted.sort()
    return converted


def list_to_string(content_list):
    #return str(content_list)[1:-1] 
    return ', '.join(str(x) for x in content_list)


def work_loop(url):
    r = remove_delimiters(decode_content(get_content(url)), '\n')
    date = extract_date(r)
    numbers = convert_sort_results(r)
    nn = list_to_string(numbers)
    return date + '\n' + nn


def get_stuff_done(*args):
    for a in args:
        print(work_loop(a))

get_stuff_done(duzy_lotek, lotto_plus)

