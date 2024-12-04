#adjusted from @wbjmattingly - https://www.youtube.com/watch?v=s86jz9qVeWA&t=158s

#imports
import streamlit as st


Dashboard = st.Page('Dashboard.py', title='Dashboard')
ChangeLog = st.Page('ChangeLog.py', title = 'Change Log')
Placeholder= st.Page('page_2.py', title = 'Placeholder')
Visualization = st.Page('VisTrans.py', title = 'Viz & Transform')

#initialize session states to be used across pages
if 'upload_toggle' not in st.session_state:
    st.session_state.upload_toggle = None
if 'raw_data' not in st.session_state:
    st.session_state.raw_data = None
if 'raw_numeric_attrs' not in st.session_state:
    st.session_state.raw_numeric_attrs = None
if 'raw_object_attrs' not in st.session_state:
    st.session_state.raw_object_attrs = None
if 'class_attr' not in st.session_state:
    st.session_state.class_attr = None
if 'change_log' not in st.session_state:
    st.session_state.change_log = []
if 'available_columns' not in st.session_state:
    st.session_state.available_columns = []
if "data" not in st.session_state:
    st.session_state.data = []
if 'transformed_data' not in st.session_state:
    st.session_state.transformed_data = st.session_state.raw_data
if 'transform_column' not in st.session_state:
    st.session_state.transform_column = None
if 'transform_type' not in st.session_state:
    st.session_state.transform_type = None

pg = st.navigation([Dashboard, Visualization, Placeholder, ChangeLog])

st.set_page_config(page_title='No-code EDA', page_icon=':blue:')
pg.run()