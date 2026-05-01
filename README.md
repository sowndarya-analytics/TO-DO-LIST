# 📝 To-Do List App (Streamlit)

A Streamlit-based To-Do app using session state to persist tasks during runtime. Users can add tasks via input, view them as a numbered list, and delete items with dynamic buttons. The app updates instantly using rerun, demonstrating interactive UI handling and state management.

## 🚀 Features
- ➕ Add tasks through a text input field  
- 📌 Display tasks as a numbered list  
- ❌ Delete individual tasks instantly  
- ⚡ Real-time updates using `st.experimental_rerun()`  
- 🧠 Persistent task handling within a session using `st.session_state`  

## 🛠️ Tech Stack
- Python  
- Streamlit  

## ⚙️ How It Works
- Tasks are stored in `st.session_state` to maintain data during runtime  
- Each task is dynamically rendered with a unique delete button  
- On deletion, the app reruns to reflect updated task list instantly  

## ▶️ Run Locally
```bash
pip install streamlit
streamlit run app.py
