#!/bin/bash

echo "==================================================="
echo "  🏔️ Visit Nepal 2022 Installer (Linux/macOS)"
echo "==================================================="
echo

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ python3 could not be found. Please install Python 3.9+ and try again."
    exit 1
fi

echo "📦 Creating Python virtual environment (venv)..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment."
    exit 1
fi
echo

echo "🔌 Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment."
    exit 1
fi
echo

echo "🔄 Upgrading pip..."
python3 -m pip install --upgrade pip
echo

echo "📥 Installing project dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    exit 1
fi
echo

echo "🗄️ Setting up database and migrations..."
cd django_app
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "⚠️ Database migration had issues. Continuing..."
fi
cd ..
echo

echo "==================================================="
echo "🎉 Installation Completed Successfully!"
echo "==================================================="
echo
echo "To run the application:"
echo "1. Run 'source venv/bin/activate' to activate virtual env."
echo "2. Run 'python run_all.py' to start Django and Rasa."
echo
