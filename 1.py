import streamlit as st

st.title("小型计算应用")
name = st.text_input("输入你的名字：")
num = st.number_input("输入一个数字：", value=0)

if st.button("计算平方"):
    st.write(f"{name}，你的数字平方是：{num ** 2}")

