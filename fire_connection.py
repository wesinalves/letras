import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FireConnection:
    '''Classe to represent music entity in dataset'''
    def __init__(self):
        #self.read_config()
        cred = credentials.Certificate('hope.json') # service account json goes here
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def save_music(self, title, author, lyrics, year):
        doc_ref = self.db.collection(u'musicas')
        music = {u'titulo': title,
                u'autor': author,
                u'letra': lyrics,
                u'ano': year
                }
        try:
            doc_ref.add(music)
            print(title + " has been saved!")
        except:
            print("Something goes wrong on firebase!")
    
    def get_musics(self):
        doc_ref = self.db.collection(u'musicas')
        docs = doc_ref.stream()
        return docs

    def get_music(self, title):
        doc_ref = self.db.collection(u'musicas')
        docs = doc_ref.where(u'titulo', u'==', title).stream()
        return docs


        
        
    