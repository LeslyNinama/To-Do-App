import streamlit as st
import functions
todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.date_input('Date', format= 'DD-MM-YYYY')
st.title('My To-Do App')
st.subheader('This Is To Increase Your Productivity')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
new_todo = st.text_input(label="", placeholder='Enter New Todo', on_change=add_todo, key='new_todo')

