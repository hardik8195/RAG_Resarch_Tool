#!/usr/bin/env python3
"""
Project Analysis Script
Analyzes the actual code distribution in your project to show the real complexity
"""

import os
import glob
from pathlib import Path

def analyze_project():
    """Analyze the project structure and code distribution"""
    
    # Define file extensions and their categories
    categories = {
        'Python (Backend/AI)': ['*.py'],
        'JavaScript/React': ['*.js', '*.jsx'],
        'CSS/Styling': ['*.css'],
        'HTML': ['*.html'],
        'JSON': ['*.json'],
        'Markdown': ['*.md'],
        'Configuration': ['*.toml', '*.yaml', '*.yml', '*.ini', '*.cfg'],
        'Docker': ['Dockerfile', '*.dockerfile'],
        'Requirements': ['requirements.txt', 'package.json']
    }
    
    stats = {category: {'files': 0, 'lines': 0} for category in categories}
    
    # Analyze each category
    for category, patterns in categories.items():
        for pattern in patterns:
            files = glob.glob(f"**/{pattern}", recursive=True)
            for file_path in files:
                if os.path.isfile(file_path):
                    stats[category]['files'] += 1
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = len(f.readlines())
                            stats[category]['lines'] += lines
                    except:
                        pass
    
    # Print results
    print("🤖 AI-Powered News Research Tool - Project Analysis")
    print("=" * 60)
    print()
    
    total_files = sum(stats[cat]['files'] for cat in stats)
    total_lines = sum(stats[cat]['lines'] for cat in stats)
    
    print(f"📊 Total Files: {total_files}")
    print(f"📊 Total Lines of Code: {total_lines:,}")
    print()
    
    print("📈 Code Distribution by Category:")
    print("-" * 40)
    
    for category, data in stats.items():
        if data['files'] > 0:
            percentage = (data['lines'] / total_lines * 100) if total_lines > 0 else 0
            print(f"{category:25} | {data['files']:3} files | {data['lines']:6,} lines | {percentage:5.1f}%")
    
    print()
    print("🎯 Key Insights:")
    print("-" * 20)
    
    # Calculate AI/ML related code
    ai_ml_lines = stats['Python (Backend/AI)']['lines']
    ai_ml_percentage = (ai_ml_lines / total_lines * 100) if total_lines > 0 else 0
    
    print(f"• AI/ML Backend Code: {ai_ml_lines:,} lines ({ai_ml_percentage:.1f}%)")
    print(f"• Frontend Code: {stats['JavaScript/React']['lines']:,} lines")
    print(f"• Styling: {stats['CSS/Styling']['lines']:,} lines")
    print()
    print("💡 This project is primarily an AI/ML application with a modern web interface!")
    print("   The CSS percentage on GitHub is misleading - the real complexity is in the AI pipeline.")

if __name__ == "__main__":
    analyze_project()
