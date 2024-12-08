# 🔥 SCRATCHPER v1 🔍

Welcome to the **SCRATCHPER v1**!  
This tool allows you to check the availability of usernames using a responsive, animated, and visually appealing interface directly in your terminal. 🌟  

---

## ✨ Features

- **Responsive Design** 🖥️: ASCII art and interface adapt to terminal size.  
- **Animated Intro** 🎥: Enjoy a stylish animation in shades of red.  
- **Interactive Menu** 📋: Choose options easily via an intuitive menu.  
- **Progress Bar** 📊: Visual feedback on the checking progress.  
- **Customization** 🛠️: Modify the API endpoint directly from the interface.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.x installed along with the `requests` and `colorama` libraries.  
Install dependencies using:
```bash
pip install requests colorama
```

---

### Setup
1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/kyrazzx/scratchper.git
   cd scratchper
   ```
2. Create a `list.txt` file in the same directory containing one username per line:
   ```plaintext
   user1
   user2
   testuser
   ...
   ```

---

### Usage
Run the script with:
```bash
python main.py
```
 
1. Use the **interactive menu** to:
   - Start the username availability check.  
   - Change the API endpoint if needed.  
   - Exit the tool gracefully.  
3. **Output**: Available usernames are saved in an `output.txt` file.  

---

## 🎨 Preview

### Intro Animation:
```
                                                                                                                                              
         ______        _____        _____         _____   _________________      _____    ____   ____      _____        ______        _____   
     ___|\     \   ___|\    \   ___|\    \    ___|\    \ /                 \ ___|\    \  |    | |    | ___|\    \   ___|\     \   ___|\    \  
    |    |\     \ /    /\    \ |    |\    \  /    /\    \\______     ______//    /\    \ |    | |    ||    |\    \ |     \     \ |    |\    \ 
    |    |/____/||    |  |    ||    | |    ||    |  |    |  \( /    /  )/  |    |  |    ||    |_|    ||    | |    ||     ,_____/||    | |    |
 ___|    \|   | ||    |  |____||    |/____/ |    |__|    |   ' |   |   '   |    |  |____||    .-.    ||    |/____/||     \--'\_|/|    |/____/ 
|    \    \___|/ |    |   ____ |    |\    \ |    .--.    |     |   |       |    |   ____ |    | |    ||    ||    |||     /___/|  |    |\    \ 
|    |\     \    |    |  |    ||    | |    ||    |  |    |    /   //       |    |  |    ||    | |    ||    ||____|/|     \____|\ |    | |    |
|\ ___\|_____|   |\ ___\/    /||____| |____||____|  |____|   /___//        |\ ___\/    /||____| |____||____|       |____ '     /||____| |____|
| |    |     |   | |   /____/ ||    | |    ||    |  |    |  |`   |         | |   /____/ ||    | |    ||    |       |    /_____/ ||    | |    |
 \|____|_____|    \|___|    | /|____| |____||____|  |____|  |____|          \|___|    | /|____| |____||____|       |____|     | /|____| |____|
    \(    )/        \( |____|/   \(     )/    \(      )/      \(              \( |____|/   \(     )/    \(           \( |_____|/   \(     )/  
     '    '          '   )/       '     '      '      '        '               '   )/       '     '      '            '    )/       '     '   
                         '                                                         '                                       '                     
Made by Kyra
```

### Interactive Menu:
```
-----------------------------------------
                Main Menu                
-----------------------------------------
[1] Start Username Check
[2] Change API Endpoint
[3] Exit
```

---

## 🛠️ Customization

### API Endpoint
The default API endpoint is:
```
https://api.scratch.mit.edu/accounts/checkusername/
```
Change it directly in the script or via the **interactive menu**.

---

## ❤️ Contributing
We welcome contributions!  
Feel free to open issues or submit pull requests to enhance this tool.

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

### 🌟 Star this repo if you find it useful!  
```
⭐ GitHub: https://github.com/kyrazzx/scratchper/
```
```
