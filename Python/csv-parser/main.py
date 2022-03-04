from csv import DictReader
import json

reader = DictReader(open("username-password-recovery-code.csv"), delimiter = ";")
jsonData = json.dumps(list(reader), indent=2)

print(jsonData)