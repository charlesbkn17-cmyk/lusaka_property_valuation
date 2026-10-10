# Heroku Deployment Guide for Lusaka Property Valuation AVM

## Prerequisites
Before you deploy, make sure you have:
1. A GitHub account (already done ✓)
2. A Heroku account (FREE - https://www.heroku.com)
3. Heroku CLI installed on your computer
4. Git installed on your computer

---

## Step 1: Create a Heroku Account (FREE)

1. Go to https://www.heroku.com
2. Click **Sign Up**
3. Enter your email and create a password
4. Verify your email
5. Log in to Heroku dashboard

---

## Step 2: Install Heroku CLI

### On Windows:
- Download installer from https://devcenter.heroku.com/articles/heroku-cli
- Run the installer and follow prompts
- Open Command Prompt or PowerShell and verify:
```bash
heroku --version
```

### On Mac:
```bash
brew tap heroku/brew && brew install heroku
heroku --version
```

### On Linux:
```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku --version
```

---

## Step 3: Login to Heroku via CLI

Open Command Prompt/Terminal and run:
```bash
heroku login
```

This opens a browser window to authenticate. Click **Log In** and wait for confirmation.

---

## Step 4: Prepare Your Repository

Navigate to your project folder:
```bash
cd lusaka_property_valuation
```

Initialize Git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit - Lusaka AVM project"
```

Verify Git is working:
```bash
git remote -v
```

If you already have a GitHub remote:
```bash
git push origin main
```

---

## Step 5: Create a Heroku App

Choose a unique app name (lowercase, no spaces). Replace `lusaka-avm-demo` with your chosen name:

```bash
heroku create lusaka-avm-demo
```

**Note:** If the name is taken, try:
```bash
heroku create lusaka-avm-demo-2026
heroku create your-name-lusaka-avm
```

Verify the app was created:
```bash
heroku apps:info lusaka-avm-demo
```

You should see something like:
```
=== lusaka-avm-demo
Git URL:        https://git.heroku.com/lusaka-avm-demo.git
Web URL:        https://lusaka-avm-demo.herokuapp.com
```

---

## Step 6: Deploy to Heroku

Push your code to Heroku:
```bash
git push heroku main
```

This will:
- Upload your code
- Detect Python app
- Install dependencies from `requirements.txt`
- Start the Streamlit server
- Build and deploy

Wait for completion. You should see:
```
remote:        Verifying deploy... done.
To https://git.heroku.com/lusaka-avm-demo.git
```

---

## Step 7: View Your Live App

Your app is now live at:
```
https://lusaka-avm-demo.herokuapp.com
```

(Replace `lusaka-avm-demo` with your actual app name)

Open it in your browser and test:
- ✓ Home page loads
- ✓ Valuation Gap section shows 12/19/7
- ✓ Model prediction form works
- ✓ System Architecture displays

---

## Step 8: Update Your Report and Presentation

Add this URL to:

### In your final-report.rtf:
```
Section: Demonstration and Deployment

The system is deployed and publicly accessible at:
https://lusaka-avm-demo.herokuapp.com

Examiners can access the live demonstration via this URL. 
The system includes:
- Valuation gap analysis showing 12 recorded vs 19 mapped properties
- Interactive property valuation model
- Performance metrics and model evaluation
- System architecture overview
```

### In your presentation slides:
**Add new slide after Slide 22 (Thank You):**

```
SLIDE 23: Live Demonstration

The system is publicly deployed and accessible for examination:

URL: https://lusaka-avm-demo.herokuapp.com

Features available for testing:
✓ Valuation gap analysis
✓ Property value prediction
✓ Model performance metrics
✓ System workflow overview

Examiners can access and interact with the system during oral examination.
```

---

## Troubleshooting

### App fails to deploy
Check logs:
```bash
heroku logs --tail
```

### Port error
Already handled in Procfile - should bind to port from environment

### Model not loading
The demo uses synthetic data, so no external model file is needed.

### App sleeps after 30 minutes of inactivity
This is normal on free tier. Accessing the URL wakes it up.

### Need to rebuild/redeploy
Make changes locally, then:
```bash
git add .
git commit -m "Update message"
git push heroku main
```

---

## Full Command Checklist

```bash
# 1. Login
heroku login

# 2. Create app
heroku create lusaka-avm-demo

# 3. Verify Git remote
git remote -v

# 4. Push code
git push heroku main

# 5. Open app
heroku open

# 6. View logs
heroku logs --tail
```

---

## Testing the Deployed System

Once live, test these features for examiners:

### 1. Home Page
- Displays title and project description
- Shows metrics: 12 recorded, 19 mapped, 7 gap

### 2. Valuation Gap Section
- Bar chart showing property counts
- Pie chart showing gap percentage
- Clear explanation of implications

### 3. Model Section
- Shows model performance metrics (RMSE, MAE, MAPE, R²)
- Interactive prediction form
- Users can input property features and get value estimate

### 4. System Architecture
- Displays workflow steps
- Explains methodology

---

## After Deployment

### Share the URL
Send this to your supervisor and examiners:
```
System is available at: https://lusaka-avm-demo.herokuapp.com
Repository: https://github.com/charlesbkn17-cmyk/lusaka_property_valuation
```

### Keep it running
The app will sleep after 30 minutes of no use (free tier). 
Just visiting the URL wakes it back up.

### Monitor usage
```bash
heroku apps:info lusaka-avm-demo
heroku logs --tail
```

---

## Important: Include in Final Submission

Your supervisor needs:
1. **Live URL** in your report
2. **Live URL** in your presentation
3. **GitHub link** (already public)
4. Instructions for examiners to access the system

Example text for your report:

> "The system has been deployed on Heroku and is publicly accessible for examination at https://lusaka-avm-demo.herokuapp.com. Examiners can access the interactive dashboard, test the property valuation model, and review the valuation gap analysis without requiring a local installation."

---

## Full Deployment Status Checklist

- [ ] Heroku account created
- [ ] Heroku CLI installed and logged in
- [ ] Git repository initialized locally
- [ ] All files added and committed to Git
- [ ] Heroku app created
- [ ] Code pushed to Heroku
- [ ] App deployed and live
- [ ] URL tested and working
- [ ] URL added to final report
- [ ] URL added to presentation
- [ ] Supervisor notified of live URL
- [ ] GitHub repository linked

---

## After Deployment is Complete

Your project will have:
✅ Complete written report (final-report.rtf)
✅ Professional presentation slides (presentation_slides.md)
✅ Live, publicly accessible web dashboard
✅ All code in public GitHub repository
✅ Ready for examiner testing during oral examination

This satisfies your lecturer's requirement: **"Demonstrating your system with personal/local devices will not be permitted. The system must be publicly accessible."**

---

## Quick Reference: Your Live System

Once deployed, examiners will see:
- Interactive web interface
- Real-time property valuation predictions
- Kalingalinga valuation gap: 7 missing properties
- Model performance: R² = 0.85+ (depends on training)
- No local installation required
- Accessible from any device with internet

**You're almost there!** After deployment, your project is exam-ready.

