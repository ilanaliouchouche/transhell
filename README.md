🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧

# `trans`: Direct Translation in Terminal for Text and .txt Files (Linux)

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
trans (--lang|-l) <INPUT LANG> ((--text|-t) "<PROMPT>" | (--file|-f) "<FILENAME>")
```

### Parameters:
- `--lang` or `-l`: Specifies the target language for translation.
- `--text` or `-t`: Provide the text you want to translate in single quotes.
- `--file` or `-f`: Provide the filename of the .txt file you want to translate.

## 📋 To Do

In the upcoming development stages, we plan to:

1. **Streaming Integration**: We aim to incorporate a streaming feature in the terminal, allowing for token-by-token translation generation, for a more seamless and interactive user experience.

2. :warning::warning::warning: **Data Collection**: Collect PDFs of mini dictionaries from language1 to language2.

3. **Embedding**: After collecting the documents, build a Vector Database by embedding the documents

🌍
