import streamlit as st
import json
import os

# Path to the JSON file that stores all patients' data
patients_data_file = "D:/Users/SHAIK MOHD HUZAIFA/Documents/Upstage Hackathon/Server/patients/patients_data.json"

# Load existing patients' data
if os.path.exists(patients_data_file):
    with open(patients_data_file, 'r') as file:
        patients_data = json.load(file)
else:
    patients_data = []

# Title for the Doctor's Page
st.title("Doctor's Page - Patient Records")

# Check if there are any patients
if not patients_data:
    st.warning("No patient data available.")
else:
    # Dropdown to select a patient
    patient_names = [f"{patient['name']} ({patient['timestamp']})" for patient in patients_data]
    selected_patient_name = st.selectbox("Select Patient", patient_names)

    # Find the selected patient's data
    selected_patient = next((patient for patient in patients_data if f"{patient['name']} ({patient['timestamp']})" == selected_patient_name), None)

    if selected_patient:
        # Display the selected patient's data
        st.subheader("Patient Details")
        st.write(f"**Health Center:** {selected_patient['health_center']}")
        st.write(f"**Consulting Doctor:** {selected_patient['consulting_doctor']}")
        st.write(f"**Name:** {selected_patient['name']}")
        st.write(f"**Age:** {selected_patient['age']}")
        st.write(f"**Temperature:** {selected_patient['temperature']} °C")
        st.write(f"**Pulse Rate:** {selected_patient['pulse_rate']} bpm")
        st.write(f"**Visit Type:** {selected_patient['visit_type']}")
        st.write(f"**Report Type:** {selected_patient['report_type']}")
        
        # Display the report path if it exists
        if selected_patient['report_path']:
            st.write(f"**Report Path:** {selected_patient['report_path']}")
        else:
            st.write("**Report Path:** No report uploaded")

        # Provide a link to download the report if it exists
        if selected_patient['report_path'] and os.path.exists(selected_patient['report_path']):
            with open(selected_patient['report_path'], "rb") as report_file:
                st.download_button(
                    label="Download Report",
                    data=report_file,
                    file_name=os.path.basename(selected_patient['report_path']),
                    mime="application/octet-stream"
                )
    else:
        st.error("Patient not found.")
