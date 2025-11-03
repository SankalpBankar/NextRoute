# 🛰️ NextRoute 💻 🌐
A **Streamlit-based visual simulator** for the **Distance Vector Routing Algorithm**, which demonstrates how routers exchange routing information and update their routing tables until convergence.

## 📁 Project Directory Structure 🧠💬

```
NextRoute/
├── .gitignore            # 🛡️To exclude myenv and other temp files
├── app.py                # 🖥️🎨 Streamlit app (main simulator)
├── main.py               # ⚙️ Algorithm code
├── README.md             # 📖 Project overview and usage guide
└── requirements.txt      # ✅ Dependencies list

```

## 💡 Tech Stack 🛠️
- **Python** 🐍 — Core programming language for logic and data handling
- **Streamlit** 🌐 — For building the interactive web interface
- **Pandas** 📦 — Data handling
- **NetworkX** ⚡ — Manipulation of Graphs
- **Matplotlib** 📈 — Visualization


---

## ⚙️ Setup & Installation for NextRoute 📦🗺️
Follow these steps to set up and track the NextRoute:
### 1️⃣ Clone the Repository 📥
```sh
git clone https://github.com/SankalpBankar/NextRoute.git
cd NextRoute
```

### 2️⃣ Create a virtual environment 🐍
```sh
python -m venv myenv
```

### 3️⃣ Activate the environment 📦
On Windows (PowerShell):
```sh
.\myenv\Scripts\activate
```

⚠️ If you get an error saying "running scripts is disabled", run this as Administrator:
```sh
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

On macOS/Linux:
```sh
source myenv/bin/activate
```

### 4️⃣ Install dependencies 📦
```sh
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit app 🚀
```sh
streamlit run app.py
```

## 🛠️ Troubleshooting 🚨

### 1. ValueError ⚠️: Unknown format code 'f' for object of type 'str'
Apply formatting only to numeric columns:
```sh
st.dataframe(df_main.style.format(
    {col: "{:.1f}" for col in df_main.select_dtypes(include="number").columns},
    na_rep="∞"
))
```

### 2. AttributeError 🧩: module 'streamlit' has no attribute 'experimental_rerun'
Replace with:
```sh
st.rerun()
```

### 3. PowerShell Activation Error ⚡
Open PowerShell as Administrator and run:
```sh
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then retry:
```sh
.\myenv\Scripts\activate
```

## 💻⚙️Contributions
### 1️⃣ Sankalp Bankar (A7-B1-17)
### 2️⃣ Anish Makhija  (A7-B1-01)
### 3️⃣ Deeya Saoji    (A7-B1-10)
