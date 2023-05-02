
import re

with open("test.k", "r", encoding="utf-8") as f:
    source = f.read()

method_reg = re.compile(r"method\s+[a-zA-Z0-9_]+\s*\([a-zA-Z0-9_,\s]+\)\s*\{[\sa-zA-Z0-9,_\.\+\-\*\;\=\/\\\(\)\'\"\$]+\}")
methods = re.findall(method_reg, source)

for m in methods:
    print(m + "\n===\n")
