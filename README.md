# 26_Endeavor

## How to Add a Python Interpreter Manually

If the version you want isn't in the list, you must add it manually. 

### Steps:
1. **Access Settings:** Follow the *Via Settings* steps mentioned above.
2. **Add Interpreter:** Click the **Add Interpreter** link or the **gear icon** next to the dropdown and select **Add Local Interpreter**.
3. **Choose Environment Type:** Select the type of environment you want to add:
    * **Virtualenv:** Create a new or use an existing virtual environment.
    * **System Interpreter:** Use the standard Python installation on your machine.
    * **Conda/Poetry/Pipenv:** Select these if you use specific package managers.
4. **Locate Executable:** Browse to the location of your Python executable and click **OK**.
    * *Windows:* `python.exe`
    * *Linux/macOS:* `/usr/bin/python3`


## 📂 File Handling & Portability

To ensure the script runs on any computer (Windows, Mac, or Linux) without manual path configuration, this script includes **Relative Paths** via the `pathlib` library.

### The Path Logic:
Instead of a "hardcoded" path like `C:\Users\Name\Documents...`, the code uses:
```python 
file_path = Path(__file__).parent / "your_example_file.xlsx"
```

## 💡 Technical Deep Dive: String Manipulation in Pandas

### The `.str` Accessor & Method Chaining
In this project, text cleaning is performed using vectorized string operations. A common pattern used is:
```python
df[col] = df[col].str.strip().str.lower()
```

### Why call .str twice?
**The Accessor:** Pandas Series are not strings; they are containers. The `.str` attribute is an "accessor" that grants access to string-specific methods.

**The Return Type:** Each method (like `.strip()`) returns a new Series. Because the return is a Series and not a raw string, we must re-invoke the `.str` accessor to perform the next operation (like `.lower()`).

**Efficiency:** While it looks repetitive, this is "vectorized," meaning Pandas performs the operation on the entire column at once in C-speed, rather than looping through rows in slow Python.

