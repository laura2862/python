import re
def match_result(data):
    if data:
        print('matched!')
        print(data.group())
    else:
        print('un-matched!')

data=re.match('<(?P<ht>[a-zA-Z1-6]+)><(?P<h>[a-zA-Z1-6]+)>.*</(?P=h)></(?P=ht)>' , '<html><h1>welcome!</h1></html>')
match_result(data)