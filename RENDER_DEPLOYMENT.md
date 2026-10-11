# Render Deployment Guide for Lusaka Property Valuation AVM

## Prerequisites
Before you deploy, make sure you have:
1. A GitHub account (already done ✓)
2. A Render account (FREE - https://render.com)
3. Your code pushed to GitHub
4. Git installed on your computer

---

## Step 1: Create a Render Account (FREE)

1. Go to https://render.com
2. Click **Sign Up**
3. Choose **Sign up with GitHub** (easiest)
4. Authorize Render to access your GitHub account
5. Verify your email if needed

---

## Step 2: Push Your Latest Code to GitHub

Open Command Prompt in your project folder:

```bash
cd "C:\Users\Absolute Electronics\Desktop\school\Finalyear project\lusaka_proper_valuation"
```

Then run:

```bash
git add .
git commit -m "Prepare app for Render deployment"
git push origin main
```

This uploads all your files to GitHub.

Verify it worked by going to:
```
https://github.com/charlesbkn17-cmyk/lusaka_property_valuation
```

You should see all your files listed.

---

## Step 3: Create a New Web Service on Render

1. Log in to https://render.com
2. Click **New +** button (top right)
3. Select **Web Service**
4. A page appears asking to connect a repository

---

## Step 4: Connect Your GitHub Repository

1. Click **Connect account** (if not already connected)
2. Authorize Render to access GitHub
3. Search for your repository: `lusaka_property_valuation`
4. Click the repository to select it
5. Click **Connect**

---

## Step 5: Configure the Render App

Fill in these exact settings:

| Field | Value |
|-------|-------|
| **Name** | lusaka-avm-demo |
| **Environment** | Python 3 |
| **Region** | Oregon (US East) |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port=10000 --server.address=0.0.0.0` |
| **Instance Type** | Free |

---

## Step 6: Add Environment Variables

1. Scroll down to **Environment** section
2. Click **Add Environment Variable**
3. Add this variable:

```
KEY: PYTHONUNBUFFERED
VALUE: true
```

This helps Streamlit output logs correctly.

---

## Step 7: Deploy the App

1. Review all settings (make sure they match above)
2. Click **Create Web Service** button
3. Wait 3-5 minutes for deployment

You will see a log showing:
```
Building...
Deploying...
```

When complete, you should see:
```
✓ Your service is live!
```

---

## Step 8: Get Your Public URL

At the top of the page, you will see your live app URL:

```
https://lusaka-avm-demo.onrender.com
```

(The exact name depends on what you entered in Step 5)

**Copy this URL** — you will need it for your report and presentation.

---

## Step 9: Test Your Live App

1. Click the URL or open it in your browser
2. Wait for the app to load (first load takes 10-15 seconds)
3. Test these sections:
   - ✓ Home page loads
   - ✓ Valuation Gap shows "12 recorded, 19 mapped, 7 missing"
   - ✓ Model section shows prediction form
   - ✓ Try entering values and click "Predict value"
   - ✓ System Architecture section loads

---

## Step 10: Update Your Final Report

Open your `final-report.rtf` file and add this section before the conclusion:

```
6.5 Public Demonstration and Deployment

The Automated Valuation Model has been deployed on Render 
and is publicly accessible for examination and testing at:

https://lusaka-avm-demo.onrender.com

This public deployment satisfies the requirement that the system 
must be accessible online during oral examination without reliance 
on personal or local devices. Examiners can access the following 
components through the live dashboard:

- Valuation gap analysis showing 12 recorded vs 19 mapped properties
- Interactive property valuation prediction model
- Model performance metrics (RMSE, MAE, MAPE, R²)
- System architecture and workflow overview

The system is fully functional and ready for examination.
```

---

## Step 11: Update Your Presentation

Add a new slide to your presentation slides (after Slide 22):

```
SLIDE 23: LIVE SYSTEM DEPLOYMENT

🌐 Public Access URL:
https://lusaka-avm-demo.onrender.com

✅ Features Available for Testing:
• Valuation gap analysis (12 vs 19 vs 7 properties)
• Interactive property value prediction
• Model performance evaluation
• System workflow overview

✅ No local installation required
✅ Accessible from any device
✅ Ready for examiner testing

System is live and ready for oral examination.
```

---

## Step 12: Make Any Changes to Your App

If you need to make changes to your app after deployment:

1. Edit your files locally
2. Push to GitHub:
   ```bash
   git add .
   git commit -m "Update description"
   git push origin main
   ```

3. Render will automatically redeploy

---

## Troubleshooting

### App won't deploy
Check the build logs in Render:
1. Go to your service page
2. Click **Logs** tab
3. Look for error messages
4. Common fix: make sure `requirements.txt` has all packages

### App loads slowly
First load can take 10-15 seconds. Subsequent loads are faster.

### App goes to sleep
Free tier apps sleep after 15 minutes of inactivity. They restart automatically when you visit the URL.

### Port error
The Start Command already handles the port:
```
streamlit run app.py --server.port=10000 --server.address=0.0.0.0
```

Do not change this.

### Missing dependencies
Make sure all required packages are in `requirements.txt`:
```
pandas>=2.0.0
numpy>=1.24.0
geopandas>=0.14.0
shapely>=2.0.0
scikit-learn>=1.4.0
fastapi>=0.110.0
uvicorn>=0.29.0
streamlit>=1.30.0
joblib>=1.3.0
matplotlib>=3.8.0
seaborn>=0.13.0
folium>=0.15.0
pyproj>=3.3.0
requests>=2.31.0
```

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

## Email to Send Your Supervisor

Subject: Project Deployment Complete - Live System Ready for Examination

---

Dear Mr. Mubanga,

I am pleased to inform you that the GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka has been successfully deployed and is now publicly accessible for examination.

**System URL:** https://lusaka-avm-demo.onrender.com

**GitHub Repository:** https://github.com/charlesbkn17-cmyk/lusaka_property_valuation

The system is live and ready for testing during the oral examination. Examiners can access the interactive dashboard, test the property valuation predictions, and review the valuation gap analysis without requiring a local installation.

The final report, presentation slides, and deployment documentation are included in the repository.

Best regards,
Charles Silunjili
Cosmas Mwanza
Isaac Lungu

---

## Quick Reference: Your Live System

Once deployed, examiners will see:
- Interactive web interface
- Real-time property valuation predictions
- Kalingalinga valuation gap: 7 missing properties
- Model performance metrics
- No local installation required
- Accessible from any device with internet

**You're almost there!** After deployment, your project is exam-ready.

---

## Key Advantages of Render

✅ Simpler than Heroku (just connect GitHub)
✅ Automatic redeployment on GitHub push
✅ Free tier is generous
✅ No CLI installation needed
✅ UI is very user-friendly
✅ Logs are easy to read

---

## Full Deployment Checklist

- [ ] Render account created
- [ ] GitHub repository up to date
- [ ] Code pushed to GitHub
- [ ] Web Service created on Render
- [ ] Build Command set correctly
- [ ] Start Command set correctly
- [ ] Environment variable added
- [ ] App deployed successfully
- [ ] Public URL verified working
- [ ] URL added to final report
- [ ] URL added to presentation
- [ ] Supervisor notified of live URL
- [ ] GitHub repository linked

---

Your system is now ready for public examination. Good luck!
