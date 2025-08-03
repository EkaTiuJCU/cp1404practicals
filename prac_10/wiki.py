import wikipedia

def main():
    print("Wikipedia Search (enter blank to quit)\n")
    while True:
        search_phrase = input("Enter page title: ").strip()
        if not search_phrase:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"\n{page.title}")
            print(wikipedia.summary(search_phrase, sentences=2))  # shorter summary
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(search_phrase))

if __name__ == '__main__':
    main()