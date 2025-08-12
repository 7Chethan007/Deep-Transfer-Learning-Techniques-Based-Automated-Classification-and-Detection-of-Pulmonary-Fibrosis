#!/usr/bin/env python3
"""
Repository Structure Visualization Tool
Generates a tree-like visualization of the repository structure
"""

import os
import sys

def print_tree(directory, prefix="", max_depth=3, current_depth=0):
    """
    Print a tree structure of the directory
    """
    if current_depth >= max_depth:
        return
    
    items = []
    try:
        items = sorted(os.listdir(directory))
        # Filter out hidden files and common non-essential directories
        items = [item for item in items if not item.startswith('.') and item != '__pycache__']
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        
        current_prefix = "└── " if is_last else "├── "
        
        # Add emoji indicators for different file types
        if os.path.isdir(path):
            if item == "templates":
                emoji = "🌐"
            elif item == "images":
                emoji = "🖼️"
            elif "utils" in item:
                emoji = "🛠️"
            else:
                emoji = "📁"
            print(f"{prefix}{current_prefix}{emoji} {item}/")
            
            # Recursively print subdirectory contents
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, next_prefix, max_depth, current_depth + 1)
        else:
            # File type emojis
            if item.endswith('.py'):
                emoji = "🐍"
            elif item.endswith('.html'):
                emoji = "🌐"
            elif item.endswith('.md'):
                emoji = "📄"
            elif item.endswith('.txt'):
                emoji = "📋"
            elif item.endswith('.h5'):
                emoji = "🤖"
            elif item.endswith('.jpg') or item.endswith('.png'):
                emoji = "🖼️"
            else:
                emoji = "📄"
            
            # Add special indicators for important files
            if item == "app.py":
                print(f"{prefix}{current_prefix}{emoji} {item} (Main Flask App)")
            elif item == "predict.py":
                print(f"{prefix}{current_prefix}{emoji} {item} (ML Prediction Engine)")
            elif item == "requirements.txt":
                print(f"{prefix}{current_prefix}{emoji} {item} (Dependencies)")
            elif item == "Model.h5":
                print(f"{prefix}{current_prefix}{emoji} {item} (⚠️ MISSING: Trained Model)")
            else:
                print(f"{prefix}{current_prefix}{emoji} {item}")

def main():
    """
    Main function to display repository structure
    """
    current_dir = os.getcwd()
    repo_name = os.path.basename(current_dir)
    
    print("🏗️  Repository Structure Visualization")
    print("=" * 50)
    print(f"📁 {repo_name}/")
    
    # Check if Model.h5 exists and add note if missing
    model_path = os.path.join(current_dir, "Model.h5")
    if not os.path.exists(model_path):
        print("⚠️  Note: Model.h5 file is missing and needs to be added")
        print()
    
    print_tree(current_dir, max_depth=3)
    
    print("\n🔍 File Type Legend:")
    print("🐍 Python scripts")
    print("🌐 Web templates/HTML")
    print("📄 Documentation")
    print("📋 Configuration/Requirements")
    print("🤖 Machine Learning Models")
    print("🖼️ Images/Screenshots")
    print("📁 Directories")
    print("🛠️ Utility packages")
    
    print("\n📊 Repository Summary:")
    print(f"• Main Application: app.py (Flask web server)")
    print(f"• Prediction Engine: predict.py (ResNet50v2 model)")
    print(f"• Web Interface: templates/index.html")
    print(f"• Dependencies: requirements.txt")
    print(f"• Documentation: README.md + REPOSITORY_STRUCTURE_DOCUMENTATION.md")
    print(f"• Utilities: com_in_ineuron_ai_utils/")
    print(f"• Assets: images/ (screenshots and diagrams)")

if __name__ == "__main__":
    main()