import React, { useState } from 'react'
import "./menubar.css"
import axios from 'axios'

const Menubar = () => {
    const [url1, setUrl1] = useState("")
    const [url2, setUrl2] = useState("")
    const [loading, setLoading] = useState(false)
    const [isSubmitted, setIsSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault()
        const urls = [url1, url2].filter(url => url.trim() !== '')

        if (urls.length === 0) {
            alert('Please enter at least one URL')
            return
        }

        try {
            setLoading(true)
            const res = await axios.post("http://127.0.0.1:8000/api/process_url", { urls: urls })
            console.log(res)
        } catch (error) {
            console.log(error)
        }
        finally {
            setLoading(false)
            setIsSubmitted(true)
        }
    }

    return (
        <div>
            <div className="section-header">
                <h2 className="section-title">Add News Sources</h2>
                <p className="section-subtitle">Enter URLs to analyze and search through</p>
            </div>
            
            <form className="menu-form" onSubmit={handleSubmit}>
                <div className="input-group">
                    <label htmlFor="input1">News URL 1:</label>
                    <input
                        onChange={(e) => setUrl1(e.target.value)}
                        type="url"
                        id="input1"
                        name="input1"
                        placeholder="https://example.com/article" />
                </div>

                <div className="input-group">
                    <label htmlFor="input2">News URL 2:</label>
                    <input
                        onChange={(e) => setUrl2(e.target.value)}
                        type="url"
                        id="input2"
                        name="input2"
                        placeholder="https://example.com/article" />
                </div>

                <button type="submit" disabled={loading}>
                    {loading ? 'Processing...' : 'Process URLs'}
                </button>
            </form>
            
            <div className="loading-container">
                {loading && (
                    <div className="loading">
                        <div className="spinner"></div>
                        <p>Processing your URLs...</p>
                    </div>
                )}
                {!loading && isSubmitted && <div className="message">✅ URLs processed successfully! You can now search.</div>}
            </div>
        </div>
    )
}

export default Menubar
