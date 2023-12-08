import streamlit as st
import streamlit.components.v1 as components

tab1, tab2, tab3 = st.tabs(["Option 1", "Option 2", "Option 3"])

with tab1:
   st.header("A cat")
   # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   st.components.v1.html("""<iframe src="https://30days.streamlit.app/?embed=true" height="800" style="width:100%;border:none;"></iframe>""", width=None, height=None, scrolling=False)

with tab2:
   st.header("A dog")
   # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   st.components.v1.html("""<iframe src="https://doc-column-config-overview.streamlit.app/?embed=true" height="800" style="width:100%;border:none;"></iframe>""", width=None, height=None, scrolling=False)


with tab3:
   st.header("An owl")
   # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
