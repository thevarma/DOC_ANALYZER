# Entry point for the doc analyzer
from analyzer.analyzer import analyze_doc

if __name__ == '__main__':
    url = 'https://help.moengage.com/hc/en-us/articles/1234567890'
    results = analyze_doc(url)
    print(results)