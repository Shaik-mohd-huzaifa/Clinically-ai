# Clinically AI - Health Management System

## Overview

Clinically AI is a health management system designed to streamline patient data collection and analysis. The system uses Streamlit for a user-friendly interface, Python for backend logic, Upstage for document processing, and LangChain for advanced text processing and retrieval. This project helps healthcare professionals manage patient information efficiently and provides valuable insights through document analysis.

## Features

- **Patient Data Collection**: Collect patient details including health center, consulting doctor, name, age, temperature, pulse rate, and visit type.
- **Report Management**: Upload and store blood reports with options for fresh or re-visit.
- **Document Processing**: Process and analyze uploaded reports using Upstage's layout analysis.
- **Advanced Text Processing**: Utilize LangChain for text extraction and summarization from documents.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- Upstage API Key
- LangChain

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/clinically-ai.git
   cd clinically-ai
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```plaintext
   UPSTAGE_API_KEY=your_upstage_api_key
   ```

   Replace `your_upstage_api_key` with your actual Upstage API key.

### Running the Application

1. **Start the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Navigate to the application in your browser:**

   Open `http://localhost:8501` in your web browser.

## File Structure

- `app.py`: The main Streamlit application file.
- `core/layout_analysis.py`: Contains the `LayoutAnalysis` function for document processing.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables for API keys and other sensitive information.
- `patients/`: Directory where patient data and reports are stored.
- `output.txt`: File where processed text from reports is saved.

## Usage

### Homepage

- **Select Health Center**: Choose the health center from the dropdown.
- **Select Consulting Doctor**: Choose the doctor from the dropdown.
- **Enter Patient Details**: Provide name, age, temperature, pulse rate, and visit type.
- **Upload Report**: Optionally upload a blood report.
- **Save Data**: Save the patient data along with the report (if uploaded).

### Doctor's Page

- **Select Patient**: Choose a patient from the list.
- **View Patient Details**: Display patient details and the uploaded report.
- **Process Report**: The selected report is processed using the `LayoutAnalysis` function.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

---

Feel free to adjust the sections and details as necessary for your project!
