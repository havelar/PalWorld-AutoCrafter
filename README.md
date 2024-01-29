# PalWorld Auto-Crafter
Script in pure Python that enables auto-crafting in PalWorld by holding the 'F' key.

## Usage
1. Run **autoCrafter.exe**
2. Press **F12** to start auto-crafting by holding the 'F' key
3. Press **W, A, S, D or F** to stop holding 'F' and cease auto-crafting
4. Use **Pause / Break** to close the program

## Compilation
If you want to compile the **EXE** yourself using *PyInstaller*

(You migh have to allow the exe file to exists in your AntiVirus)

### 1) Create a new Virtual Environment
```bash
python -m venv .venv
```

### 2) Activate the Virtual Environment
On Windows
```bash
.venv\Scripts\activate
```
On MacOS/Linux:
```bash
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the Compilation Script
```bash
python compile.py
```
This will generate the **autoCrafter.exe** on the root folder.