from seoanalyzer import analyze


def run():
    output = analyze('https://www.sethserver.com/tests/utf8.html')
    print(output)
