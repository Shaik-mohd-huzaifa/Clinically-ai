import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv() 


# API key and model for Layout Analysis
api_key = os.getenv("UPSTAGE_API_KEY")
model = "receipt-extraction"

# Layout Analysis Function
def LayoutAnalysis(folderpath, filename):
    url = "https://api.upstage.ai/v1/document-ai/layout-analysis"
    # Construct the full path to the file
    file_path = os.path.join(folderpath, filename)
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        # Open the file and send the request
        with open(file_path, "rb") as file:
            files = {"document": file}
            data = {"ocr": True}
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()  # Check for request errors
            response_data = response.json()

            elements = response_data.get("elements", [])

            # Extract and concatenate text from elements
            text = ''
            for element in elements:
                text += '\n' + element.get("text", "")

            # Save the output text
            output_file = "output.txt"
            with open(output_file, "w") as file:
                file.write(text)
                
            return text, output_file

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Directory containing folders
base_directory = 'patients'

# Function to get folders containing at least one file
def get_folders_with_files(base_dir):
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    non_empty_folders = []
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if any(os.path.isfile(os.path.join(folder_path, f)) for f in os.listdir(folder_path)):
            non_empty_folders.append(folder_path)
    return non_empty_folders

# Get a list of folders that contain files
folders = get_folders_with_files(base_directory)

# Page title
st.title("Folder and File Selector")

# Dropdown for selecting a folder
selected_folder = st.selectbox("Select Folder", folders)

if selected_folder:
    # Get a list of files in the selected folder
    files = [f for f in os.listdir(selected_folder) if os.path.isfile(os.path.join(selected_folder, f))]
    
    if files:
        # Dropdown for selecting a file
        selected_file = st.selectbox("Select File", files)
        
        # Button to process the selected file
        if st.button("Process File"):
            if selected_file:
                result_text, output_file_path = LayoutAnalysis(selected_folder, selected_file)
                if result_text:
                    st.write("Processed Text:")
                    st.write(result_text)
                    st.success(f"Processing complete! Output saved to {output_file_path}")
            else:
                st.warning("Please select a file.")
    else:
        st.warning("The selected folder is empty.")
else:
    st.warning("No folders available with files.")
