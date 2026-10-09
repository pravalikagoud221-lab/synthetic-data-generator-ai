#!/bin/bash

# Synthetic Data Generator - Run Script

echo "====================================================="
echo "  Synthetic Data Generator - Ollama Edition"
echo "====================================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "====================================================="
echo "✅ Setup complete!"
echo "====================================================="
echo ""
echo "🚀 Starting Flask application..."
echo ""
echo "📍 Open your browser to: http://localhost:5000"
echo ""
echo "💡 Make sure Ollama is running in another terminal:"
echo "   $ ollama pull mistral"
echo "   $ ollama serve"
echo ""
echo "Press Ctrl+C to stop the application"
echo "====================================================="
echo ""

python3 app.py
