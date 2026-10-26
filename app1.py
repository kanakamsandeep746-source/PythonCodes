import streamlit as st
st.set_page_config(
    page_title="Streamlit Demo App",
    layout="centered"
)
st.title("Streamlit App")
st.subheader("Topic 1")
st.button("button check")

tab1,tab2,tab3=list(st.tabs(['Home','Dashboard','Contact']))

st.divider()
st.subheader('Topic 2')
with tab1:
    st.write("Welcom to Home")
    col1,col2=st.columns(2)
    with col1:
        st.button("left side button",type="primary")
    with col2:
        st.button("right side button")
with tab2:
    st.write("Welcom to Dashboard")
with tab3:
    st.write("Welcom to Contact")


with st.container(height=300,border=200):
    for i in range(50):
        st.write(f"this is {i}")

st.divider()
if st.button("Button2"):
    st.write("i am alive")
a=0
st.subheader("level 2")
name=st.text_input("enter your name")
print(a)
st.write(f" my name is {name}")
