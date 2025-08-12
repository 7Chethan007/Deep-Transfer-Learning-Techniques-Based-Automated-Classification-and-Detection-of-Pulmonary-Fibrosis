#!/usr/bin/env python3
"""
Repository Setup Verification Script
Checks if all components are properly configured
"""

import os
import sys
import importlib.util

def check_file_exists(filepath, description):
    """Check if a file exists and report status"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} (MISSING)")
        return False

def check_import(module_name, description):
    """Check if a module can be imported"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            print(f"✅ {description}: {module_name}")
            return True
        else:
            print(f"❌ {description}: {module_name} (NOT FOUND)")
            return False
    except Exception as e:
        print(f"❌ {description}: {module_name} (ERROR: {e})")
        return False

def check_directory_structure():
    """Verify the expected directory structure"""
    print("🏗️  CHECKING REPOSITORY STRUCTURE")
    print("=" * 40)
    
    structure_ok = True
    
    # Core files
    structure_ok &= check_file_exists("app.py", "Main Flask Application")
    structure_ok &= check_file_exists("predict.py", "Prediction Engine")
    structure_ok &= check_file_exists("requirements.txt", "Dependencies File")
    structure_ok &= check_file_exists("README.md", "Documentation")
    
    # Template files
    structure_ok &= check_file_exists("templates/index.html", "Web Interface Template")
    
    # Utility package
    structure_ok &= check_file_exists("com_in_ineuron_ai_utils/__init__.py", "Utils Package Init")
    structure_ok &= check_file_exists("com_in_ineuron_ai_utils/utils.py", "Utils Module")
    
    # Documentation files (newly added)
    structure_ok &= check_file_exists("REPOSITORY_STRUCTURE_DOCUMENTATION.md", "Detailed Documentation")
    structure_ok &= check_file_exists("QUICK_OVERVIEW.md", "Quick Overview")
    structure_ok &= check_file_exists("visualize_structure.py", "Structure Visualization")
    
    # Model file (expected to be missing)
    model_exists = check_file_exists("Model.h5", "Trained Model File")
    if not model_exists:
        print("⚠️  Note: Model.h5 is missing but this is expected for this repository")
    
    return structure_ok

def check_dependencies():
    """Check if required dependencies can be imported"""
    print("\n📦 CHECKING DEPENDENCIES")
    print("=" * 40)
    
    deps_ok = True
    
    # Core dependencies from requirements.txt
    deps_ok &= check_import("flask", "Flask Web Framework")
    deps_ok &= check_import("numpy", "NumPy")
    deps_ok &= check_import("PIL", "Pillow (PIL)")
    
    # Optional dependencies (might not be installed in this environment)
    check_import("tensorflow", "TensorFlow (Optional)")
    check_import("keras", "Keras (Optional)")
    check_import("h5py", "H5PY (Optional)")
    
    return deps_ok

def check_code_syntax():
    """Check if Python files have valid syntax"""
    print("\n🐍 CHECKING CODE SYNTAX")
    print("=" * 40)
    
    syntax_ok = True
    python_files = ["app.py", "predict.py", "com_in_ineuron_ai_utils/utils.py", "visualize_structure.py"]
    
    for file_path in python_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    compile(f.read(), file_path, 'exec')
                print(f"✅ Syntax check: {file_path}")
            except SyntaxError as e:
                print(f"❌ Syntax error in {file_path}: {e}")
                syntax_ok = False
            except Exception as e:
                print(f"⚠️  Could not check {file_path}: {e}")
        else:
            print(f"❌ File not found: {file_path}")
            syntax_ok = False
    
    return syntax_ok

def analyze_repository_health():
    """Provide overall repository health assessment"""
    print("\n📊 REPOSITORY HEALTH ASSESSMENT")
    print("=" * 40)
    
    structure_score = check_directory_structure()
    deps_score = check_dependencies()
    syntax_score = check_code_syntax()
    
    print(f"\n📈 OVERALL HEALTH REPORT:")
    print(f"• Repository Structure: {'✅ GOOD' if structure_score else '❌ ISSUES'}")
    print(f"• Dependencies: {'✅ AVAILABLE' if deps_score else '⚠️  SOME MISSING'}")
    print(f"• Code Syntax: {'✅ VALID' if syntax_score else '❌ ERRORS'}")
    
    if structure_score and syntax_score:
        print(f"\n🎉 REPOSITORY STATUS: HEALTHY")
        print(f"The repository structure is complete and code is syntactically correct.")
        print(f"Missing dependencies can be installed with: pip install -r requirements.txt")
        print(f"Missing Model.h5 file needs to be obtained separately.")
    else:
        print(f"\n⚠️  REPOSITORY STATUS: NEEDS ATTENTION")
        print(f"Some issues were detected that should be addressed.")
    
    return structure_score and syntax_score

def main():
    """Main verification function"""
    print("🔍 REPOSITORY SETUP VERIFICATION")
    print("=" * 50)
    print("Verifying Deep Transfer Learning Pulmonary Fibrosis Detection Repository")
    print("=" * 50)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run all checks
    overall_health = analyze_repository_health()
    
    print(f"\n🎯 NEXT STEPS:")
    if overall_health:
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Obtain the trained model file (Model.h5)")
        print("3. Run the application: python app.py")
        print("4. Visit http://localhost:5000 to test the interface")
    else:
        print("1. Address the issues identified above")
        print("2. Re-run this script to verify fixes")
    
    print(f"\n📚 DOCUMENTATION:")
    print("• Quick Overview: QUICK_OVERVIEW.md")
    print("• Detailed Docs: REPOSITORY_STRUCTURE_DOCUMENTATION.md")
    print("• Structure Visualization: python visualize_structure.py")

if __name__ == "__main__":
    main()