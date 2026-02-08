import os,re
from langdetect import detect
from sentence_transformers import SentenceTransformer
import faiss

WORD=re.compile(r"[a-zA-Z]+")

class PoetryAI:

    def __init__(self):
        self.model=SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.texts=[]
        self.index=None

    def load_poems(self,f):
        poems=[]
        for x in os.listdir(f):
            if x.endswith(".txt"):
                poems.append(open(f+"/"+x,encoding="utf8").read())

        emb=self.model.encode(poems,normalize_embeddings=True)
        self.index=faiss.IndexFlatIP(emb.shape[1])
        self.index.add(emb)
        self.texts=poems

    def analyze(self,text,k):
        q=self.model.encode([text],normalize_embeddings=True)
        s,i=self.index.search(q,k)

        return {
            "language":detect(text),
            "similar":[float(x) for x in s[0]]
        }
