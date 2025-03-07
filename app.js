import { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const generateResponse = async () => {
    if (!prompt.trim()) {
      setError('Please enter a question for the Game Master');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response from the GM');
      }

      const data = await response.json();
      setResponse(data.response);
    } catch (error) {
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>D&D Game Master</h1>
      
      <div className="input-section">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt..."
          disabled={isLoading}
        />
        
        <button 
          onClick={generateResponse}
          disabled={isLoading}
        >
          {isLoading ? 'Consulting the Scrolls...' : 'Ask the GM'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="response-section">
        <h2>Response:</h2>
        <div className="response-content">
          {isLoading ? (
            <div className="loading-animation">
              <div className="d20"></div>
              <div className="d20"></div>
              <div className="d20"></div>
            </div>
          ) : (
            <p>{response}</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;