import json
import re
from collections import Counter

# Store request counts, unique IPs, and total requests
paths = Counter()
ips = set()
total = 0

# Read the access log
with open("/app/access.log", "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        total += 1

        # Extract client IP
        ip = line.split()[0]
        ips.add(ip)

        # Extract requested URL path
        match = re.search(
            r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH)\s+(\S+)',
            line
        )

        if match:
            paths[match.group(1)] += 1

# Prepare report
report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": paths.most_common(1)[0][0] if paths else None,
}

# Write report to JSON file
with open("/app/report.json", "w") as out:
    json.dump(report, out, indent=4)

print("Report successfully written to /app/report.json")
