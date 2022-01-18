import wikipediaapi
import time

while True:

    wiki_wiki = wikipediaapi.Wikipedia('en')

    print("page name?")

    x = input()

    page_py = wiki_wiki.page(x)

    print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True


    time.sleep(1)

    print("page name?")

    y = input()

    page_py = wiki_wiki.page(y)

    print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %s" % page_py.summary[0:999999999999])
    # Page - Summary: Python is a widely used high-level programming language for

    input("Press Enter to restart...")