import csv
import random
from datetime import datetime, timedelta

users = [
    "jane.doe@company.com",
    "john.smith@company.com",
    "alex.lee@company.com",
    "sam.taylor@company.com"
]

event_types = ["LoginSuccess", "LoginFailure", "MFAChallenge"]
auth_methods = ["Password", "Password+MFA"]
locations = ["USA", "Canada", "UK", "Nigeria", "Unknown"]
risk_levels = ["Low", "Medium", "High"]
devices = ["Windows", "Mac", "Mobile"]

start_date = datetime(2025, 1, 1)

with open("iam_security_events.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "EventDate", "UserPrincipalName", "EventType", "AuthMethod",
        "MFAEnabled", "DeviceType", "Location", "RiskLevel",
        "FailureReason", "SourceIP"
    ])

    for i in range(60):
        date = start_date + timedelta(days=random.randint(0, 10))
        user = random.choice(users)
        event = random.choice(event_types)
        mfa = random.choice([True, False])
        risk = random.choice(risk_levels)

        writer.writerow([
            date.strftime("%Y-%m-%d"),
            user,
            event,
            random.choice(auth_methods),
            mfa,
            random.choice(devices),
            random.choice(locations),
            risk,
            "InvalidPassword" if event == "LoginFailure" else "",
            f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        ])

