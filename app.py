import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas

st.title("Body na kružnici")

x_center = st.number_input("Souřadnice středu X:", value=0.0)
y_center = st.number_input("Souřadnice středu Y:", value=0.0)
radius = st.number_input("Poloměr kružnice [m]:", value=5.0, min_value=0.1)
num_points = st.number_input("Počet bodů:", value=8, min_value=1, step=1)
color = st.color_picker("Barva bodů:", "#ff0000")

angles = np.linspace(0, 2*np.pi, int(num_points), endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

fig, ax = plt.subplots()
circle = plt.Circle((x_center, y_center), radius, fill=False, linestyle="--")
ax.add_artist(circle)
ax.scatter(x_points, y_points, c=color)
ax.set_aspect("equal", "box")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.grid(True)

st.pyplot(fig)

st.sidebar.title("O aplikaci")
st.sidebar.write("""
**Autor:** Ondřej Karásek 
**Kontakt:** 277960@vutbr.cz  

Použité technologie:  
- Python  
- Streamlit  
- Matplotlib  
- Reportlab
""")

if st.button("Stáhnout PDF"):
    filename = "vystup.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "Body na kružnici")
    c.drawString(100, 780, f"Střed: ({x_center}, {y_center})")
    c.drawString(100, 760, f"Poloměr: {radius} m")
    c.drawString(100, 740, f"Počet bodů: {num_points}")
    c.drawString(100, 720, f"Barva bodů: {color}")
    c.drawString(100, 700, "Autor: Ondřej Karásek, 277960@vutbr.cz")
    c.save()
    with open(filename, "rb") as f:
        st.download_button("Stáhnout výsledné PDF", f, file_name=filename)
        
