from xml.dom import minidom


def show(file):
    doc = minidom.parse(file)
    name = doc.getElementsByTagName("name")[0]
    print(name.firstChild.data)
    books = doc.getElementsByTagName("book")
    for book in books:
            sid = book.getAttribute("id")
            author = book.getElementsByTagName("author")[0]
            title = book.getElementsByTagName("title")[0]
            genre = book.getElementsByTagName("genre")[0]
            price = book.getElementsByTagName("price")[0]
            print("ID: %s, Author: %s, Title: %s, Genre: %s, Price: %s" %
                  (sid, author.firstChild.data, title.firstChild.data, genre.firstChild.data, price.firstChild.data))


show("books.xml")
