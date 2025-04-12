
# Backward Difference Derivative Calculator

## Overview
This web app implements the **Backward Difference Method** for approximating the derivative of a function at a specific point. It allows users to input mathematical functions, the point at which to evaluate the derivative, and the step size. The calculator computes both the **numerical derivative** using the backward difference formula and the **analytical derivative** (if possible), displaying the results along with the absolute error between the numerical and analytical solutions.

### Formula Used:
The backward difference formula is used to approximate the derivative of a function \( f(x) \) at a point \( x = a \) as:

\[
f'(a) \approx \frac{f(a) - f(a - h)}{h}
\]

Where:
- \( f(a) \) is the value of the function at point \( a \),
- \( f(a - h) \) is the value of the function at \( a - h \), with \( h \) being the step size.

### Method Used:
The **Backward Difference Method** is a simple numerical method to estimate derivatives. It uses the value of the function at two points: at the point of interest \( a \), and at a small step \( h \) behind that point, \( a - h \). This method is particularly useful when the exact derivative is difficult or impossible to compute.

## How the App Works:
1. **Function Input:** The user inputs a mathematical function in Python syntax. The function can include basic arithmetic operations, trigonometric functions (`sin(x)`, `cos(x)`, etc.), exponentials, logarithms, and square roots.

2. **Point and Step Size:** The user provides the point at which the derivative is to be evaluated and the step size.

3. **Numerical Derivative:** The app computes the derivative using the backward difference formula.

4. **Analytical Derivative:** The app uses **SymPy** to compute the exact derivative (if possible) and compares it to the numerical approximation.

5. **Error Calculation:** The absolute error between the numerical and analytical derivatives is calculated and displayed.

6. **Graph Plot:** A graph of the function is plotted alongside the tangent line at \( x = a \) and the secant line connecting \( f(a) \) and \( f(a - h) \).

## Instructions to Run the App

### 1. Prerequisites:
You must have Python 3.x and **Streamlit** installed on your machine.

### 2. Install Dependencies:
In your terminal, run:

```bash
pip install streamlit sympy numpy matplotlib
