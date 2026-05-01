# 📝 To-Do List App (Streamlit)

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-Click%20Here-green)](https://to-do-list-site.streamlit.app/)

A lightweight and interactive To-Do List web app built using **Streamlit**, focusing on real-time UI updates and session-based state management.

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
