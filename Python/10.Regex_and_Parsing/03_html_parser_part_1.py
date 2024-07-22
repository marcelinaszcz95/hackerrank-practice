# Problem: https://www.hackerrank.com/challenges/html-parser-part-1/problem
# Score: 30

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value}")
        
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
        
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value}")
    

parser = MyHTMLParser()

lines = []
n = int(input())
for _ in range(n):
    line = input()
    lines.append(line)
    
parser.feed(''.join(lines))