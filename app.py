import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- UI Header & Student Information ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.divider()
st.markdown(f"### Developed By: **Jawad Ahmed**")
st.markdown(f"### Roll Number: **25-ME-67**")
st.divider()

# --- Sidebar Navigation ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a Tool", ["Unit Converter", "Density Checker"])

# --- Logic: Unit Converter ---
if page == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    
    category = st.selectbox("Select Dimension", ["Length", "Pressure", "Temperature"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        units = {"Meters": 1, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084}
        with col1:
            val = st.number_input("Value", value=1.0)
            from_u = st.selectbox("From", list(units.keys()))
        with col2:
            to_u = st.selectbox("To", list(units.keys()))
            result = val * (units[to_u] / units[from_u])
            st.metric("Converted Value", f"{result:.4f}")

    elif category == "Pressure":
        units = {"Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038, "Atm": 9.8692e-6}
        with col1:
            val = st.number_input("Value", value=1.0)
            from_u = st.selectbox("From", list(units.keys()))
        with col2:
            to_u = st.selectbox("To", list(units.keys()))
            result = val * (units[to_u] / units[from_u])
            st.metric("Converted Value", f"{result:.4f}")

    elif category == "Temperature":
        with col1:
            val = st.number_input("Value", value=0.0)
            temp_op = st.selectbox("Convert", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        with col2:
            if temp_op == "Celsius to Fahrenheit":
                res = (val * 9/5) + 32
                st.metric("Fahrenheit", f"{res:.2f} °F")
            else:
                res = (val - 32) * 5/9
                st.metric("Celsius", f"{res:.2f} °C")

# --- Logic: Density Checker ---
else:
    st.header("⚖️ Material Density Checker")
    
    # Standard densities in kg/m^3
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Water": 1000
    }
    
    selected_material = st.selectbox("Select Material", list(materials.keys()))
    density = materials[selected_material]
    
    st.info(f"The density of **{selected_material}** is **{density} kg/m³**.")
    
    st.subheader("Mass Calculation")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0)
    mass = density * volume
    st.success(f"Total Mass: **{mass:,.2f} kg**")
