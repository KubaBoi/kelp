
import os
import sys
import subprocess

if (len(sys.argv) == 1):
    name = "test"
else:
    name = sys.argv[1]

added_files = []

def doFile(file_name):
    file_path = os.path.abspath(file_name)
    dir_path = os.path.dirname(file_path)

    with open(file_path, "r") as f:
        data_lines = f.readlines()

    content = ""
    for line in data_lines:
        if (line.startswith(";import")):
            parts = line.split(" ")

            while " " in parts: 
                parts.remove("")
            line = ""
            for i in range(1, len(parts)):
                parts[i] = os.path.join(dir_path, parts[i].strip())
                if (parts[i] not in added_files):
                    if (os.path.exists(parts[i])):
                        line += doFile(parts[i])
                        print(parts[i])
                        added_files.append(parts[i])
                    else:
                        print(f"ERROR: {parts[i]} does not exists.")
                        exit(1)
        content += line

    return content + "\n\n"

print("Linking imports")
content = doFile(name + ".s")
with open(f"{name}_temp.s", "w") as f:
    f.write(content)

print("Assembling: " + name + ".s")

script_path = os.path.abspath(name)
dir_path = os.path.dirname(script_path)
exec_path = os.path.join(dir_path, "build.sh")

subprocess.call(["-d", script_path, name], executable=exec_path)
