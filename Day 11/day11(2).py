#
reading_list = []
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    reading_list.append({
        "title": title,
        "author": author,
        "year": year
    })

def show_books():
    for book in reading_list:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})")

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        show_books()
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    selected_option = input(menu_prompt).strip().lower()

