### Backend (Flask):
- **Main file**: `flask_app/routes.py`
- **Templates**: Lines 310+ contain template functions you can copy

### Frontend (HTML/JavaScript):
- **HTML tab**: `web_frontend/index.html`
- **JavaScript functions**: `web_frontend/app.js` (functions starting with `fetch...`)

## 🔧 Step-by-Step Integration Process

### Step 1: Add Backend Endpoint (Flask)

1. **Open**: `flask_app/routes.py`
2. **Find**: Line ~310 (template functions section)
3. **Copy**: One of the template functions (uncomment and modify)
4. **Customize**:

```python
@api_bp.route('/external/your-api-name', methods=['GET'])
def get_your_api_data():
    """Your API description"""
    try:
        # Replace with your external website URL
        response = requests.get('https://your-website.com/api/endpoint', timeout=10)
        response.raise_for_status()
        
        # Process the response
        data = response.json()
        
        # Return formatted data
        return jsonify({
            'status': 'success',
            'source': 'your-website.com',
            'data': data,
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Your API error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Failed to fetch data: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500
```

### Step 2: Add Frontend Function (JavaScript)

1. **Open**: `web_frontend/app.js`
2. **Find**: Line ~450 (External API Functions section)
3. **Add** your function:

```javascript
async function fetchYourApiData() {
    const resultsDiv = document.getElementById('your-api-results');
    showApiLoading(resultsDiv, 'Fetching data from your website...');
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/external/your-api-name`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, 'Your API Results', data);
        } else {
            showApiError(resultsDiv, data.message || 'Failed to fetch data');
        }
    } catch (error) {
        console.error('Your API error:', error);
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}
```

### Step 3: Add Frontend UI (HTML)

1. **Open**: `web_frontend/index.html`
2. **Find**: Line ~140 (External APIs tab content)
3. **Add** your section:

```html
<div class="api-section">
    <h3><i class="fas fa-your-icon"></i> Your Website Name</h3>
    <p>Description of what this integration does</p>
    <button onclick="fetchYourApiData()" class="btn btn-primary">
        <i class="fas fa-download"></i> Fetch Data
    </button>
    <div id="your-api-results" class="api-results"></div>
</div>
```

## 🎯 Common Integration Patterns

### Pattern 1: Simple GET Request
**Use case**: Fetch public data from an API
**Example**: News articles, public posts, weather data
```python
response = requests.get('https://api.example.com/data', timeout=10)
```

### Pattern 2: Authenticated API
**Use case**: APIs requiring API keys or tokens
**Example**: Private user data, premium services

1. **Add to .env file**:
```
YOUR_API_KEY=your_actual_api_key_here
```

2. **Use in code**:
```python
api_key = os.getenv('YOUR_API_KEY')
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get('https://api.example.com/data', headers=headers, timeout=10)
```

### Pattern 3: POST Request
**Use case**: Send data to external services
**Example**: Submit forms, create records
```python
payload = {'field1': value1, 'field2': value2}
response = requests.post('https://api.example.com/submit', json=payload, timeout=10)
```

## 🌟 Popular APIs to Integrate

### 1. News APIs
- **NewsAPI**: https://newsapi.org/
- **Guardian**: https://open-platform.theguardian.com/

### 2. Weather APIs
- **OpenWeatherMap**: https://openweathermap.org/api
- **WeatherAPI**: https://www.weatherapi.com/

### 3. Finance APIs
- **Alpha Vantage**: https://www.alphavantage.co/
- **CoinGecko**: https://www.coingecko.com/api

### 4. Social Media APIs
- **Reddit**: https://www.reddit.com/dev/api/
- **Twitter**: https://developer.twitter.com/

## ⚠️ Important Security Notes

### 1. API Keys
- **Never** put API keys directly in your code
- **Always** use environment variables (.env file)
- **Add** .env to your .gitignore file

### 2. Allowed Domains
- The custom request endpoint has security restrictions
- Only certain domains are allowed by default
- Modify the `allowed_domains` list in `routes.py` line ~230

### 3. Rate Limiting
- Be aware of API rate limits
- Add caching for frequently requested data
- Handle rate limit errors gracefully

## 🧪 Testing Your Integration

### 1. Test Backend Endpoint
```bash
# Test your new endpoint
curl http://localhost:5000/api/external/your-api-name
```

### 2. Test Frontend
1. Start Flask server: `python start_flask.py`
2. Open `web_frontend/index.html` in browser
3. Click "External APIs" tab
4. Test your new integration

### 3. Debug Issues
- Check browser console for JavaScript errors
- Check Flask terminal for Python errors
- Verify API endpoint URLs and parameters

## 📝 Quick Checklist

- [ ] Added backend endpoint in `flask_app/routes.py`
- [ ] Added frontend function in `web_frontend/app.js`
- [ ] Added UI section in `web_frontend/index.html`
- [ ] Added API keys to `.env` file (if needed)
- [ ] Updated allowed domains (if using custom requests)
- [ ] Tested the integration
- [ ] Added error handling
- [ ] Documented the new feature

## 🆘 Common Issues & Solutions

### Issue: CORS Errors
**Solution**: CORS is already enabled in `flask_app/app.py`

### Issue: API Key Not Working
**Solution**: Check .env file format and restart Flask server

### Issue: Network Timeout
**Solution**: Increase timeout value or check external API status

### Issue: JSON Parsing Error
**Solution**: Check if external API returns valid JSON

## 📖 Example Integration: GitHub API

Here's a complete example of integrating GitHub API:

### Backend (`flask_app/routes.py`):
```python
@api_bp.route('/external/github-user', methods=['GET'])
def get_github_user():
    """Fetch GitHub user information"""
    try:
        username = request.args.get('username', 'octocat')
        response = requests.get(f'https://api.github.com/users/{username}', timeout=10)
        response.raise_for_status()
        
        user_data = response.json()
        
        return jsonify({
            'status': 'success',
            'source': 'api.github.com',
            'user': {
                'name': user_data.get('name'),
                'public_repos': user_data.get('public_repos'),
                'followers': user_data.get('followers'),
                'avatar_url': user_data.get('avatar_url')
            },
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': f'GitHub API error: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500
```

### Frontend (`web_frontend/app.js`):
```javascript
async function fetchGitHubUser() {
    const username = document.getElementById('github-username').value.trim() || 'octocat';
    const resultsDiv = document.getElementById('github-results');
    showApiLoading(resultsDiv, `Fetching GitHub user: ${username}...`);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/external/github-user?username=${encodeURIComponent(username)}`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, 'GitHub User Info', data);
        } else {
            showApiError(resultsDiv, data.message || 'Failed to fetch user');
        }
    } catch (error) {
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}
```

### HTML (`web_frontend/index.html`):
```html
<div class="api-section">
    <h3><i class="fab fa-github"></i> GitHub User Info</h3>
    <p>Get information about any GitHub user</p>
    <div class="form-group">
        <input type="text" id="github-username" placeholder="Enter GitHub username" value="octocat">
        <button onclick="fetchGitHubUser()" class="btn btn-primary">
            <i class="fab fa-github"></i> Get User Info
        </button>
    </div>
    <div id="github-results" class="api-results"></div>
</div>
```

This guide should help you integrate any external website or API into your application!
