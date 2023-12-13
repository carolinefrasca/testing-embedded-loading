import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

tab1, tab2, tab3 = st.tabs(["Option 1", "Option 2", "Option 3"])
code = """
import streamlit as st

st.text('This is some text.')
"""

with tab1:
   # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   show_code = st.checkbox("Show code")
   if show_code:
      col1, col2 = st.columns(2)
   
      with col1:
         st.components.v1.html("""<iframe src="https://echarts.streamlit.app/?embed=true" height=700 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)
      with col2:
         st.code(code)
   else:
      st.components.v1.html("""<iframe src="https://echarts.streamlit.app/?embed=true" height=1200 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)
with tab2:
   col1, col2 = st.columns(2)

   st.header("A dog")
   # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   with col1:
      st.components.v1.html("""<iframe src="https://cross-chain-monitoring.streamlit.app/?embed=true" height=1200 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)
   with col2:
      st.code(code)

with tab3:
   col1, col2 = st.columns(2)

   st.header("An owl")
   with col1:
      st.components.v1.html("""<iframe src="https://gptlab.streamlit.app/?embed=true" height=1200 style="width:100%;border:none;"></iframe>""", width=None, height=1200, scrolling=False)
   with col2:
      st.code(code)
   # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
