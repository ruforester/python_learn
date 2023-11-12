import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('portfolio/images/1.png')

with col2:
    st.title("Lorem, ipsum.")
    content = """Lorem ipsum dolor sit amet consectetur adipisicing elit.
      Asperiores dolore iusto odio odit modi quas maiores aliquid sit tempora saepe?
      rspiciatis, distinctio soluta. Veniam voluptates totam hic perspiciatis recusandae. Nesciunt?"""
    st.info(content)

content2 = """
Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ipsa, maiores?
"""
st.write(content2)

df = pd.read_csv('portfolio/data.csv', sep=';')
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('portfolio/images/' + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('portfolio/images/' + row['image'])
        st.write(f"[Source code]({row['url']})")