
# Commande `trans`: Direct Translation in Terminal for Text and .txt Files (Linux)

Easily translate text or content from .txt files directly within your terminal using the `trans` command.

## 🚀 Installation Guide

Follow these steps to install the `trans` command on your system:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ilanaliouchouche/transhell.git
    ```
2. **Grant Execution Permission**:
   Navigate to the project directory in your terminal:
    ```bash
    cd <repository-directory-name>
    ```
   Then, grant execution permission to the installation script:
    ```bash
    chmod +x install.sh
    ```

3. **Run the Installation Script**:
    ```bash
    sudo ./install.sh
    ```

4. **Close the Terminal**.

## 📘 Usage Guide

To use the `trans` command, follow the structure below:

```bash
trans (--lang|-l) <INPUT LANG> ((--text|-t) '<PROMPT>' | (--file|-f) '<FILENAME>')
```

### Parameters:
- `--lang` or `-l`: Specifies the target language for translation.
- `--text` or `-t`: Provide the text you want to translate in single quotes.
- `--file` or `-f`: Provide the filename of the .txt file you want to translate.

 🌍