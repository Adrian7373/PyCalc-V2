## 🧮 PyCalc v2

A **modern, responsive calculator app** built with **PySide6**.
This version focuses on clean architecture, improved responsiveness, and code readability — ideal for beginners learning GUI design and event handling in Python.

---

### 🚀 Features

* **Responsive UI** — Adapts gracefully to different window sizes.
* **Simple & Minimal Layout** — Clear and consistent button arrangement using `QGridLayout`.
* **Expression Evaluation** — Safely computes mathematical expressions via `simpleeval`.
* **Custom Button Styling** — Consistent look and feel with the `CustomButtons` class.
* **Clear & Backspace Controls** — `C` clears all, `CE` deletes the last character.
* **Arithmetic Operations Supported:**

  * Addition (+)
  * Subtraction (−)
  * Multiplication (×)
  * Division (÷)
  * Modulo (%)
  * Decimal support (.)

---

### 🧰 Technologies Used

* **Python 3.x**
* **PySide6** — For GUI components and layout management
* **simpleeval** — For safe evaluation of mathematical expressions

---

### 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Adrian7373/pyside6-calculator-v2.git
   cd pyside6-calculator-v2
   ```

2. Install dependencies:

   ```bash
   pip install PySide6 simpleeval
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

### 🖼️ UI Overview

| Component            | Description                                  |
| -------------------- | -------------------------------------------- |
| **QLineEdit**        | Displays user input and results              |
| **CustomButtons**    | Styled QPushButtons for digits and operators |
| **GridButtonHolder** | Manages button placement using `QGridLayout` |
| **MainWindow**       | Root window container                        |
| **MainWidget**       | Wraps main content with `QVBoxLayout`        |

---

### 🧠 Code Highlights

* Each button connects to a dedicated event handler method.
* Modular design — UI and logic are organized into clean, separate classes.
* Uses `QSizePolicy.Expanding` for responsive resizing.
* Safe and readable mathematical evaluation with `simple_eval()`.

---

### 💡 Future Enhancements

* Keyboard input support
* Dark/Light mode theme toggle
* Parentheses and advanced math operations
* Expression history panel

---

### 📸 Preview (optional)

<img width="401" height="532" alt="image" src="https://github.com/user-attachments/assets/596e128b-4da9-4a05-9e5b-ce8066f17829" />


---

### 👨‍💻 Author

**Adrian Ablaza**
Student Developer | Python & Web Enthusiast
📚 Nueva Ecija University of Science and Technology
🖥️ *“Code clean, design clear.”*
