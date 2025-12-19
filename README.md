# 🔐 Power BI IAM Security Dashboard  
**Enterprise Identity & Access Security Reporting**

## 📌 Overview

This project demonstrates how identity and access management (IAM) security data can be transformed into **clear, leadership-ready insights** using **Power BI**.

Instead of focusing on raw logs or SOC-style alerts, the dashboard emphasizes **risk visibility, control posture, and decision-making**, mirroring how IAM and cloud security teams communicate with stakeholders.

The project uses **simulated but realistic IAM event data**, generated and validated on Linux, and visualized in Power BI Desktop on Windows.

---

## 🎯 Project Goals

- Translate IAM security events into **actionable insights**
- Highlight **risky users and behaviors**
- Surface **authentication failures and high-risk activity**
- Demonstrate **security reporting maturity**, not just tooling usage

---

## 🧠 What This Project Demonstrates

- Power BI Desktop reporting and dashboard design  
- DAX measures for security analytics  
- IAM-focused security thinking (authentication, MFA, risk)  
- Analyst-level prioritization (who to investigate first)  
- Cross-platform workflow (Linux + Windows)  
- GitHub-based project documentation  

---

## 🛠️ Tools & Technologies

- **Power BI Desktop** (Windows)
- **DAX (Data Analysis Expressions)**
- **Python** (dataset generation)
- **Linux (Ubuntu)** for data prep & version control
- **Git & GitHub**
- **CSV-based security event data**

---

## 📊 Dashboard Features

### 🔹 KPI Metrics
- Total Login Attempts  
- Failed Login Attempts  
- High Risk Events  
- MFA Coverage Percentage  

### 🔹 Analytical Visuals
- Failed logins over time  
- High-risk activity by location  
- **Risk by User table** for investigation prioritization  

### 🔹 Investigation-Focused Design
The dashboard is structured to quickly answer:
- *Are authentication failures increasing?*  
- *Which users represent the highest risk?*  
- *Are MFA controls effectively applied?*  

---

## 📂 Repository Structure

```text
powerbi-security-dashboard/
├── data/
│   ├── iam_security_events.csv      # Simulated IAM security dataset
│   ├── generate_data.py             # Dataset generation script
│   └── IAM_Security_Dashboard.pbix  # Power BI dashboard file
│
├── screenshots/                     # Dashboard screenshots
│
└── README.md
```

> Note: Git does not track empty folders. Screenshots are added incrementally as the dashboard is finalized and polished.

---

## 🔄 Data Workflow

1. IAM security event data is generated and validated on Linux  
2. Dataset is stored as CSV and version-controlled in GitHub  
3. CSV is imported into Power BI Desktop  
4. DAX measures calculate security KPIs  
5. Visuals present leadership-ready insights  

---

## ⚡ Automation (Planned / Documented)

In an enterprise environment, the **High Risk Events** KPI would trigger a **Power BI data alert** integrated with **Power Automate** to notify stakeholders when thresholds are exceeded.

Because Power BI Service and Power Automate require a work or school tenant, automation is **documented conceptually** for this portfolio project rather than deployed live.

---

## 📸 Screenshots

Screenshots of the final dashboard are located in:

```text
screenshots/
```

---

## 🧪 Dataset Notes

- Data is **simulated for learning and portfolio purposes**
- No real user, tenant, or production data is included
- Dataset structure reflects common IAM event attributes:
  - Authentication method
  - MFA status
  - Risk level
  - Location
  - Device type

---

## 💼 How This Maps to Real Roles

This project aligns with responsibilities found in:
- IAM Analyst
- Cloud Security Analyst
- Security Operations (identity-focused)
- Security Reporting & GRC support roles

---

## 🚀 Future Enhancements

- Power BI Service publishing (enterprise tenant)
- Live Power Automate alerting
- Additional IAM signals (conditional access, device compliance)
- Executive summary page for leadership

---

## 📬 Author

**LaTerral Williams**  
IT & Cloud Security Professional  
DevTo: Adding Soon  
