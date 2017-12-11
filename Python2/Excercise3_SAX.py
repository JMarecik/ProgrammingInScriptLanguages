import xml.sax


class XMLBookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print("________BOOK________")
            ids = attributes["id"]
            print("ID: ", ids)

    def endElement(self, tag):
        if self.CurrentData == "author":
            print("Author: ", self.author)
        elif self.CurrentData == "title":
            print("Title: ", self.title)
        elif self.CurrentData == "genre":
            print("Genre: ", self.genre)
        elif self.CurrentData == "price":
            print("Price:", self.price)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "genre":
            self.genre = content
        elif self.CurrentData == "price":
            self.price = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = XMLBookHandler()
parser.setContentHandler(Handler)
parser.parse("books.xml")
