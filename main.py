import streamlit as st

st.title("Tính tônổng, hiệu, tích và thương của 2 số")

st.header("Nhập 2 số")
num1 = st.number_input("Số thứ nhất", value=0.0, format="%f")
num2 = st.number_input("Số thứ hai", value=0.0, format="%f")

tong = num1 + num2
hieu = num1 - num2
tich = num1 * num2

if num2 != 0:
    thuong = num1 / num2
else:
    thuong = "Không xác định được"

st.header("Kết quả")
st.write(f"Tổng: {tong}")
st.write(f"Hiệu: {hieu}")
st.write(f"Tích: {tich}")
st.write(f"Thương: {thuong}")
