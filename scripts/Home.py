import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# URL pointing to the Excel file
file_url = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/STEM%20Colleges%20in%20India%20Dataset.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svU1RFTSBDb2xsZWdlcyBpbiBJbmRpYSBEYXRhc2V0Lnhsc3giLCJpYXQiOjE3MzMzNzU0NTYsImV4cCI6MTczNTk2NzQ1Nn0.wsf_IVhS7PpfvkLg15RvmYKo8P3sPKZPx56UWB0Fm-E&t=2024-12-05T05%3A10%3A55.478Z'

# Function to fetch CSV from Supabase storage
def fetch_csv_from_supabase():
    try:
        # Get the file from Supabase (replace 'your-bucket-name' and 'your-file-name.csv')
        file_url = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/STEM%20Colleges%20in%20India%20Dataset.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svU1RFTSBDb2xsZWdlcyBpbiBJbmRpYSBEYXRhc2V0Lnhsc3giLCJpYXQiOjE3MzMzNzU0NTYsImV4cCI6MTczNTk2NzQ1Nn0.wsf_IVhS7PpfvkLg15RvmYKo8P3sPKZPx56UWB0Fm-E&t=2024-12-05T05%3A10%3A55.478Z'

        if file_url:
            # If the file is successfully fetched, read it into a DataFrame
            df = pd.read_csv(BytesIO(file_url))
            return df
        else:
            raise Exception("File not found or failed to download.")
    except Exception as e:
        st.error(f"Error fetching the CSV file: {e}")
        return None

# Fetch the CSV file
df = fetch_csv_from_supabase()

# Define the Streamlit interface
def main():
    st.title('Student Progress Report')

    # Initialize 'student_name' in session state if it's not already done
    if 'student_name' not in st.session_state:
        st.session_state['student_name'] = ''

    # Use user input to update the 'student_name' in session state
    st.session_state.student_name = st.text_input('**Enter your name**', value=st.session_state.student_name)

    # Check if 'student_name' is empty and display a warning
    if st.session_state.student_name == '':
        st.warning('*Please enter a valid name.*')

    if df is not None:
        # Load qualified degrees from the DataFrame
        st.session_state.qualified_degrees = df['Degree'].unique() 
        st.session_state.selected_degree = st.selectbox('**Select the Degree you want to pursue next (Your Aspiration Degree)**', st.session_state.qualified_degrees)

        # Filter Fields based on selected Degree
        st.session_state.filtered_fields = sorted([i for i in df[df['Degree'] == st.session_state.selected_degree]['Field'].unique() if isinstance(i, str)])
        st.session_state.selected_field = st.selectbox('**Select Area of Interest**', st.session_state.filtered_fields)

        # Filter Subfields based on selected Field
        st.session_state.filtered_subfields = sorted([i for i in df[(df['Degree'] == st.session_state.selected_degree) & (df['Field'] == st.session_state.selected_field)]['SubField'].unique() if isinstance(i, str)])
        st.session_state.selected_subfield = st.selectbox('**Select Specialization between this Field**', st.session_state.filtered_subfields)

        # Filter Colleges based on selected Subfield
        st.session_state.filtered_colleges = sorted([i for i in df[(df['Degree'] == st.session_state.selected_degree) & (df['Field'] == st.session_state.selected_field) & (df['SubField'] == st.session_state.selected_subfield)]['College_Name'].unique() if isinstance(i, str)])
        st.session_state.selected_college = st.selectbox('**Select college**', st.session_state.filtered_colleges)

        if st.session_state.selected_college:
            st.session_state.college_details = df[(df['Degree'] == st.session_state.selected_degree) &
                                (df['Field'] == st.session_state.selected_field) &
                                (df['SubField'] == st.session_state.selected_subfield) &
                                (df['College_Name'] == st.session_state.selected_college)]

            st.header('**College Details**')
            st.markdown(f"**College:** {st.session_state.selected_college}")
            st.markdown(f"**Duration:** {st.session_state.college_details['Duration'].values[0]}")
            st.markdown(f"**College Fee:** {st.session_state.college_details['Fees'].values[0]}")
            st.markdown(f"**Minimum Eligibility:** {st.session_state.college_details['Eligiblity Criteria'].values[0]}")
            st.markdown(f"**Selection Criteria:** {st.session_state.college_details['Selection Process'].values[0]}")
            st.markdown(f"**Exam to Qualify:** {st.session_state.college_details['Exam'].values[0]}")
            st.markdown(f"**Available Seats:** {st.session_state.college_details['Seats'].values[0]}")
            st.markdown(f"**Mode of exam:** {st.session_state.college_details['Mode'].values[0]}")
            st.warning(f"*A complete list of all relevant scholarships will be provided when you download the report (pdf) on the next page.*")

    # Button to trigger the next page
    if st.button('Explore Career'):
        # Set a session state variable to indicate that the next page should be displayed
        st.session_state.next_page = True
        # Rerun the script
        st.experimental_rerun()

# Check if the next page should be displayed
if 'next_page' in st.session_state and st.session_state.next_page:
    # Display the Job12.py page
    import Job  # Assuming Job12.py is a separate file, adjust this import as necessary
    Job.main()
else:
    # Display the Home.py page
    main()
