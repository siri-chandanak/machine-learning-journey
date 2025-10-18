# NLP & Generative AI Foundations

## Overview
Phase 3 focuses on **Natural Language Processing (NLP)** and **Generative AI (LLMs)**. The goal is to build a strong foundation in text processing, embeddings, sequence models, transformers, and retrieval-augmented generation (RAG) pipelines. By the end of this phase, you will be able to preprocess text, implement embeddings, fine-tune LLMs, and build AI-powered search/chat systems using vector search.

---

## Objectives
- Learn text preprocessing techniques: tokenization, stemming, lemmatization, stopword removal.
- Understand and implement vector representations: Bag of Words, TF-IDF, Word2Vec, GloVe, FastText.
- Implement sequence models: RNN, LSTM, BiLSTM, Attention mechanisms.
- Understand Transformer architecture and fine-tune LLMs (BERT, RoBERTa, GPT-2/3) for NLP tasks.
- Learn vector search and build Retrieval-Augmented Generation (RAG) pipelines using FAISS, Pinecone, or Chroma.
- Integrate embeddings with LLMs to create intelligent retrieval systems.

---

## Weekly Breakdown

### NLP Basics -- NLP_Basics.ipynb
- **Topics**
  - Text preprocessing: tokenization, stemming, lemmatization, lowercase conversion, stopwords removal.
  - Bag of Words (BoW) and TF-IDF vectorization.
  - Text similarity: cosine similarity, Euclidean distance.
- **Hands-on**
  - Preprocess IMDB reviews, news articles, or your own dataset.
  - Convert text to BoW and TF-IDF features.
  - Compute similarity between text samples.

### Word Embeddings -- Word_Embeddings.ipynb
- **Topics**
  - Word2Vec (CBOW, Skip-gram)
  - GloVe embeddings
  - FastText embeddings (subword information)
- **Hands-on**
  - Train Word2Vec embeddings on your dataset using `gensim`.
  - Visualize embeddings using PCA or t-SNE.
  - Use embeddings in a classification task (e.g., sentiment analysis).

### Sequence Models -- Sequence_Models.ipynb
- **Topics** 
  - Vanilla RNN, LSTM, GRU
  - BiLSTM for sequence modeling
  - Attention mechanisms
- **Hands-on**
  - Build an LSTM-based sentiment classifier.
  - Implement BiLSTM for sequence classification.
  - Add attention layers for improved performance.

### Transformers & LLMs -- Transformers_LLMs.ipynb
- **Topics**
  - Transformer architecture: encoder, decoder, self-attention, positional encoding.
  - Hugging Face Transformers: BERT, RoBERTa, GPT-2/3.
  - Fine-tuning LLMs for classification, summarization, and QA.
- **Hands-on**
  - Fine-tune BERT on a text classification dataset.
  - Summarize text using T5.
  - Build a QA system using DistilBERT or BERT.

### Vector Search & RAG -- Vector_Search_RAG.ipynb
- **Topics**
  - Vector databases: FAISS, Pinecone, Chroma.
  - Embedding models: OpenAI, Hugging Face, GoogleAI.
  - Retrieval-Augmented Generation (RAG) pipelines.
- **Hands-on**
  - Store embeddings in FAISS or Pinecone.
  - Build a simple RAG-based QA bot:
    - Index documents using embeddings.
    - Perform search using query embeddings.
    - Generate answers with GPT-3 or another LLM.
  - Experiment with hybrid search: keyword + vector search.

---

## Tools & Libraries
- **Python:** `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- **NLP:** `nltk`, `spaCy`, `gensim`, `Hugging Face Transformers`
- **Deep Learning:** `TensorFlow`, `Keras`, `PyTorch`
- **Vector Search:** `FAISS`, `Pinecone`, `Chroma`
- **Visualization:** `TSNE`, `PCA`
- **Datasets:** IMDB reviews, 20 Newsgroups, custom text datasets

---

## Expected Outcomes
By the end of Phase 3, you should be able to:
1. Clean and preprocess text for ML and NLP tasks.
2. Represent text using embeddings and vectorization techniques.
3. Build and fine-tune sequence models and transformer-based LLMs.
4. Integrate vector search with LLMs to create intelligent retrieval systems.
5. Implement end-to-end RAG pipelines for real-world applications like QA chatbots or AI search engines.