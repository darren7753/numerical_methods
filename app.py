# libraries
import streamlit as st
import numpy as np
import pandas as pd
import math
from sympy import simplify, symbols, diff, solve

# Settings
st.set_page_config(
    page_title="Numerical Methods",
    layout="wide"
)

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

hide_decoration_bar_style = """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Side bar
with st.sidebar:
    st.header("Numerical Methods")

    num_method = st.radio(
        "Choose one of the following numerical methods",
        ["Bisection", "False Position", "Newton-Raphson", "Secant"]
    )

    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    st.markdown(lnk + """
        <br>
        <p>Made by <b>Mathew Darren Kusuma</b></p>
        <a href='https://github.com/darren7753'><i class='fab fa-github' style='font-size: 30px; color: #FAFAFA;'></i></a>&nbsp;
        <a href='https://www.linkedin.com/in/mathewdarren/'><i class='fab fa-linkedin' style='font-size: 30px; color: #FAFAFA;'></i></a>&nbsp;
        <a href='https://www.instagram.com/darren_matthew_/'><i class='fab fa-instagram' style='font-size: 30px; color: #FAFAFA;'></i></a>
    """, unsafe_allow_html=True)

# Bisection
if num_method == "Bisection":
    st.markdown("<h1 style='text-align: center;'>Bisection</h1>", unsafe_allow_html=True)

    st.info("A root is considered found when the absolute value of $f(c)$, where $c$ is the midpoint of the interval, is smaller than a predefined tolerance value and this occurs before the maximum number of iterations is reached", icon="ℹ️")

    equation = st.text_input("Input the equation")
    if equation:
        function = simplify(equation)
        st.write(function)

        character = [char for char in equation if char.isalpha()]
        if len(character) > 0:
            symbol = symbols(character[0])

    with st.form(key="my_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.number_input("Input the first interval")
        with col2:
            b = st.number_input("Input the second interval")
        with col3:
            e = st.number_input("Input the tolerance", format="%.6f", value=0.000001)
        with col4:
            N = st.number_input("Input the maximum number of iterations", value=100)

        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        fa = function.subs(symbol, a)
        fb = function.subs(symbol, b)

        if fa * fb < 0:
            n = 1
            list_a, list_b, list_c, list_fa, list_fb, list_fc, list_abs_fc = ([] for _ in range(7))
            while True:
                c = (a + b) / 2
                fc = function.subs(symbol, c)

                lists = [list_a, list_b, list_c, list_fa, list_fb, list_fc, list_abs_fc]
                variables = [a, b, c, fa, fb, fc, math.fabs(fc)]
                variables = [float(i) for i in variables]
                
                for i, j in zip(lists, variables):
                    i.append(j)

                if math.fabs(fc) <= e:
                    result = "success"
                    break

                if n > N:
                    result = "failed"
                    break

                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
                n += 1

            df = pd.DataFrame({
                "a": list_a,
                "b": list_b,
                "c": list_c,
                "f(a)": list_fa,
                "f(b)": list_fb,
                "f(c)": list_fc,
                "| f(c) |": list_abs_fc
            })
            df.index += 1
            st.dataframe(df.head(N).style.format({"E": "{:.6f}"}), use_container_width=True)

            if result == "success":
                st.success(f"This equation has an approximate root of {np.round(float(c), 6)}")
            else:
                st.error("The maximum number of iterations has been exceeded")
        else:
            st.error("This equation doesn't have any solutions")

# False Position
if num_method == "False Position":
    st.markdown("<h1 style='text-align: center;'>False Position</h1>", unsafe_allow_html=True)

    st.info("A root is considered found when the absolute value of $f(c)$, where $c$ is the midpoint of the interval, is smaller than a predefined tolerance value and this occurs before the maximum number of iterations is reached", icon="ℹ️")

    equation = st.text_input("Input the equation")
    if equation:
        function = simplify(equation)
        st.write(function)

        character = [char for char in equation if char.isalpha()]
        if len(character) > 0:
            symbol = symbols(character[0])

    with st.form(key="my_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.number_input("Input the first interval")
        with col2:
            b = st.number_input("Input the second interval")
        with col3:
            e = st.number_input("Input the tolerance", format="%.6f", value=0.000001)
        with col4:
            N = st.number_input("Input the maximum number of iterations", value=100)

        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        fa = function.subs(symbol, a)
        fb = function.subs(symbol, b)

        if fa * fb < 0:
            n = 1
            list_a, list_b, list_c, list_fa, list_fb, list_fc, list_abs_fc = ([] for _ in range(7))
            while True:
                c = b - ((fb * (b - a)) / (fb - fa))
                fc = function.subs(symbol, c)

                lists = [list_a, list_b, list_c, list_fa, list_fb, list_fc, list_abs_fc]
                variables = [a, b, c, fa, fb, fc, math.fabs(fc)]
                variables = [float(i) for i in variables]
                
                for i, j in zip(lists, variables):
                    i.append(j)

                if math.fabs(fc) <= e:
                    result = "success"
                    break

                if n > N:
                    result = "failed"
                    break

                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
                n += 1

            df = pd.DataFrame({
                "a": list_a,
                "b": list_b,
                "c": list_c,
                "f(a)": list_fa,
                "f(b)": list_fb,
                "f(c)": list_fc,
                "| f(c) |": list_abs_fc
            })
            df.index += 1
            st.dataframe(df.head(N).style.format({"E": "{:.6f}"}), use_container_width=True)

            if result == "success":
                st.success(f"This equation has an approximate root of {np.round(float(c), 6)}")
            else:
                st.error("The maximum number of iterations has been exceeded")
        else:
            st.error("This equation doesn't have any solutions")

# Newton-Raphson
if num_method == "Newton-Raphson":
    st.markdown("<h1 style='text-align: center;'>Newton-Raphson</h1>", unsafe_allow_html=True)

    st.info("A root is considered found when the absolute value of the difference between $x_{n}$ and $x_{n-1}$ is smaller than a predefined tolerance value and this occurs before the maximum number of iterations is reached", icon="ℹ️")

    equation = st.text_input("Input the equation")
    if equation:
        col1, col2 = st.columns(2)
        with col1:
            st.write("Initial Equation")
            function = simplify(equation)
            st.write(function)

        character = [char for char in equation if char.isalpha()]
        if len(character) > 0:
            symbol = symbols(character[0])

        with col2:
            st.write("Derived Equation")
            derived_function = diff(function, symbol)
            st.write(derived_function)

    with st.form(key="my_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            x0 = st.number_input("Input the initial guess")
        with col2:
            e = st.number_input("Input the tolerance", format="%.6f", value=0.000001)
        with col3:
            N = st.number_input("Input the maximum number of iterations", value=100)

        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        n = 0
        list_xn, list_fxn, list_f_der_xn, list_diff = ([] for _ in range(4))
        while True:
            f = function.subs(symbol, x0)
            f_derivative = derived_function.subs(symbol, x0)
            if f_derivative == 0:
                result = "zero"
                break

            if n == 0:
                lists = [list_xn, list_fxn, list_f_der_xn, list_diff]
                variables = [x0, f, f_derivative, np.nan]
                variables = [float(i) for i in variables]

                for i, j in zip(lists, variables):
                    i.append(j)

            x1 = x0 - (f / f_derivative)
            fx1 = function.subs(symbol, x1)
            f_derivative_x1 = derived_function.subs(symbol, x1)
            diff = math.fabs(x1 - x0)

            lists = [list_xn, list_fxn, list_f_der_xn, list_diff]
            variables = [x1, fx1, f_derivative_x1, diff]
            variables = [float(i) for i in variables]
            
            for i, j in zip(lists, variables):
                i.append(j)
            
            x0 = x1
            n += 1

            if diff <= e:
                result = "success"
                break

            if n > N:
                result = "failed"
                break

        if result != "zero":
            df = pd.DataFrame({
                "xn": list_xn,
                "f(xn)": list_fxn,
                "f'(xn)": list_f_der_xn,
                "| xn - xn-1 |": list_diff
            })
            st.dataframe(df.head(N).style.format({"E": "{:.6f}"}), use_container_width=True)

        if result == "success":
            st.success(f"This equation has an approximate root of {np.round(float(x1), 6)}")
        elif result ==  "failed":
            st.error("The maximum number of iterations has been exceeded")
        else:
            st.error("Division by zero is not allowed")

# Secant
if num_method == "Secant":
    st.markdown("<h1 style='text-align: center;'>Secant</h1>", unsafe_allow_html=True)

    st.info("A root is considered found when the absolute value of the difference between $x_{n}$ and $x_{n-1}$ is smaller than a predefined tolerance value and this occurs before the maximum number of iterations is reached", icon="ℹ️")

    equation = st.text_input("Input the equation")
    if equation:
        function = simplify(equation)
        st.write(function)

        character = [char for char in equation if char.isalpha()]
        if len(character) > 0:
            symbol = symbols(character[0])

    with st.form(key="my_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            x0 = st.number_input("Input the first guess")
        with col2:
            x1 = st.number_input("Input the second guess")
        with col3:
            e = st.number_input("Input the tolerance", format="%.6f", value=0.000001)
        with col4:
            N = st.number_input("Input the maximum number of iterations", value=100)

        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        n = 0
        list_x, list_fx, list_diff = ([] for _ in range(3))
        while True:
            fx0 = function.subs(symbol, x0)
            fx1 = function.subs(symbol, x1)
            x = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
            fx = function.subs(symbol, x)

            if math.fabs(fx1 - fx0) == 0:
                result = "zero"
                break

            if n == 0:
                lists = [list_x, list_fx, list_diff]
                variables = [x0, fx0, np.nan]
                variables = [float(i) for i in variables]

                for i, j in zip(lists, variables):
                    i.append(j)

            diff = math.fabs(x - x0)

            lists = [list_x, list_fx, list_diff]
            variables = [x, fx, diff]
            variables = [float(i) for i in variables]
            
            for i, j in zip(lists, variables):
                i.append(j)
            
            x0 = x1
            x1 = x
            n += 1

            if diff <= e:
                result = "success"
                break

            if n > N:
                result = "failed"
                break

        if result != "zero":
            df = pd.DataFrame({
                "xn": list_x,
                "f(xn)": list_fx,
                "| xn - xn-1 |": list_diff
            })
            st.dataframe(df.head(N).style.format({"E": "{:.6f}"}), use_container_width=True)

        if result == "success":
            st.success(f"This equation has an approximate root of {np.round(float(x1), 6)}")
        elif result ==  "failed":
            st.error("The maximum number of iterations has been exceeded")
        else:
            st.error("Division by zero is not allowed")