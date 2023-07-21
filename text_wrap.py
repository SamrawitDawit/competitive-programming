import textwrap

def wrap(string, max_width):
    while string:
        if len(string) < max_width:
            return string
        else:
            print (string[:max_width], end ='\n')
            return wrap(string[max_width:], max_width)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
