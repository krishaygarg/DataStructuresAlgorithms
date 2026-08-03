import os
import urllib.parse

def generate_readme():
    base_dir = "Data Structures & Algorithms"
    if not os.path.exists(base_dir):
        print("Base directory does not exist")
        return

    folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])
    index_md = []
    for folder in folders:
        clean_name = " ".join([word.capitalize() for word in folder.split("-")])
        url_path = "./Data%20Structures%20%26%20Algorithms/" + urllib.parse.quote(folder)
        index_md.append(f"*   [{clean_name}]({url_path})")
    
    index_content = "\n".join(index_md)

    readme_template = f"""# Data Structures & Algorithms

A curated archive of solutions to classical data structures and algorithms problems.

---

## 📈 Progress Tracker
*   **Total Problems Solved**: {len(folders)}

---

## 📂 Repository Layout
All solutions are written in Python and organized by problem identifier:
```
Data Structures & Algorithms/
  <problem-id>/
    submission-0.py   ← Accepted Solution
```

---

## 🗺️ Solved Problems Index

{index_content}

---

## ⚙️ Running Locally
You can run any solution file directly using Python:
```bash
python3 "Data Structures & Algorithms/<problem-id>/submission-0.py"
```

---

*Synced automatically from [NeetCode.io](https://neetcode.io) using the GitHub Sync integration.*
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_template)

if __name__ == "__main__":
    generate_readme()
