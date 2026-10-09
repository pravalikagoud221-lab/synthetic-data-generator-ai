# Synthetic Data Generator with Ollama

A Flask web application that generates realistic synthetic business data using free local Ollama models or fallback mock data. No API costs required.

## 🎯 Features

- ✅ Generate synthetic customer profiles
- ✅ Generate transaction history
- ✅ Generate employee records
- ✅ Generate customer feedback
- ✅ Export to CSV format
- ✅ Works completely offline with mock data fallback
- ✅ No API charges
- ✅ Privacy-friendly (all data is synthetic)

## 📋 Requirements

- Python 3.8+
- Flask
- Requests
- Ollama (optional, but recommended)

## 🚀 Quick Start

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
cd synthetic-data-generator-ai
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install and Run Ollama (Optional)

Download Ollama from: https://ollama.com

Then pull a model:

```bash
ollama pull mistral
```

Run Ollama:

```bash
ollama serve
```

**Note:** If Ollama is not running, the app will automatically use mock data generation.

### Step 4: Run the Flask App

```bash
python app.py
```

### Step 5: Open in Browser

```
http://localhost:5000
```

## 🔧 Environment Variables

Optional - Create a `.env` file or set these environment variables:

```bash
FLASK_SECRET_KEY=your-secret-key-here
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=mistral
```

## 📂 Project Structure

```
synthetic-data-generator-ai/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── templates/
    └── index.html         # Web UI
```

## 🎨 Usage

1. **Generate Customers**: Click "Generate Customers" to create synthetic customer profiles
2. **Generate Transactions**: Create transaction history for testing and training
3. **Generate Employees**: Generate realistic employee records
4. **Generate Feedback**: Create customer feedback entries
5. **Download CSV**: Export any dataset as a CSV file
6. **Copy JSON**: Copy the JSON output to clipboard

## 💼 Business Use Cases

- **Testing**: Test data for application development and QA
- **Training**: ML model training without exposing real customer data
- **Demos**: Demo datasets for client presentations
- **Development**: Safe testing environment with realistic data
- **Data Science**: Practice analytics and data visualization
- **Load Testing**: Generate large datasets for performance testing

## 🔐 Privacy & Security

- All generated data is completely fictional
- No real customer data is used
- GDPR and HIPAA compliant (no real data)
- Runs completely locally by default
- Flask secret key provides session security

## 🛠️ Troubleshooting

### Ollama Connection Issues

If you see "Ollama offline" but need AI generation:
1. Make sure Ollama is installed and running
2. Check that `ollama serve` is running in a terminal
3. The app will use mock data automatically if Ollama is unavailable

### Port Already in Use

If port 5000 is already in use, modify the last line of `app.py`:

```python
app.run(debug=True, host="0.0.0.0", port=8000)  # Change to 8000 or any available port
```

### CSV Export Not Working

Ensure you generate data first before trying to export.

## 📊 Sample Data Structure

### Customer
```json
{
  "customer_id": "CUST_10001",
  "company_name": "Northwind 1",
  "industry": "Healthcare",
  "employee_count": 70,
  "location": "City 1, State",
  "subscription_tier": "Professional",
  "annual_revenue": 65000,
  "churn_risk": "Low"
}
```

### Transaction
```json
{
  "transaction_id": "TXN_1_1",
  "customer_id": "CUST_10001",
  "date": "2024-10-01",
  "amount": 700,
  "type": "Sale",
  "payment_method": "Credit Card",
  "status": "Completed"
}
```

## 📝 License

Open source - Free to use and modify

## 🤝 Contributing

Feel free to fork and submit pull requests!

## 📞 Support

For issues or questions, please open an issue in the GitHub repository.

---

**Built with ❤️ for businesses that need realistic test data without privacy concerns.**
