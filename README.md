# PoetryMind — AI Poetry Analyzer

PoetryMind is an original personal project that explores how artificial intelligence can understand poetry through meaning rather than keywords.
The system analyzes any poem by detecting its language and finding semantically similar poems using modern NLP techniques and vector search.
Built entirely as a solo project, PoetryMind combines machine learning with a minimal web interface to demonstrate semantic text understanding in a creative domain.

✨ Features
🌍 Automatic language detection
🧠 Semantic similarity between poems
⚡ Fast vector search using FAISS
🌐 REST API powered by FastAPI
🖥 Simple browser-based interface

🔬 How It Works

Poems are converted into semantic embeddings using a multilingual transformer model.
These embeddings are stored in a FAISS index for fast similarity search.
When a user submits a poem, the system:
1-Detects its language
2-Generates its embedding
3-Searches for the most similar poems
4-Returns similarity scores via API
5-This allows comparison based on meaning, even across different languages.

## 🧑‍💻 Author

Designed and built entirely by *A.Ceno* as an independent AI/NLP exploration project.
