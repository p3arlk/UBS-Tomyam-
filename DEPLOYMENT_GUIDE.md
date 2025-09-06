# Deployment Guide

Your Flask server and frontend are now **deployment-ready**! Here are the best free hosting options and deployment instructions.

## 🚀 Free Hosting Services Comparison

### 1. **Heroku** (Recommended) ⭐
- **Cost**: Free tier with 550-1000 dyno hours/month
- **Best for**: Flask backend + static frontend
- **Pros**: Easy deployment, great documentation, add-ons available
- **Cons**: App sleeps after 30 minutes of inactivity

### 2. **Railway** ⭐
- **Cost**: $5 free credit monthly (enough for small apps)
- **Best for**: Modern deployment with great developer experience
- **Pros**: No sleep mode, excellent performance, easy setup
- **Cons**: Credit-based system

### 3. **Render** ⭐
- **Cost**: Free tier for web services
- **Best for**: Flask backend
- **Pros**: No sleep mode on paid tier, easy setup
- **Cons**: Free tier has limitations

### 4. **Vercel** (Frontend only)
- **Cost**: Free tier with generous limits
- **Best for**: Static frontend hosting
- **Pros**: Excellent for frontend, automatic deployments
- **Cons**: Backend needs separate hosting

### 5. **Netlify** (Frontend only)
- **Cost**: Free tier with 100GB bandwidth
- **Best for**: Static frontend hosting
- **Pros**: Easy setup, form handling, functions
- **Cons**: Backend needs separate hosting

## 📋 Deployment Instructions

### Option 1: Heroku (Full-Stack) - RECOMMENDED

#### Prerequisites:
```bash
# Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

#### Steps:
1. **Create Heroku app**:
```bash
heroku create your-app-name
```

2. **Set environment variables**:
```bash
heroku config:set SECRET_KEY=your-secure-secret-key
heroku config:set FLASK_ENV=production
heroku config:set DEBUG=False
```

3. **Deploy**:
```bash
git add .
git commit -m "Ready for deployment"
git push heroku main
```

4. **Access your app**:
```
https://your-app-name.herokuapp.com
```

### Option 2: Railway (Full-Stack)

#### Steps:
1. **Connect GitHub**: Go to https://railway.app
2. **Deploy from GitHub**: Select your repository
3. **Environment Variables**: Add in Railway dashboard:
   - `SECRET_KEY=your-secure-secret-key`
   - `FLASK_ENV=production`
   - `DEBUG=False`
4. **Deploy**: Automatic on git push

### Option 3: Render (Full-Stack)

#### Steps:
1. **Connect GitHub**: Go to https://render.com
2. **Create Web Service**: Select your repository
3. **Configuration**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn wsgi:app`
4. **Environment Variables**: Add in Render dashboard
5. **Deploy**: Automatic

### Option 4: Separate Frontend + Backend

#### Backend (Heroku/Railway/Render):
- Deploy Flask app using steps above

#### Frontend (Vercel/Netlify):

**Vercel**:
1. Go to https://vercel.com
2. Import your GitHub repository
3. Set build settings:
   - Framework: Other
   - Root Directory: `web_frontend`
   - Output Directory: `web_frontend`

**Netlify**:
1. Go to https://netlify.com
2. Drag and drop your `web_frontend` folder
3. Or connect GitHub repository

## ⚙️ Pre-Deployment Checklist

### ✅ Files Created (Already Done):
- [x] `Procfile` - Heroku deployment configuration
- [x] `wsgi.py` - Production WSGI entry point
- [x] `runtime.txt` - Python version specification
- [x] `env.production` - Production environment template
- [x] Updated `requirements.txt` with gunicorn
- [x] Dynamic API URL configuration in frontend

### ✅ Required Actions:

1. **Set Production Environment**:
```bash
# Copy production environment template
cp env.production .env

# Edit .env file with your production values
# IMPORTANT: Set a secure SECRET_KEY!
```

2. **Generate Secure Secret Key**:
```python
# Run this in Python to generate a secure key
import secrets
print(secrets.token_hex(32))
```

3. **Test Production Setup Locally**:

**On Windows:**
```bash
# Install waitress (Windows-compatible WSGI server)
pip install waitress

# Test production server with waitress
python test_production_server.py

# Access: http://localhost:8000
```

**On Linux/Mac (or for deployment):**
```bash
# Install gunicorn (Unix-only)
pip install gunicorn

# Test production server
gunicorn wsgi:app

# Access: http://localhost:8000
```

4. **Configure Git (if not done)**:
```bash
git init
git add .
git commit -m "Initial deployment setup"
```

## 🔧 Environment Variables for Production

### Required:
```
SECRET_KEY=your-64-character-secret-key
FLASK_ENV=production
DEBUG=False
```

### Optional (for external APIs):
```
OPENWEATHER_API_KEY=your_api_key
NEWS_API_KEY=your_api_key
GITHUB_TOKEN=your_token
```

## 🌐 Domain Configuration

### Custom Domain (Optional):
1. **Free options**: Use platform subdomains
   - Heroku: `your-app.herokuapp.com`
   - Railway: `your-app.railway.app`
   - Render: `your-app.render.com`

2. **Custom domain**: Configure DNS in platform settings

## 🔒 Security Considerations

### Production Security:
1. **Never commit .env files** - Add to `.gitignore`
2. **Use strong SECRET_KEY** - Generate with `secrets.token_hex(32)`
3. **Set DEBUG=False** in production
4. **Configure CORS properly** for your domain
5. **Use HTTPS** (most platforms provide this automatically)

## 🐛 Common Deployment Issues

### Issue: App not starting
**Solution**: Check logs
```bash
# Heroku
heroku logs --tail

# Railway/Render: Check platform logs
```

### Issue: Static files not loading
**Solution**: Ensure frontend uses relative paths

### Issue: API calls failing
**Solution**: Check CORS configuration and API URLs

### Issue: Environment variables not working
**Solution**: Verify they're set in platform dashboard

## 📈 Monitoring & Maintenance

### Free Monitoring Tools:
1. **Platform logs**: Built-in logging on all platforms
2. **Uptime monitoring**: UptimeRobot (free)
3. **Error tracking**: Sentry (free tier)

### Automatic Deployments:
- Connect GitHub repository for automatic deployments on push
- Use staging/production branches for better control

## 🎯 Recommended Deployment Strategy

**For Beginners**:
1. Start with **Heroku** (full-stack, easy setup)
2. Use platform subdomain initially
3. Add custom domain later if needed

**For Performance**:
1. **Railway** for backend (no sleep mode)
2. **Vercel** for frontend (excellent performance)
3. Configure frontend to call backend API

**For Learning**:
1. Try multiple platforms to understand differences
2. Start with free tiers
3. Upgrade as needed

## 🆘 Need Help?

1. **Platform Documentation**:
   - Heroku: https://devcenter.heroku.com/
   - Railway: https://docs.railway.app/
   - Render: https://render.com/docs
   - Vercel: https://vercel.com/docs
   - Netlify: https://docs.netlify.com/

2. **Test Deployment Locally**: Always test with `gunicorn wsgi:app` before deploying

3. **Environment Variables**: Double-check all required variables are set

Your application is now ready for deployment! Choose your preferred platform and follow the corresponding instructions above.
