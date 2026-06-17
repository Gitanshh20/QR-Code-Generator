# 💳 UPI QR Code Generator (Python)

Generate a **UPI payment QR Code** instantly by entering your UPI ID. This simple Python project creates a QR code that can be scanned with any UPI-supported payment app such as PhonePe, Google Pay, Paytm, or BHIM.

---

## 📸 Preview

```
Enter Your UPI Id: yourname@upi
```

A QR code will be generated and displayed automatically.

---

## ✨ Features

- ⚡ Generate UPI payment QR codes instantly
- 📝 Accepts any valid UPI ID
- 📱 Compatible with all UPI payment apps
- 🖼️ Automatically opens the generated QR code
- 💻 Beginner-friendly Python project

---

## 🛠️ Built With

- Python 3
- qrcode Library

---

## 📂 Project Structure

```
UPI-QR-Code-Generator/
│
├── main.py
└── README.md
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/UPI-QR-Code-Generator.git
```

Move into the project directory

```bash
cd UPI-QR-Code-Generator
```

Install the required package

```bash
pip install qrcode[pil]
```

---

## ▶️ Usage

Run the program

```bash
python main.py
```

Enter your UPI ID

```
Enter Your UPI Id: example@upi
```

The QR code will automatically open on your screen.

---

## 🧠 How It Works

1. Takes your UPI ID as input.
2. Creates a UPI payment URL.
3. Converts the URL into a QR code.
4. Displays the QR code for payment.

---

## 📄 Example

Input

```
Enter Your UPI Id: demo@oksbi
```

Generated UPI URL

```
upi://pay?pa=demo@oksbi&pn=Recipient%20Name&mc=1234
```

---

## 📌 Requirements

- Python 3.x
- qrcode
- Pillow

Install using

```bash
pip install qrcode[pil]
```

---

## 🚀 Future Improvements

- Save QR code as PNG
- Custom recipient name
- Enter payment amount
- Add payment note
- Custom QR colors
- GUI using Tkinter or CustomTkinter
- Logo inside QR code
- Batch QR Generator

---

## 🤝 Contributing

Contributions are welcome!

If you have ideas or improvements:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---
## 👨‍💻 Author

**Gitansh**  
*Future AI Engineer* 🚀
- 💻 Passionate about Python, AI, Machine Learning, and Open Source.
- 🎯 Building projects to become a professional AI Engineer.
---
