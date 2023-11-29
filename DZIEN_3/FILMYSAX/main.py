import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""

    def startElement(self, tag, attrs):
        self.current_data = tag
        if tag == "film":
            print("_______________ FILM __________________")

    def endElement(self, tag):
        if self.current_data == "id_filmu":
            print(f'identyfikator filmu: {self.id}')
        elif self.current_data == "tytul":
            print(f'tytuł filmu: {self.tytul}')
        elif self.current_data == "rok":
            print(f'rok produkcji filmu: {self.rok}')
        elif self.current_data == "kraj":
            print(f'kraj produkcji filmu: {self.kraj}')
        elif self.current_data == "czas_trwania":
            print(f'czas trwania filmu: {self.czas_t}')
        elif self.current_data == "gatunek":
            print(f'gatunek filmu: {self.gatunek}')

    def characters(self, content):
        if self.current_data == "id_filmu":
            self.id = content
        elif self.current_data == "tytul":
            self.tytul = content
        elif self.current_data == "rok":
            self.rok = content
        elif self.current_data == "kraj":
            self.kraj = content
        elif self.current_data == "czas_trwania":
            self.czas_t = content
        elif self.current_data == "gatunek":
            self.gatunek = content




parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)

handler = UchwytFilmu()
parser.setContentHandler(handler)
parser.parse("filmy.xml")






