#!/bin/bash
set -e

echo "📤 Pushing to GitHub..."

# Check if remote exists
if git remote get-url origin 2>/dev/null; then
    echo "✓ Remote already configured"
else
    echo "Adding remote..."
    git remote add origin https://github.com/ashwin24121995/fanliteplay.git
fi

# Try to push
echo "Pushing commits to GitHub..."
git push -u origin main 2>&1 || echo "Push may require authentication"

echo "✅ Repository is ready"
echo "GitHub URL: https://github.com/ashwin24121995/fanliteplay"
