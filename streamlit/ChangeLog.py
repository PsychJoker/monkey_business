import streamlit as st

def update_session_state(key, action, value):
    """
    Args:
        key (str):key in st.session_state.
        action (str):type of change.
        value:associated value.
    """
    if key == "data":
        if action == "add":
            st.session_state.data.append(value)
        elif action == "remove" and value in st.session_state.data:
            st.session_state.data.remove(value)
    st.session_state.change_log.append({"key": key, "action": action, "value": value})


def undo():
    if st.session_state.change_log:
        # Remove the last change from the log
        last_change = st.session_state.change_log.pop()
        
        # Extract the key (attribute name) from the last change
        attribute = last_change["key"]
        
        # Handle undo logic based on the attribute
        if attribute == "class_attr":
            st.session_state.class_attr = None  # Reset to default or previous value
            st.write(f"Undo: Reset {attribute}")
        elif attribute == "transform":
            st.session_state.transform_column = None
            st.session_state.transform_type = None
            st.write(f"Undo: Reversed transformation on column")
        else:
            st.write("Undo: No specific action for this change")


st.title("Change Log")

if st.session_state.data:
    st.write("Current Data:")
    for item in st.session_state.data:
        st.write(item)

    selected_item = st.selectbox("Select an item to remove:", st.session_state.data)
    if st.button("Remove Selected Item"):
        update_session_state("data", "remove", selected_item)
        st.experimental_rerun()

if st.button("Undo Last Change"):
    undo()
    st.experimental_rerun()

if st.checkbox("Show Change Log"):
    st.write("Change Log:")
    st.write(st.session_state.change_log)
