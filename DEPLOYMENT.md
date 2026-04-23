# Deployment Guide: Medicio Hospital to Render

## Prerequisites
- GitHub account
- Render account (https://render.com)
- Your code pushed to GitHub

## Step 1: Push Your Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit - ready for deployment"
git remote add origin https://github.com/yourusername/medicio-hospital.git
git branch -M main
git push -u origin main
```

## Step 2: Create PostgreSQL Database on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `medicio-hospital-db`
   - **Database**: `medicio_db`
   - **User**: `medicio_user`
   - **Region**: Choose closest to you
   - **Plan**: Free tier
4. Click **"Create Database"**
5. **Copy the database URL** from the connection details (you'll need this)

## Step 3: Deploy Web Service on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Select **"Deploy an existing Git repository"**
4. Paste your GitHub repository URL
5. Configure the service:
   - **Name**: `medicio-hospital`
   - **Environment**: `Python 3`
   - **Region**: Same as database
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   - **Start Command**: 
     ```
     gunicorn medicio_project.wsgi
     ```
   - **Plan**: Free tier

## Step 4: Set Environment Variables

In the Render dashboard for your web service, go to **Environment** and add:

```
DEBUG = False
SECRET_KEY = [Generate a strong secret key]
ALLOWED_HOSTS = medicio-hospital.onrender.com,*.onrender.com,localhost,127.0.0.1
DATABASE_URL = [Paste the PostgreSQL URL from Step 2]
```

### Generate a Secret Key:

Run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Step 5: Complete Render Configuration

1. Click **"Create Web Service"**
2. Wait for the deployment to complete (5-10 minutes)
3. Check the build logs for any errors

## Step 6: Run Database Migrations

Once deployed, Render will automatically run `python manage.py migrate` via the Procfile.

## Step 7: Create Superuser (Optional)

To access Django admin panel:
```bash
# Via Render Shell (in dashboard)
python manage.py createsuperuser
```

## Step 8: Access Your Application

- **Website**: https://medicio-hospital.onrender.com
- **Admin**: https://medicio-hospital.onrender.com/admin

## Troubleshooting

### Database connection errors
- Ensure DATABASE_URL is correctly copied
- Check that PostgreSQL instance is running on Render

### Static files not loading
- The `collectstatic` command should handle this
- WhiteNoise is configured to serve static files

### 500 Internal Server Error
- Check Build Logs in Render dashboard
- Check Runtime Logs for detailed errors

## Updating Your Application

Simply push changes to GitHub:
```bash
git add .
git commit -m "Your message"
git push origin main
```

Render will automatically redeploy your application.

## Important Notes

- ✅ SQLite database is local (not synced on Render)
- ✅ All appointments will be saved in PostgreSQL
- ✅ Static files are served by WhiteNoise
- ✅ Email functionality will need SMTP configuration for production
- ✅ Free tier has limitations (RAM, disk space)

## Support

For Render support: https://render.com/docs
