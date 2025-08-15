# News Research Tool 🔍

![News Research Tool Interface](https://img.shields.io/badge/Status-Active-brightgreen) ![React](https://img.shields.io/badge/React-18.3.1-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Python-green) ![AI](https://img.shields.io/badge/AI-Powered-orange)

An AI-powered tool that helps users analyze news articles and get intelligent answers to their questions with source attribution.

## 📸 Screenshots

![Application Interface](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=News+Research+Tool+Interface)

*Note: Replace the placeholder image above with an actual screenshot of your application*

## 🌟 Features

- **URL Processing**: Extract and analyze content from news article URLs
- **AI-Powered Q&A**: Get intelligent answers based on processed articles
- **Source Attribution**: Track and display sources for all answers
- **Real-time Processing**: Immediate feedback with loading states
- **Responsive Design**: Works seamlessly on desktop and mobile

## 🛠️ Tech Stack

### Frontend
- React (v18.3.1)
- Vite
- Axios for API calls
- CSS for styling

### Backend
- FastAPI
- LangChain for LLM operations
- FAISS Vector Store
- Groq LLM Integration
- HuggingFace Embeddings



# News Research Tool - Flow Points 📋

### 1. Initial URL Processing 📥
User inputs URLs in left panel
Frontend sends URLs to /api/process_url endpoint
Backend receives URLs for processing
   - Context retrieval
   - LLM-powered answer generation
   - Source attribution


### 2. Document Processing Pipeline 📄
```python
# Key Steps:
1. URL Content Extraction (UnstructuredURLLoader)
2. Text Splitting (RecursiveCharacterTextSplitter)
   - Chunk size: 300 characters
   - Overlap: 50 characters
3. Embedding Generation (HuggingFace)
4. Vector Storage (FAISS)
5. Save to disk for later use
```


### 3. Question Processing Pipeline 🔍
```python
# Flow:
1. User submits question
2. Load vector store
3. Retrieve relevant context
4. Generate answer using LLM
5. Return answer with sources
```


### 4. Key Components 🛠️
```
Frontend:
- React components (Main.jsx, Menubar.jsx)
- Axios for API calls
- Loading states
- Error handling

Backend:
- FastAPI endpoints
- LangChain integration
- Groq LLM
- FAISS vector store
```



### 5. Data Flow Steps 📊
```
1. Document Flow:
   URL → Text → Chunks → Embeddings → Storage

2. Query Flow:
   Question → Vector Search → Context → LLM → Response
```

### 6. User Interface Flow 👤
```
1. Left Panel:
   - URL input fields
   - Process button
   - Processing status

2. Right Panel:
   - Question input
   - Answer display
   - Source attribution
   - Loading indicators
```





