# UBS Coding Challenge 2025

### 🎯 **Features**
- **View Challenges**: Browse available coding challenges with difficulty levels and point values
- **Submit Solutions**: Code editor with syntax highlighting and real-time validation
- **Track Progress**: Monitor your submission status and scores
- **Live Leaderboard**: See real-time rankings and compete with other participants

### 🚀 **Developer-Friendly**
- **No Build Process**: Pure HTML/CSS/JS - works immediately
- **CORS Enabled**: Ready for cross-origin API requests
- **Error Handling**: Comprehensive error messages and loading states
- **Keyboard Shortcuts**: Ctrl+1-4 for quick tab navigation

## 🌐 Quick Start

### Prerequisites
- UBS Coding Challenge Flask server running on `http://localhost:5000`
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Option 1: Windows Batch Script (Recommended)
```bash
# Double-click this file
start_frontend.bat
```

### Option 2: Python Script
```bash
python start_frontend.py
```

### Option 3: Custom Port
```bash
python start_frontend.py 8081
```

### Option 4: Simple HTTP Server
```bash
# If you have Python installed
python -m http.server 8080

# If you have Node.js installed
npx serve .
```

🌐 **Access the frontend at:** http://localhost:8080

## 🎮 How to Use

### 1. **Set Your Name**
- Enter your participant name in the header
- Click "Set Name" to identify your submissions

### 2. **Browse Challenges**
- View all available challenges on the "Challenges" tab
- Filter by difficulty: Easy, Medium, Hard
- Click "Solve This" to jump directly to submission

### 3. **Submit Solutions**
- Select a challenge from the dropdown
- Write your Python solution in the code editor
- Click "Submit Solution" to send for validation

### 4. **Track Your Progress**
- Check "My Submissions" tab for submission history
- View status: Accepted, Rejected, Pending, Error
- See scores and timestamps for each submission

### 5. **Compete on Leaderboard**
- Monitor real-time rankings on "Leaderboard" tab
- See total scores and challenges solved
- Auto-refreshes every 30 seconds

## 🔧 Technical Details

### **Frontend Stack**
- **HTML5**: Semantic structure with accessibility features
- **CSS3**: Modern flexbox/grid layout with animations
- **Vanilla JavaScript**: No frameworks - maximum compatibility
- **Font Awesome**: Professional icons
- **Google Fonts**: Clean Inter typography

### **API Integration**
- **RESTful API calls** to Flask backend
- **JSON data exchange** for all operations
- **Error handling** with user-friendly messages
- **Real-time updates** and status monitoring

### **Browser Compatibility**
- ✅ Chrome 70+
- ✅ Firefox 65+
- ✅ Safari 12+
- ✅ Edge 79+

## 📱 Features Overview

### **Challenges Tab**
```javascript
GET /api/challenges  // Load all challenges
```
- Grid layout of challenge cards
- Difficulty badges (Easy/Medium/Hard)
- Point values and descriptions
- Quick "Solve This" buttons

### **Submit Solution Tab**
```javascript
POST /api/submit  // Submit solution
```
- Challenge selection dropdown
- Large code textarea with syntax hints
- Real-time validation feedback
- Success/error result display

### **My Submissions Tab**
```javascript
GET /api/submissions/{id}  // Get submission details
```
- Chronological submission history
- Status badges with color coding
- Score display and timestamps
- Detailed submission information

### **Leaderboard Tab**
```javascript
GET /api/leaderboard  // Get current rankings
```
- Real-time participant rankings
- Total scores and challenges solved
- Highlighting for current user
- Auto-refresh functionality

## 🎨 Customization

### **Color Scheme**
Edit `styles.css` to change colors:
```css
:root {
    --primary-color: #007bff;
    --success-color: #28a745;
    --danger-color: #dc3545;
    --warning-color: #ffc107;
}
```

### **API Endpoint**
Change the API URL in `app.js`:
```javascript
const API_BASE_URL = 'http://your-server:5000';
```

### **Auto-refresh Interval**
Modify leaderboard refresh rate:
```javascript
setInterval(() => {
    // Current: 30 seconds
}, 30000);
```

## 🔧 Development

### **File Structure**
```
web_frontend/
├── index.html          # Main HTML structure
├── styles.css          # All CSS styles
├── app.js             # JavaScript application logic
├── start_frontend.py   # Python web server
├── start_frontend.bat  # Windows batch script
└── README.md          # This file
```

### **Adding New Features**
1. **HTML**: Add new elements to `index.html`
2. **CSS**: Style in `styles.css`
3. **JavaScript**: Add logic to `app.js`
4. **API**: Ensure Flask backend supports the feature

### **Debugging**
- Open browser Developer Tools (F12)
- Check Console for JavaScript errors
- Monitor Network tab for API requests
- Verify Flask server is running and accessible

## 🌟 Advanced Features

### **Keyboard Shortcuts**
- `Ctrl+1`: Switch to Challenges tab
- `Ctrl+2`: Switch to Submit Solution tab
- `Ctrl+3`: Switch to My Submissions tab
- `Ctrl+4`: Switch to Leaderboard tab

### **Real-time Updates**
- ✅ Leaderboard auto-refreshes every 30 seconds
- ✅ Server status monitoring with connection indicators
- ✅ Last update timestamp in status bar

### **Error Handling**
- ✅ Network connection failures
- ✅ Invalid API responses
- ✅ Form validation errors
- ✅ Server unavailable scenarios

## 🚀 Production Deployment

### **Static File Hosting**
Deploy to any static hosting service:
- **Netlify**: Drag and drop the `web_frontend` folder
- **Vercel**: Connect to your Git repository
- **GitHub Pages**: Push to a GitHub repository
- **AWS S3**: Upload as static website

### **CORS Configuration**
Ensure your Flask server allows the frontend domain:
```python
CORS(app, origins=['http://your-frontend-domain.com'])
```

### **Environment Variables**
For production, update the API URL:
```javascript
const API_BASE_URL = process.env.API_URL || 'http://localhost:5000';
```

## 🤝 Integration with Flask API

### **Required API Endpoints**
The frontend expects these Flask endpoints:
```
GET  /health              # Server health check
GET  /api/challenges      # List challenges
GET  /api/challenges/{id} # Get specific challenge
POST /api/submit          # Submit solution
GET  /api/submissions/{id} # Get submission details
GET  /api/leaderboard     # Get rankings
GET  /api/status          # API statistics
```

### **Expected Response Formats**
All responses should be JSON with consistent structure:
```json
{
  "success": true,
  "data": {...},
  "timestamp": "2025-09-05T15:30:00Z"
}
```

## 🆘 Troubleshooting

### **Common Issues**

1. **"Failed to connect to server"**
   - Ensure Flask server is running on port 5000
   - Check if `http://localhost:5000/health` returns data

2. **"CORS error"**
   - Verify Flask server has CORS enabled
   - Check browser console for specific CORS errors

3. **"Submissions not showing"**
   - Ensure you've set your participant name
   - Check that submissions were successful

4. **"Leaderboard empty"**
   - Submit at least one solution first
   - Check Flask server logs for errors

### **Debug Mode**
Enable debug logging by adding to browser console:
```javascript
localStorage.debug = true;
```
