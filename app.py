import streamlit as st

# Title
st.title("📝 To-Do List App")

# Initialize task list in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box to add task
task = st.text_input("Enter a new task:")

# Add button
if st.button("➕ Add Task"):
    if task.strip() != "":
        st.session_state.tasks.append(task)
        st.success("Task Added Successfully!")
    else:
        st.warning("Please enter a task!")

st.write("---")

# Display tasks
st.subheader("📌 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet. Add one above!")
else:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])

        # Task text
        col1.write(f"{i+1}. {t}")

        # Delete button
        if col2.button("❌", key=i):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()