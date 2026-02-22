#!/bin/bash
set -e

echo "📦 Preparing FanLitePlay for Vercel deployment..."

# Create .vercel directory
mkdir -p .vercel

# Create project.json
cat > .vercel/project.json << 'VERCEL_JSON'
{
  "projectId": "prj_fanliteplay",
  "orgId": "team_n7FbF69Eq4LPUWgrDjrqg2Vt",
  "settings": {
    "buildCommand": "echo 'Static site'",
    "outputDirectory": ".",
    "cleanUrls": true
  }
}
VERCEL_JSON

echo "✅ Vercel configuration created"
echo "📝 Project is ready for deployment"
echo ""
echo "Next steps:"
echo "1. Go to https://vercel.com"
echo "2. Click 'Add New' → 'Project'"
echo "3. Import: https://github.com/ashwin24121995/fanliteplay"
echo "4. Vercel will auto-deploy your website"
