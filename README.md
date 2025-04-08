# instageram-py

A simple Python script that analyzes your Instagram data and identifies users who don’t follow you back.

## 🔍 What It Does

This script reads your Instagram data exports:

- `followers.json` – a list of people who follow you
- `following.json` – a list of people you follow

It then compares both lists and outputs the accounts you follow who **aren’t following you back**.

---

## 📁 How to Get Your Instagram Data

1. Go to [Instagram Data Download](https://www.instagram.com/download/request/)
2. Request your data in **JSON format**
3. Once downloaded, extract the ZIP and find:
   - `followers.json` under `followers_and_following/`
   - `following.json` under the same folder

---

## ⚙️ How to Use

1. Clone this repo:

   ```bash
   git clone https://github.com/ramadiansyah/instageram-py.git
   cd instageram-py
   ```

2. Place `followers.json` and `following.json` inside json folder.

3. Run the script:

   ```bash
   python instageram.py
   ```

4. The script will print a list of usernames who don’t follow you back.

---

## 🐍 Requirements

- Python 3.x
- No external libraries needed (just uses built-in `json`)

---

## 💡 Example Output

```text
Accounts not following you back:
- @username1
- @username2
- @username3
```

---

## 📜 License

MIT License. Feel free to use, modify, and share.


