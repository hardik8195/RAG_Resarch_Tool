import React, { useState } from 'react'
import "./main.css"
import axios from 'axios'
import {Link, Links} from 'react-router-dom'

const Main = () => {
  const [q, setQ] = useState("")
  const [message,setMessage] = useState("")
  const [loading, setLoading] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [source,setSource] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      setLoading(true)
      const res = await axios.post("http://127.0.0.1:8000/api/predict", { q: q })
      setMessage(res.data.answer)
      setSource(res.data.sources)
      console.log(res.data.sources)

    } catch (error) {
      console.log(error)
    }
    finally{
      setLoading(false)
      setIsSubmitted(true)
    }
  }

  return (
    <div>
      <form className="main-form" onSubmit={handleSubmit}>
        <label htmlFor="mainInput">Ask a question about your news sources:</label>
        <input 
          required 
          onChange={(e) => setQ(e.target.value)} 
          type="text" 
          id="mainInput" 
          name="mainInput" 
          placeholder="e.g., What are the main points discussed in the articles?" 
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </form>
      
      <div className="loading-container">
        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Processing your request...</p>
          </div>
        )}
        
        {!loading && isSubmitted && message && (
          <div className="results-container">
            <div className="result-card">
              <div className="result-text">{message}</div>
              {source && source.length > 0 && (
                <div className="sources-container">
                  <div className="sources-title">Sources:</div>
                  {source.map((url, index) => (
                    <a 
                      key={index} 
                      href={url} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="source-link"
                    >
                      {url}
                    </a>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Main
