
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Palancas Biomecánicas", layout="centered")

st.title("⚙️ Simulador de Palancas en el Cuerpo Humano")
st.write("Explora cómo cambian las fuerzas musculares y el torque en diferentes palancas del cuerpo.")

# Entradas del usuario
st.sidebar.header("Parámetros de la palanca")
r_m = st.sidebar.slider("Brazo del músculo r_m (cm)", 1, 10, 4) / 100  # convertir a metros
r_L = st.sidebar.slider("Brazo de la carga r_L (cm)", 5, 50, 30) / 100
F_L = st.sidebar.slider("Carga (N)", 5, 200, 50)
theta_min = st.sidebar.slider("Ángulo mínimo (°)", 0, 90, 0)
theta_max = st.sidebar.slider("Ángulo máximo (°)", 0, 120, 90)
steps = st.sidebar.slider("Número de pasos", 10, 200, 100)

# Cálculos
theta = np.linspace(np.radians(theta_min), np.radians(theta_max), steps)
r_m_eff = r_m * np.sin(theta)  # brazo de palanca efectivo del músculo
r_L_eff = r_L * np.sin(theta)  # brazo de palanca efectivo de la carga

F_m = (F_L * r_L_eff) / (r_m_eff + 1e-6)  # evitar división por cero
torque = F_m * r_m_eff
VM = r_m_eff / r_L_eff

# Resultados estáticos
st.subheader("📊 Resultados principales")
col1, col2, col3 = st.columns(3)
col1.metric("Fuerza muscular (N)", f"{np.mean(F_m):.1f}")
col2.metric("Torque promedio (N·m)", f"{np.mean(torque):.2f}")
col3.metric("Ventaja mecánica promedio", f"{np.mean(VM):.2f}")

# Gráficas
st.subheader("🔍 Gráficas")
fig, ax = plt.subplots()
ax.plot(np.degrees(theta), F_m, label="Fuerza muscular (N)")
ax.plot(np.degrees(theta), torque, label="Torque (N·m)")
ax.set_xlabel("Ángulo (°)")
ax.set_ylabel("Valor")
ax.set_title("Fuerza y Torque según el ángulo")
ax.legend()
st.pyplot(fig)

fig2, ax2 = plt.subplots()
ax2.plot(np.degrees(theta), VM, color="purple", label="Ventaja mecánica")
ax2.set_xlabel("Ángulo (°)")
ax2.set_ylabel("VM")
ax2.set_title("Ventaja mecánica vs. ángulo")
ax2.legend()
st.pyplot(fig2)

# Conclusión rápida
st.info("👉 Observa cómo pequeños cambios en el brazo del músculo modifican drásticamente la fuerza requerida.")
