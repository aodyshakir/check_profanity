import urllib.request
import urllib.parse

def read_text():
    quotes = open("C:\movie_quotes\movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)


# and change the function “check_profanity” to the following :

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check))

    output = connection.read()
    print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert!")
    elif b"false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document properly")

read_text()
