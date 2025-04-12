import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def evaluate_function(func_str, x_val):
    allowed_names = math.__dict__.copy()
    allowed_names["x"] = x_val
    try:
        return eval(func_str, {"__builtins__": {}}, allowed_names)
    except Exception:
        return None

def main():
    st.set_page_config(page_title="Backward Difference Derivative Calculator", layout="centered")
    st.title("📐 Backward Difference Derivative Calculator")

    st.markdown("""
        This calculator **approximates the derivative** of a mathematical function at a specific point
        using the **Backward Difference Method**, a basic technique in numerical differentiation.
    """)

    st.latex(r"f'(a) \approx \frac{f(a) - f(a - h)}{h}")

    with st.expander("ℹ️ How to input functions correctly"):
        st.markdown("""
        - Use `**` for exponents. Example: `x**2` means \\(x^2\\)
        - Use `*` for multiplication. Example: `3*x` instead of `3x`
        - You can use math functions:
            - `sin(x)`, `cos(x)`, `tan(x)`
            - `exp(x)` for \\(e^x\\)
            - `log(x)` for \\(\\ln(x)\\)
            - `sqrt(x)` for square root
        - Follow Python math syntax.
        """)

    st.divider()

    with st.form("derivative_form"):
        func_str = st.text_input("🧮 Enter function f(x):", value="x**2 + 3*x")
        a = st.number_input("📍 Enter the point x = a:", value=2.0)
        h = st.number_input("🔁 Enter step size h:", value=0.01, format="%.5f")
        submitted = st.form_submit_button("🚀 Calculate Derivative")

    if submitted:
        f_a = evaluate_function(func_str, a)
        f_a_minus_h = evaluate_function(func_str, a - h)

        if f_a is None or f_a_minus_h is None:
            st.error("❌ There was an error evaluating your function. Make sure it's valid.")
            return

        derivative = (f_a - f_a_minus_h) / h

        st.subheader("📊 Step-by-Step Solution")
        st.markdown("### 1. Formula")
        st.latex(r"f'(a) \approx \frac{f(a) - f(a - h)}{h}")
        st.markdown("### 2. Substituting values")
        st.latex(fr"f'({a}) \approx \frac{{f({a}) - f({a - h})}}{{{h:.3f}}}")
        st.markdown("### 3. Evaluating the function")
        st.write(f"f({a}) = {f_a:.3f}")
        st.write(f"f({a - h}) = {f_a_minus_h:.3f}")
        st.markdown("### 4. Final Calculation")
        st.latex(fr"f'({a}) \approx \frac{{{f_a:.3f} - {f_a_minus_h:.3f}}}{{{h:.3f}}}")
        st.success(f"**Approximated derivative: {derivative:.3f}**")

        # --- Analytical derivative using sympy ---
        try:
            x = sp.Symbol('x')
            # Ensure the expression is properly handled (check for singularities like division by zero)
            symbolic_func = sp.sympify(func_str, locals={"sin": sp.sin, "cos": sp.cos, "log": sp.ln, "exp": sp.exp, "sqrt": sp.sqrt})
            
            # Check if the expression has a singularity at x = 0 (e.g., division by x)
            if any(sp.singularities(symbolic_func, x)):
                st.warning("⚠️ The function has a singularity at x = 0. Analytical derivative might be undefined.")

            symbolic_derivative = sp.diff(symbolic_func, x)
            exact_derivative = float(symbolic_derivative.evalf(subs={x: a}))

            st.markdown("### 5. Analytical Derivative")
            st.latex(fr"f'(x) = {sp.latex(symbolic_derivative)}")
            st.write(f"f'({a}) = {exact_derivative:.3f}")

            # Absolute error
            error = abs(derivative - exact_derivative)
            st.markdown("### 6. Error Analysis")
            st.write(f"Absolute Error = |{derivative:.3f} - {exact_derivative:.3f}| = **{error:.3f}**")

        except Exception as e:
            st.warning(f"Could not compute analytical derivative: {e}")

        # --- Graph Plot ---
        st.markdown("### 7. Graph Plot")

        x_vals = np.linspace(a - 5*h, a + 5*h, 500)
        y_vals = []
        valid_x = []

        for x_point in x_vals:
            y_val = evaluate_function(func_str, x_point)
            if isinstance(y_val, (int, float)):
                valid_x.append(x_point)
                y_vals.append(y_val)

        tangent_y = [f_a + derivative * (x_point - a) for x_point in valid_x]

        fig, ax = plt.subplots()
        ax.plot(valid_x, y_vals, label="f(x)", color="blue")
        ax.plot(valid_x, tangent_y, '--', label="Tangent (Approx.)", color="orange")
        ax.plot([a - h, a], [f_a_minus_h, f_a], 'r--', label="Secant Line", linewidth=2)

        ax.plot(a, f_a, 'ro', label="f(a)")
        ax.plot(a - h, f_a_minus_h, 'go', label="f(a - h)")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Function with Backward Difference Approximation")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    # Creator Credit
    st.markdown(
        "<div style='position: fixed; bottom: 10px; right: 10px; font-size: 0.85em;'>"
        "Made by <strong>David Ysrael Tolentino</strong>"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
