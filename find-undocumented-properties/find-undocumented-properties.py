#! usr/bin/python python3

import sys
import re
import webbrowser
import requests # For downloading content from the web
import bs4 # 'Beautiful Soup 4', for parsing HTML

def GetHTML(url):
    if not ".htm" in url:
        url = url + "/index.html" # Automatically append /index.html if specified URL doesn't contain .htm(l) file
    try:
        res = requests.get(url) print('HTTP response code: ' + str(res.status_code))
        print('Characters: ' + str(len(res.text)))
        html = bs4.BeautifulSoup(res.text, 'html.parser')
    except:
        print('Couldn\'t open "' + url + '".')
        res.raise_for_status()
    return html

def GetScope(html):
    scope = input('Enter the CSS selector for the scope: ')
    print(scope)
    print(html.select(scope))
    matches = len(html.select(scope))
    print('HTML elements matching selector "' + scope + '": ' + str(matches))
    return scope

def GetCodeProperties(html, scope):
    propertyselector = (scope + ' ' + input('Enter CSS selector for code sample property: '))
    print(propertyselector)
    matches = len(html.select(propertyselector))
    print('HTML elements matching selector "' + propertyselector + '": ' + str(matches))
    return

# def GetCode

# Open specified web page
# def OpenWebPage(subpage):
#     try:
#         res = requests.get('https://developers.line.biz/en/reference/' + subpage + '/index.html')
#         print('HTTP response code: ' + str(res.status_code))
#         print('Characters: ' + str(len(res.text)))
#         print('Sample: \n' + res.text[:100])
#         HTMLraw = res.text
#         ParseHTML(HTMLraw)
#     except:
#         print('Couldn\'t open subpage "' + subpage + '".')
#         res.raise_for_status()
#     return

# Parse HTML
# def ParseHTML(HTMLraw):
#     try:
#         soup = bs4.BeautifulSoup(HTMLraw, 'html.parser')
#         GetExampleRequest(soup)
#     except:
#         print('Problem parsing HTML.')
#     return

# Find example request
# def GetExampleRequest(soup):
#     try:
#         scope = soup.select('div.reference-with-code:nth-child(54)')
# #        IndexRequestProperties(scope)
#     except:
#         print('Problem getting specified element.')
#     return


# Index properties in sample request
# def IndexRequestProperties(scope):
#     range = len(scope.find_all('span.property'))
#     print(range)
#     return

# Index properties in properties table
def IndexTableProperties():

    return

# Compare request and table indeces
def CompareRequestAndTables():

    return

# Print list of undocumented properties
def ListUndocumentedProperties():

    return

url = input('Enter a URL: ')
html = GetHTML(url)
scope = GetScope(html)
codeproperties = GetCodeProperties(html, scope)
# referenceproperties = GetReferenceProperties(html, scope)
# result = CompareRequestAndTables()



# print('Sample: \n' + res.text[:100])

# Get command line arguments
# sys.argv
# if len(sys.argv) > 1:
#    subpage = str(sys.argv[1])
#    OpenWebPage(subpage)
# else:
#    print('Specify one of these pages:')
#    print('- messaging-api')
