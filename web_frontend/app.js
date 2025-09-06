// Configuration
// Auto-detect API base URL based on environment
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5000'  // Development
    : window.location.origin;  // Production (same domain)
let currentParticipant = 'Anonymous';
let challenges = [];
let mySubmissions = [];

// Initialize app when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('UBS Coding Challenge 2025 - Participant Interface Loaded');
    initializeApp();
});

async function initializeApp() {
    updateStatus('Initializing...', 'connecting');
    
    try {
        // Check server health
        await checkServerHealth();
        
        // Load initial data
        await loadChallenges();
        await loadLeaderboard();
        
        updateStatus('Connected', 'connected');
        updateLastUpdate();
        
        console.log('App initialized successfully');
    } catch (error) {
        console.error('Failed to initialize app:', error);
        updateStatus('Disconnected', 'error');
        showError('Failed to connect to the challenge server. Please make sure the Flask server is running.');
    }
}

// Server Health Check
async function checkServerHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (!response.ok) throw new Error('Server health check failed');
        
        const data = await response.json();
        console.log('Server health:', data);
        return data;
    } catch (error) {
        console.error('Health check failed:', error);
        throw error;
    }
}

// Tab Management
function showTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Hide all tab buttons
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');
    
    // Load data for specific tabs
    if (tabName === 'leaderboard') {
        loadLeaderboard();
    } else if (tabName === 'status') {
        loadMySubmissions();
    } else if (tabName === 'submit') {
        populateChallengeSelect();
    }
    
    updateLastUpdate();
}

// Participant Management
function setParticipant() {
    const nameInput = document.getElementById('participantName');
    const name = nameInput.value.trim();
    
    if (name && name.length > 0) {
        currentParticipant = name;
        document.getElementById('currentUser').textContent = currentParticipant;
        showSuccess(`Welcome, ${currentParticipant}! You can now submit solutions.`);
        
        // Clear and reload submissions for this participant
        mySubmissions = [];
        loadMySubmissions();
    } else {
        showError('Please enter a valid name');
    }
}

// Challenge Management
async function loadChallenges() {
    try {
        updateStatus('Loading challenges...', 'loading');
        
        const response = await fetch(`${API_BASE_URL}/api/challenges`);
        if (!response.ok) throw new Error('Failed to load challenges');
        
        const data = await response.json();
        challenges = data.challenges;
        
        displayChallenges(challenges);
        populateChallengeSelect();
        
        console.log(`Loaded ${challenges.length} challenges`);
        updateStatus('Connected', 'connected');
    } catch (error) {
        console.error('Error loading challenges:', error);
        showError('Failed to load challenges. Please try again.');
        updateStatus('Error', 'error');
    }
}

function displayChallenges(challengesToShow) {
    const container = document.getElementById('challengesList');
    
    if (!challengesToShow || challengesToShow.length === 0) {
        container.innerHTML = '<div class="empty-state"><i class="fas fa-exclamation-circle"></i><p>No challenges found</p></div>';
        return;
    }
    
    container.innerHTML = challengesToShow.map(challenge => `
        <div class="challenge-card">
            <div class="challenge-header">
                <h3 class="challenge-title">${challenge.title}</h3>
                <span class="difficulty-badge difficulty-${challenge.difficulty}">${challenge.difficulty}</span>
            </div>
            <p class="challenge-description">${challenge.description}</p>
            
            ${challenge.examples ? `
                <div class="examples">
                    <h4>Examples:</h4>
                    ${challenge.examples.map(ex => `
                        <div class="example">
                            <strong>Input:</strong> ${ex.input}<br>
                            <strong>Output:</strong> ${ex.output}
                        </div>
                    `).join('')}
                </div>
            ` : ''}
            
            <div class="challenge-meta">
                <span class="points"><i class="fas fa-star"></i> ${challenge.points} points</span>
                <button onclick="selectChallengeForSubmission(${challenge.id})" class="btn btn-primary">
                    <i class="fas fa-code"></i> Solve This
                </button>
            </div>
        </div>
    `).join('');
}

function filterChallenges() {
    const filter = document.getElementById('difficultyFilter').value;
    const filtered = filter ? challenges.filter(c => c.difficulty === filter) : challenges;
    displayChallenges(filtered);
}

function selectChallengeForSubmission(challengeId) {
    showTab('submit');
    document.getElementById('challengeSelect').value = challengeId;
    
    // Find and display challenge details
    const challenge = challenges.find(c => c.id === challengeId);
    if (challenge) {
        showInfo(`Selected: ${challenge.title} (${challenge.difficulty} - ${challenge.points} points)`);
    }
}

// Solution Submission
function populateChallengeSelect() {
    const select = document.getElementById('challengeSelect');
    select.innerHTML = '<option value="">Choose a challenge...</option>' +
        challenges.map(c => `<option value="${c.id}">${c.title} (${c.difficulty} - ${c.points} pts)</option>`).join('');
}

async function submitSolution() {
    const challengeId = document.getElementById('challengeSelect').value;
    const solution = document.getElementById('solutionCode').value.trim();
    
    if (!challengeId) {
        showError('Please select a challenge');
        return;
    }
    
    if (!solution) {
        showError('Please enter your solution code');
        return;
    }
    
    if (currentParticipant === 'Anonymous') {
        showError('Please set your name first');
        return;
    }
    
    try {
        updateStatus('Submitting solution...', 'loading');
        
        const submissionData = {
            challenge_id: parseInt(challengeId),
            solution: solution,
            participant_name: currentParticipant
        };
        
        const response = await fetch(`${API_BASE_URL}/api/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(submissionData)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showSubmissionResult(result, true);
            
            // Add to local submissions list
            mySubmissions.unshift({
                id: result.submission_id,
                challenge_id: parseInt(challengeId),
                challenge_title: result.challenge_title,
                status: result.status,
                score: result.score,
                submitted_at: result.timestamp
            });
            
            // Clear the form
            document.getElementById('solutionCode').value = '';
            
            updateStatus('Connected', 'connected');
        } else {
            showSubmissionResult(result, false);
            updateStatus('Error', 'error');
        }
        
    } catch (error) {
        console.error('Submission failed:', error);
        showError('Failed to submit solution. Please try again.');
        updateStatus('Error', 'error');
    }
}

function showSubmissionResult(result, isSuccess) {
    const resultPanel = document.getElementById('submitResult');
    resultPanel.style.display = 'block';
    resultPanel.className = `result-panel ${isSuccess ? 'result-success' : 'result-error'}`;
    
    if (isSuccess) {
        resultPanel.innerHTML = `
            <h3><i class="fas fa-check-circle"></i> Solution Submitted Successfully!</h3>
            <p><strong>Submission ID:</strong> ${result.submission_id}</p>
            <p><strong>Challenge:</strong> ${result.challenge_title}</p>
            <p><strong>Status:</strong> <span class="status-badge status-${result.status}">${result.status}</span></p>
            <p><strong>Score:</strong> ${result.score}/100 points</p>
            <p><strong>Time:</strong> ${new Date(result.timestamp).toLocaleString()}</p>
        `;
    } else {
        resultPanel.innerHTML = `
            <h3><i class="fas fa-exclamation-triangle"></i> Submission Failed</h3>
            <p><strong>Error:</strong> ${result.error || result.message}</p>
            ${result.missing_fields ? `<p><strong>Missing fields:</strong> ${result.missing_fields.join(', ')}</p>` : ''}
        `;
    }
    
    // Auto-hide after 10 seconds
    setTimeout(() => {
        resultPanel.style.display = 'none';
    }, 10000);
}

function clearSolution() {
    document.getElementById('solutionCode').value = '';
    document.getElementById('submitResult').style.display = 'none';
}

// Submissions Status
async function loadMySubmissions() {
    const container = document.getElementById('submissionsList');
    
    if (mySubmissions.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-inbox"></i>
                <p>No submissions yet. Submit your first solution!</p>
            </div>`;
        return;
    }
    
    container.innerHTML = mySubmissions.map(submission => `
        <div class="submission-card">
            <div class="submission-header">
                <span class="submission-id">${submission.id}</span>
                <span class="status-badge status-${submission.status}">${submission.status}</span>
            </div>
            <div class="submission-details">
                <h4>${submission.challenge_title}</h4>
                <p><strong>Score:</strong> ${submission.score}/100 points</p>
                <p><strong>Submitted:</strong> ${new Date(submission.submitted_at).toLocaleString()}</p>
                <button onclick="getSubmissionDetails('${submission.id}')" class="btn btn-secondary">
                    <i class="fas fa-info-circle"></i> View Details
                </button>
            </div>
        </div>
    `).join('');
}

async function getSubmissionDetails(submissionId) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/submissions/${submissionId}`);
        if (!response.ok) throw new Error('Failed to get submission details');
        
        const details = await response.json();
        
        // Show details in a modal or expanded view
        showInfo(`
            Submission Details:<br>
            <strong>ID:</strong> ${details.id}<br>
            <strong>Challenge:</strong> ${details.challenge_title}<br>
            <strong>Status:</strong> ${details.status}<br>
            <strong>Score:</strong> ${details.score}/100<br>
            <strong>Submitted:</strong> ${new Date(details.submitted_at).toLocaleString()}
            ${details.error_message ? `<br><strong>Error:</strong> ${details.error_message}` : ''}
        `);
        
    } catch (error) {
        console.error('Error getting submission details:', error);
        showError('Failed to load submission details');
    }
}

// Leaderboard
async function loadLeaderboard() {
    try {
        updateStatus('Loading leaderboard...', 'loading');
        
        const response = await fetch(`${API_BASE_URL}/api/leaderboard`);
        if (!response.ok) throw new Error('Failed to load leaderboard');
        
        const data = await response.json();
        displayLeaderboard(data.leaderboard);
        
        updateStatus('Connected', 'connected');
    } catch (error) {
        console.error('Error loading leaderboard:', error);
        showError('Failed to load leaderboard');
        updateStatus('Error', 'error');
    }
}

function displayLeaderboard(leaderboard) {
    const container = document.getElementById('leaderboardTable');
    
    if (!leaderboard || leaderboard.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-trophy"></i>
                <p>No participants yet. Be the first to submit a solution!</p>
            </div>`;
        return;
    }
    
    container.innerHTML = `
        <div class="leaderboard-header">
            <span>Rank</span>
            <span>Participant</span>
            <span>Score</span>
            <span>Solved</span>
            <span>Last Active</span>
        </div>
        ${leaderboard.map(entry => `
            <div class="leaderboard-row ${entry.participant_name === currentParticipant ? 'current-user' : ''}">
                <span class="rank rank-${entry.rank} ${entry.rank <= 3 ? `top-${entry.rank}` : ''}">#${entry.rank}</span>
                <span class="participant">${entry.participant_name} ${entry.participant_name === currentParticipant ? '(You)' : ''}</span>
                <span class="score">${entry.total_score}</span>
                <span class="solved">${entry.challenges_solved}</span>
                <span class="last-active">${new Date(entry.last_submission).toLocaleDateString()}</span>
            </div>
        `).join('')}
    `;
}

// Utility Functions
function updateStatus(message, type) {
    const statusElement = document.getElementById('serverStatus');
    statusElement.textContent = message;
    statusElement.className = `status-${type}`;
}

function updateLastUpdate() {
    document.getElementById('lastUpdate').textContent = new Date().toLocaleTimeString();
}

function showError(message) {
    console.error(message);
    // You could implement a toast notification system here
    alert('Error: ' + message);
}

function showSuccess(message) {
    console.log(message);
    // You could implement a toast notification system here
    alert('Success: ' + message);
}

function showInfo(message) {
    console.info(message);
    // You could implement a toast notification system here
    alert(message);
}

// Auto-refresh functionality
setInterval(() => {
    if (document.getElementById('leaderboard').classList.contains('active')) {
        loadLeaderboard();
    }
}, 30000); // Refresh leaderboard every 30 seconds

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.metaKey) {
        switch(e.key) {
            case '1':
                e.preventDefault();
                showTab('challenges');
                break;
            case '2':
                e.preventDefault();
                showTab('submit');
                break;
            case '3':
                e.preventDefault();
                showTab('status');
                break;
            case '4':
                e.preventDefault();
                showTab('leaderboard');
                break;
        }
    }
});

// External API Functions
async function fetchJSONPlaceholderPosts() {
    const resultsDiv = document.getElementById('jsonplaceholder-results');
    showApiLoading(resultsDiv, 'Fetching posts from JSONPlaceholder...');
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/external/jsonplaceholder`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, 'JSONPlaceholder Posts', data);
        } else {
            showApiError(resultsDiv, data.message || 'Failed to fetch posts');
        }
    } catch (error) {
        console.error('JSONPlaceholder fetch error:', error);
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}

async function fetchHTTPBinData() {
    const resultsDiv = document.getElementById('httpbin-results');
    showApiLoading(resultsDiv, 'Testing HTTPBin API...');
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/external/httpbin`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, 'HTTPBin Test Result', data);
        } else {
            showApiError(resultsDiv, data.message || 'HTTPBin test failed');
        }
    } catch (error) {
        console.error('HTTPBin fetch error:', error);
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}

async function fetchWeatherData() {
    const city = document.getElementById('weather-city').value.trim() || 'London';
    const resultsDiv = document.getElementById('weather-results');
    showApiLoading(resultsDiv, `Fetching weather for ${city}...`);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/external/weather?city=${encodeURIComponent(city)}`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, `Weather for ${city}`, data);
        } else {
            showApiError(resultsDiv, data.message || 'Failed to fetch weather data');
        }
    } catch (error) {
        console.error('Weather fetch error:', error);
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}

async function makeCustomRequest() {
    const url = document.getElementById('custom-url').value.trim();
    const method = document.getElementById('custom-method').value;
    const bodyText = document.getElementById('custom-body').value.trim();
    const resultsDiv = document.getElementById('custom-results');
    
    if (!url) {
        showApiError(resultsDiv, 'Please enter a URL');
        return;
    }
    
    showApiLoading(resultsDiv, `Making ${method} request to ${url}...`);
    
    try {
        const requestBody = {
            url: url,
            method: method
        };
        
        if (method === 'POST' && bodyText) {
            try {
                requestBody.body = JSON.parse(bodyText);
            } catch (e) {
                showApiError(resultsDiv, 'Invalid JSON in request body');
                return;
            }
        }
        
        const response = await fetch(`${API_BASE_URL}/api/external/custom`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            showApiSuccess(resultsDiv, 'Custom Request Result', data);
        } else {
            showApiError(resultsDiv, data.message || 'Custom request failed');
        }
    } catch (error) {
        console.error('Custom request error:', error);
        showApiError(resultsDiv, `Network error: ${error.message}`);
    }
}

// API Result Display Functions
function showApiLoading(element, message) {
    element.className = 'api-results show loading';
    element.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${message}`;
}

function showApiSuccess(element, title, data) {
    element.className = 'api-results show success';
    
    const timestamp = new Date(data.timestamp).toLocaleString();
    const source = data.source || 'Unknown';
    
    let content = `
        <div class="result-header">${title}</div>
        <div class="result-meta">
            <strong>Source:</strong> ${source}<br>
            <strong>Timestamp:</strong> ${timestamp}<br>
            <strong>Status:</strong> ${data.status}
        </div>
        <pre>${JSON.stringify(data, null, 2)}</pre>
    `;
    
    element.innerHTML = content;
}

function showApiError(element, message) {
    element.className = 'api-results show error';
    element.innerHTML = `
        <div class="result-header">Error</div>
        <div class="result-meta">
            <strong>Timestamp:</strong> ${new Date().toLocaleString()}
        </div>
        <p><i class="fas fa-exclamation-triangle"></i> ${message}</p>
    `;
}

console.log('UBS Coding Challenge 2025 - Participant Interface Ready!');
console.log('External API integration loaded!');

