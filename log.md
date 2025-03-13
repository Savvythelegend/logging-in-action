We'll follow an **intuitive learning approach**:  
✅ **Step 1:** What is logging & why use it? (Quick theory)  
✅ **Step 2:** Basic logging (Hands-on coding)  
✅ **Step 3:** Advanced logging (Different log levels, handlers, and formatting)  
✅ **Step 4:** Real-world use cases (ML pipeline logging, Flask API logs, file logging)  
✅ **Step 5:** Build a **mini-project** where logging actually helps you 🚀  

Let’s start with **Step 1: Understanding Logging** (Quick notes), and then we’ll jump into the hands-on part.  

---

## **📌 Step 1: What is Logging & Why Use It?**
### 🔹 **What is Logging?**  
Logging is a way to **track events in a program** while it's running. Instead of using `print()`, we use `logging` to:  
✅ **Debug** without cluttering the console  
✅ **Track errors** in production  
✅ **Save logs** to a file for future analysis  
✅ **Monitor ML model training** (loss, accuracy, data issues)  

### 🔹 **Why Not Just Use `print()`?**
❌ `print()` is temporary and doesn’t save logs.  
❌ You can’t control the **log level** (info, warning, error).  
❌ Hard to filter logs in a big application.  
✅ Logging is **structured**, saves data, and supports filtering.  

---

### **📌 Step 2: Hands-on - Basic Logging**
Try this in a Python script:  

```python
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Setting level to DEBUG
logging.debug("This is a DEBUG message")  # Debugging info
logging.info("This is an INFO message")   # General info
logging.warning("This is a WARNING message")  # Warning
logging.error("This is an ERROR message")  # Error
logging.critical("This is a CRITICAL message")  # Critical issue
```

### **🔹 What will you see in output?**
```
WARNING:root:This is a WARNING message
ERROR:root:This is an ERROR message
CRITICAL:root:This is a CRITICAL message
```
⚡ **Why no DEBUG or INFO messages?**  
Because by default, logging only **shows WARNING and above**. To include lower levels (`DEBUG`, `INFO`), we set **`level=logging.DEBUG`** in `basicConfig()`.  

---

### **📌 Step 3: Writing Logs to a File (Not Just Console)**
Modify your script to **log into a file**:  

```python
logging.basicConfig(filename="app.log", level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("This will be logged into app.log")
```

🔹 **Now, check `app.log`** file! It should contain something like:  
```
2025-03-13 12:45:00 - INFO - This will be logged into app.log
```

---

### **📌 Step 4: Real-World Use Cases**
#### **✅ 1. Logging in an ML Pipeline (Track Model Training)**
```python
import logging
import time

# Configure logging
logging.basicConfig(filename="ml_training.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Starting model training...")

# Simulating training
for epoch in range(1, 6):
    accuracy = 0.80 + (epoch * 0.02)  # Fake accuracy increase
    loss = 0.5 - (epoch * 0.05)  # Fake loss decrease
    logging.info(f"Epoch {epoch}: Accuracy = {accuracy}, Loss = {loss}")
    time.sleep(1)

logging.info("Model training completed!")
```
📝 **Use Case:** If your ML model fails mid-training, logs will help debug issues.  

---

#### **✅ 2. Logging in a Flask API (For Debugging Requests)**
```python
from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="server.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Welcome to the Flask API!"

@app.route("/error")
def error():
    logging.error("Error endpoint triggered!")
    return "This is an error!", 500

if __name__ == "__main__":
    app.run(debug=True)
```
📝 **Use Case:** Log API requests and errors for debugging.  

---

### **📌 Step 5: Mini Project - Build a "Smart Logger" for Data Processing**
#### **🛠️ Project Idea: Logging in a Data Processing Pipeline**
**Scenario:** You're processing a large CSV file, and you want to **log errors, track progress, and store logs**.  

#### **🔹 What we’ll do:**
✅ Read a **CSV file**  
✅ **Log missing values**  
✅ **Track processing time**  
✅ Save logs to `data_processing.log`  

#### **🔹 Code:**
```python
import logging
import pandas as pd
import time

# Configure logging
logging.basicConfig(filename="data_processing.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def process_csv(file_path):
    try:
        logging.info(f"Starting processing for {file_path}")
        start_time = time.time()

        # Load CSV
        df = pd.read_csv(file_path)

        # Check for missing values
        missing_values = df.isnull().sum().sum()
        if missing_values > 0:
            logging.warning(f"File {file_path} contains {missing_values} missing values")

        # Process data (Dummy operation)
        df.fillna("UNKNOWN", inplace=True)

        end_time = time.time()
        logging.info(f"Processing completed in {end_time - start_time:.2f} seconds")

    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")

# Run the function
process_csv("data.csv")
```

#### **🔹 How to Test?**
1️⃣ **Create a sample `data.csv` file** with missing values.  
2️⃣ **Run the script** → It will log missing values and processing time.  
3️⃣ **Check `data_processing.log`** for saved logs.  

📝 **Use Case:** Useful when handling big datasets in ML projects.  

---

### **📌 Recap & Next Steps**
✅ **Logging Basics** → `logging.basicConfig()`, log levels  
✅ **Writing Logs to a File**  
✅ **Real-World Examples** → ML pipeline, Flask API  
✅ **Mini Project** → Data Processing Logger  