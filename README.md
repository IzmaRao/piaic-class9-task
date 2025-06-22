
# 🐍 PIAIC Class 9 Python CLI Projects – Batch 71

This repository contains two Python command-line interface (CLI) projects developed as part of the **PIAIC Quarter 1 – Python Programming** course (Class 9, Batch 71), under the supervision of **Sir Hamzah Syed** and **Sir Okasha**.

---

## 📁 Task 1: Contact Manager using CSV

### 📝 Description

This is a simple CLI-based **Contact Manager** that allows users to store and manage contact information using a CSV file. It demonstrates file handling, set operations, user interaction through menus, and colored terminal output.

---

### 🔧 Features

- ➕ Add new contacts (name and phone number)
- 📖 View all saved contacts from a CSV file
- 🚫 Prevent duplicate contact names using Python `set`
- 🎨 Colorful terminal output using `colorama`
- 📋 Interactive options menu via `inquirer`

---

### 📂 contacts.csv Format

```
name,phone
Hoorain,03001234567
```

---

### 📦 Requirements

Install the required Python packages:

```bash
pip install inquirer colorama
```

---

### ▶️ How to Run

```bash
python contact_manager.py
```

---

### 💻 Sample Output

```
? What would you like to do? (Use arrow keys)
❯ Add Contact
  View Contacts
  Exit

✅ Contact added successfully!
📖 Contacts List:
Name: Ali, Phone: 03001234567
```

---

## 🧠 Task 2: National Quiz Game using Questionary

### 📝 Description

This is a CLI-based **Quiz Game** built using the `questionary` module. It presents multiple-choice questions based on general knowledge about **Pakistan**, checks the answers, and provides explanations along with real-time scoring.

---

### 🔧 Features

- 🎯 Multiple-choice quiz with 6 questions
- 💡 Explanations for correct answers
- ✅ Instant feedback for each question
- 🧮 Score counter after every answer
- 🏁 Final score display at the end

---

### 📦 Requirements

Install the required Python package:

```bash
pip install questionary
```

---

### ▶️ How to Run

```bash
python pakistan_quiz.py
```

---

### 💻 Sample Output

```
? Who was the first Women Prime Minister of Pakistan? 
❯ Benazir Bhutto
  Sheikh Hasina Wazzed
  Hina Rabbani Khar
  None of These
✅ Correct! Benazir Bhutto is the First Woman Prime Minister of Pakistan
Current Score: 1
```

---

## 🎓 What I Learned

- 📄 Working with CSV files using the `csv` module
- 📦 Installing and using third-party packages with `pip`
- 🧠 Using `set` to avoid duplicates in Python
- 🎨 Improving CLI UI with `colorama`
- 🧪 Building interactive apps with `inquirer` and `questionary`

---

## 📚 Class Info

- **Batch**: 71
- **Course**: PIAIC Quarter 1 – Python Programming
- **Instructors**: Sir Hamzah Syed & Sir Okasha
- **Class Link**: [Class 9 Code](https://github.com/syeda-hoorain-ali/piaic-classes/tree/main/quater-1-python/class-9)

---

## 🙋‍♀️ Author

**Izma Rao**  
GitHub: [@IzmaRao](https://github.com/IzmaRao)  
LinkedIn: [linkedin.com/in/izma-21i](https://www.linkedin.com/in/izma-21i/)  
