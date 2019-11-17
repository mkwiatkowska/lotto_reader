import urllib.request as ur


DUZY_LOTEK = 'https://app.lotto.pl/wyniki/?type=dl'
LOTTO_PLUS = 'https://app.lotto.pl/wyniki/?type=lp'


def get_content(url_):
    '''opens url and gets the content from the website
    returns content in bytes, *results need to be decoded
    '''
    with ur.urlopen(url_) as content_:
        return content_.read()


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
    removed_ = remove_delimiters(decode_content(get_content(url)), '\n')
    date = extract_date(removed_)
    numbers = convert_sort_results(removed_)
    numbers_string = list_to_string(numbers)
    return date + '\n' + numbers_string


def get_newest_numbers(*args):
    for argument_ in args:
        print(work_loop(argument_))

get_newest_numbers(DUZY_LOTEK, LOTTO_PLUS)
print('Hope you liked it :)')
