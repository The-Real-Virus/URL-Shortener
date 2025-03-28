# 💀URL-Shortener💀

## 📜 Description

This Python script helps you shorten long URLs using the **TinyURL API**. It supports both command-line arguments and an interactive mode, allowing users to enter URLs manually. The script also includes **error handling**, **clipboard support**, and a **user-friendly interface** with color-coded messages.

---

## 🔑 Features

✅ **Interactive Mode** – Enter URLs manually if not provided as arguments.  
✅ **Bulk Shortening** – Process multiple URLs at once.  
✅ **Error Handling** – Detects invalid URLs and handles API failures gracefully.  
✅ **Clipboard Support** – Automatically copies shortened URLs for easy pasting.  
✅ **Color-coded Output** – Uses colorama for improved readability.  
✅ **Lightweight & Fast** – No unnecessary dependencies.  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  

>sudo apt upgrade  

Step 2: install Dependencies  
>sudo apt install python3-pyperclip  

>sudo apt install python3-colorama  

Step 3: Clone the repository  
>git clone https://github.com/The-Real-Virus/URL-Shortener.git  

Step 4: Go to the Tool Directory where u clone it  
>cd URL-Shortener  

Step 5: After Completing the process now u can run script  
>python3 short.py  

## 💡 Tips !

- Use the **command-line mode** to quickly shorten URLs without prompts:
  ```sh
  python script.py https://example.com https://google.com
  ```
- If you forget to provide URLs, the script will **ask you to enter them interactively**.
- The shortened URL(s) **automatically get copied to your clipboard**—no need to manually copy!
- If you face an issue, check the **Troubleshooting** section below.

---

## 🤝 Follow the Prompts !

- If no URLs are provided as arguments, the script will **prompt you to enter them manually**.
- **Multiple URLs?** Separate them with commas in interactive mode.
- You'll get instant feedback on invalid URLs.
- Successful shortened URLs will be displayed and copied to the clipboard.

---

## ⚙️ Troubleshooting

**Issue:** The script is not copying URLs to the clipboard.
**Solution:** Install the `pyperclip` library if missing:
```sh
sudo apt install python3-pyperclip
```

**Issue:** No color-coded output in the terminal.
**Solution:** Ensure `colorama` is installed:
```sh
sudo apt install python3-colorama
```

**Issue:** Getting an error while shortening URLs.
**Solution:**
- Ensure the **URL is correctly formatted** (e.g., `https://example.com`).
- Check your **internet connection**.
- TinyURL API might be down—try again later.

---

## 🛠️MODIFICATION 

IF U WANT TO MODIFY OR USE THE SCRIPT IN UR PROJECTs , CONSIDER GIVING CREDITS !  

## 📂 Example Output

	### **Command-Line Mode**
	```sh
	python script.py https://example.com
	```
	**Output:**
	```
	Shortened: http://tinyurl.com/xyz123
	Shortened URLs copied to clipboard!
	```

	### **Interactive Mode**
	```sh
	python script.py
	```
	**Prompt:**
	```
	Enter URL(s) (comma-separated): https://example.com, https://google.com
	```
	**Output:**
	```
	Shortened: http://tinyurl.com/xyz123
	Shortened: http://tinyurl.com/abc789
	Shortened URLs copied to clipboard!
	```

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
