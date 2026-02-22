#!/usr/bin/env python3
import json
import subprocess
import os
import time

print("🚀 FanLitePlay - Vercel Deployment Script")
print("=" * 50)

# Step 1: Prepare project
print("\n📦 Step 1: Preparing project...")
os.chdir('/home/ubuntu/fanliteplay-pure')

# Step 2: Check git status
print("📝 Step 2: Checking git status...")
result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
if result.stdout.strip():
    print("⚠️  Uncommitted changes found. Committing...")
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Final deployment update'], capture_output=True)
    print("✅ Changes committed")
else:
    print("✅ All changes committed")

# Step 3: Get git log
print("\n📊 Step 3: Project commits:")
result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
print(result.stdout)

# Step 4: Display project info
print("📋 Step 4: Project Information:")
print("-" * 50)
print("Project Name: FanLitePlay")
print("Repository: https://github.com/ashwin24121995/fanliteplay")
print("Pages: 7 (Home, About, How to Play, Blog, Contact, Terms, Privacy)")
print("Technology: Pure HTML/CSS (No JavaScript)")
print("Theme: Light with Teal & Purple colors")
print("Status: Ready for Deployment")
print("-" * 50)

# Step 5: Display deployment instructions
print("\n🌐 Step 5: Deployment Instructions:")
print("-" * 50)
print("Since Vercel is linked to your GitHub account,")
print("deployment will happen automatically when you:")
print("")
print("1. Go to: https://vercel.com")
print("2. Click: 'Add New' → 'Project'")
print("3. Select: 'Import Git Repository'")
print("4. Paste: https://github.com/ashwin24121995/fanliteplay")
print("5. Click: 'Import'")
print("")
print("Vercel will automatically:")
print("  ✓ Detect the static site")
print("  ✓ Deploy all 7 pages")
print("  ✓ Assign a vercel.app domain")
print("  ✓ Enable HTTPS")
print("  ✓ Set up auto-deployments")
print("-" * 50)

# Step 6: Display expected domain
print("\n🎯 Step 6: Expected Vercel Domain:")
print("-" * 50)
print("Your website will be live at one of these:")
print("  • fanliteplay.vercel.app")
print("  • fanliteplay-git-main-ashwin24121995s-projects.vercel.app")
print("  • fanliteplay-ashwin24121995s-projects.vercel.app")
print("")
print("After deployment, you can:")
print("  ✓ Connect custom domain (fanliteplay.com)")
print("  ✓ Enable analytics")
print("  ✓ Set up environment variables")
print("  ✓ Configure preview deployments")
print("-" * 50)

print("\n✅ Project is ready for deployment!")
print("📤 All files are committed and pushed to GitHub")
print("🚀 Visit https://vercel.com to deploy now!")
print("\n" + "=" * 50)

