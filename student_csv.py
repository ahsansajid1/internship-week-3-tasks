import csv
import json

# CSV file read karo
with open("data.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)         
    rows = list(reader)      

# JSON file me write karo
with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(rows, json_file, indent=4, ensure_ascii=False)

print("CSV converted to JSON successfully! data.json")
