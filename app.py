import os
import json
import csv
from datetime import datetime
from io import StringIO

import requests
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "my-local-secret-key-12345")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

class SyntheticDataGenerator:
    def __init__(self):
        self.api_url = OLLAMA_URL
        self.model = OLLAMA_MODEL

    def call_model(self, prompt):
        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=120
            )
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "")
            return None
        except Exception:
            return None

    def generate_customers(self, count=5):
        prompt = f"""
        Generate exactly {count} realistic but completely fictional B2B customer profiles.
        Return JSON array only. Each object must contain:
        customer_id, company_name, industry, employee_count, location, subscription_tier, annual_revenue, churn_risk
        Use realistic values.
        """
        result = self.call_model(prompt)
        if result:
            try:
                start = result.find("
")
                end = result.rfind("]") + 1
                return json.loads(result[start:end])
            except Exception:
                pass
        return self.mock_customers(count)

    def generate_transactions(self, customer_count=3, per_customer=5):
        prompt = f"""
        Generate {customer_count * per_customer} realistic business transactions.
        Return JSON array only. Each object must contain:
        transaction_id, customer_id, date, amount, type, payment_method, status
        Use realistic values.
        """
        result = self.call_model(prompt)
        if result:
            try:
                start = result.find("
")
                end = result.rfind("]") + 1
                return json.loads(result[start:end])
            except Exception:
                pass
        return self.mock_transactions(customer_count, per_customer)

    def generate_employees(self, count=5):
        prompt = f"""
        Generate exactly {count} realistic employee records.
        Return JSON array only. Each object must contain:
        employee_id, full_name, email, department, job_title, salary, start_date, location, performance_rating
        """
        result = self.call_model(prompt)
        if result:
            try:
                start = result.find("
")
                end = result.rfind("]") + 1
                return json.loads(result[start:end])
            except Exception:
                pass
        return self.mock_employees(count)

    def generate_feedback(self, count=5):
        prompt = f"""
        Generate {count} realistic customer feedback entries.
        Return JSON array only. Each object must contain:
        feedback_id, customer_id, date, rating, text, sentiment, category
        """
        result = self.call_model(prompt)
        if result:
            try:
                start = result.find("
")
                end = result.rfind("]") + 1
                return json.loads(result[start:end])
            except Exception:
                pass
        return self.mock_feedback(count)

    def mock_customers(self, count):
        customers = []
        for i in range(1, count + 1):
            customers.append({
                "customer_id": f"CUST_{10000 + i}",
                "company_name": f"Northwind {i}",
                "industry": ["Healthcare", "Finance", "Retail", "Tech", "Manufacturing"][i % 5],
                "employee_count": 50 + i * 20,
                "location": f"City {i}, State",
                "subscription_tier": ["Starter", "Professional", "Enterprise"][i % 3],
                "annual_revenue": 50000 + i * 15000,
                "churn_risk": ["Low", "Medium", "High"][i % 3]
            })
        return customers

    def mock_transactions(self, customer_count, per_customer):
        transactions = []
        for c in range(1, customer_count + 1):
            for t in range(1, per_customer + 1):
                transactions.append({
                    "transaction_id": f"TXN_{c}_{t}",
                    "customer_id": f"CUST_{10000 + c}",
                    "date": f"2024-10-{(t % 28) + 1:02d}",
                    "amount": 200 + (t * 500),
                    "type": ["Sale", "Refund", "Subscription", "Support"][t % 4],
                    "payment_method": ["Credit Card", "ACH", "Invoice"][t % 3],
                    "status": ["Completed", "Failed", "Refunded"][t % 3]
                })
        return transactions

    def mock_employees(self, count):
        employees = []
        departments = ["Engineering", "Sales", "Marketing", "HR", "Finance"]
        for i in range(1, count + 1):
            employees.append({
                "employee_id": f"EMP_{10000 + i}",
                "full_name": f"Employee {i}",
                "email": f"employee{i}@company.com",
                "department": departments[i % len(departments)],
                "job_title": "Senior Analyst" if i % 2 == 0 else "Manager",
                "salary": 60000 + i * 5000,
                "start_date": "2022-01-15",
                "location": "Remote" if i % 2 == 0 else "New York",
                "performance_rating": 3 + (i % 3)
            })
        return employees

    def mock_feedback(self, count):
        feedback = []
        for i in range(1, count + 1):
            feedback.append({
                "feedback_id": f"FB_{10000 + i}",
                "customer_id": f"CUST_{10000 + (i % 5 + 1)}",
                "date": "2024-10-15",
                "rating": (i % 5) + 1,
                "text": f"Customer feedback sample {i}. Product is useful and reliable.",
                "sentiment": ["Positive", "Neutral", "Negative"][i % 3],
                "category": ["Product Quality", "Pricing", "Customer Service"][i % 3]
            })
        return feedback

generator = SyntheticDataGenerator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def status():
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        if resp.status_code == 200:
            return jsonify({"status": "online"})
        return jsonify({"status": "offline"})
    except Exception:
        return jsonify({"status": "offline"})

@app.route("/api/generate/customers", methods=["POST"])
def generate_customers():
    count = int(request.json.get("count", 5))
    return jsonify({"data": generator.generate_customers(count)})

@app.route("/api/generate/transactions", methods=["POST"])
def generate_transactions():
    customer_count = int(request.json.get("customer_count", 3))
    per_customer = int(request.json.get("per_customer", 5))
    return jsonify({"data": generator.generate_transactions(customer_count, per_customer)})

@app.route("/api/generate/employees", methods=["POST"])
def generate_employees():
    count = int(request.json.get("count", 5))
    return jsonify({"data": generator.generate_employees(count)})

@app.route("/api/generate/feedback", methods=["POST"])
def generate_feedback():
    count = int(request.json.get("count", 5))
    return jsonify({"data": generator.generate_feedback(count)})

@app.route("/api/export/<data_type>", methods=["POST"])
def export_data(data_type):
    rows = request.json.get("data", [])
    if not rows:
        return jsonify({"error": "No data"}), 400

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

    return send_file(
        StringIO(output.getvalue()),
        mimetype="text/csv",
        as_attachment=True,
        download_name=f"{data_type}.csv"
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
