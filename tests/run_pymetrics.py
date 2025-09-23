import json
import sys
from pymetrics.analysis import analyze_paths

# Change this to your file(s) you want to analyze
files_to_analyze = ["banking.py"]

# Run pymetrics
results = analyze_paths(files_to_analyze)

# Save results to JSON
with open("oo_metrics3.json", "w") as f:
    json.dump(results, f, indent=4)

print("OO metrics saved to oo_metrics.json")

