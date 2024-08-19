import streamlit as st
import json
import os
from datetime import datetime
from core.layout_analysis import LayoutAnalysis

# Create the patients folder if it doesn't exist
if not os.path.exists('patients'):
    os.makedirs('patients')

# Path to the JSON file that stores all patients' data
patients_data_file = 'patients/patients_data.json'

# Load existing patients' data if the file exists
if os.path.exists(patients_data_file):
    with open(patients_data_file, 'r') as file:
        patients_data = json.load(file)
else:
    patients_data = []

# Homepage title
st.title("Clinically AI")

# Dropdown for Health Center selection
health_centers = ["Health Center A", "Health Center B", "Health Center C"]
selected_center = st.selectbox("Select Health Center", health_centers)

# Dropdown for Consulting Doctor selection
doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Williams"]
selected_doctor = st.selectbox("Select Consulting Doctor", doctors)

# Input fields for patient details
name = st.text_input("Name")
age = st.number_input("Age", min_value=0)
temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
pulse_rate = st.number_input("Pulse Rate (bpm)", min_value=30, max_value=200)

# Option for visit type
visit_type = st.radio("Visit Type", ["Fresh Visit", "Re-Visit"])

# Input field for report type
report_type = st.text_input("Report Type")

# File uploader for blood reports (optional)
uploaded_file = st.file_uploader("Upload Blood Report (Optional)", type=["pdf", "jpg", "jpeg", "png"])

# Button to save patient data
if st.button("Save Data"):
    if not name or not age or not report_type:
        st.warning("Please fill out all required fields.")
    else:
        # Create a directory for the patient using the name and a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        patient_dir = os.path.join('patients', f"{name}_{timestamp}")
        os.makedirs(patient_dir, exist_ok=True)

        # Initialize report path as None
        report_path = None

        # Save the uploaded report file if it exists
        if uploaded_file:
            report_path = os.path.join(patient_dir, uploaded_file.name)
            normalFilepath = 'patients' + '/' + f"{name}_{timestamp}" + "/" + uploaded_file.name 
            LayoutAnalysis(normalFilepath)
            with open(report_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Prepare the patient data to be added to the JSON file
        patient_data = {
            "health_center": selected_center,
            "consulting_doctor": selected_doctor,
            "name": name,
            "age": age,
            "temperature": temperature,
            "pulse_rate": pulse_rate,
            "visit_type": visit_type,
            "report_type": report_type,
            "report_path": report_path,  # This will be None if no file was uploaded
            "timestamp": timestamp
        }

        # Append the new patient data to the list
        patients_data.append(patient_data)

        # Save all patients' data back to the JSON file
        with open(patients_data_file, "w") as json_file:
            json.dump(patients_data, json_file, indent=4)
            
        st.write(report_path)
        

        st.success(f"Patient data saved successfully! Report stored in {patient_dir}" if uploaded_file else f"Patient data saved successfully!")
