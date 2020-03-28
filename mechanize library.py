import mechanize
def ViewPage(url):
    browser = mechanize.Browser()
    page = browser.open(url)
    source_code = page.read()
    print (source_code)
ViewPage('https://www.kuk.ac.in/')
