import numpy as np
import pandas as pd
import streamlit as st

def main():
  st.title("Multiplication")
  html_temp = """
  <multiply style="background-color:blue;padding:10px">
  <h2 style="color:white;text-align:center;">Multiplication of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  number1 = st.number_input("Number 1")
  number2 = st.number_input("Number 2")
  result = number1 * number2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Rushikessh D")

if __name__=='__main__':
  main()
