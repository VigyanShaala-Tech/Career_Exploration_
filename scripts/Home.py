import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# URL pointing to the Excel file
file_url = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/STEM%20Colleges%20in%20India%20Dataset.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svU1RFTSBDb2xsZWdlcyBpbiBJbmRpYSBEYXRhc2V0Lnhsc3giLCJpYXQiOjE3MzMzNzU0NTYsImV4cCI6MTczNTk2NzQ1Nn0.wsf_IVhS7PpfvkLg15RvmYKo8P3sPKZPx56UWB0Fm-E&t=2024-12-05T05%3A10%3A55.478Z'

# Make a GET request to the URL to retrieve the CSV file
try:
    response = requests.get(file_url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Read the content of the response as a pandas DataFrame
    df = pd.read_excel(BytesIO(response.content))  # Use pd.read_excel for Excel files
except requests.exceptions.RequestException as e:
    st.error(f"An error occurred while accessing the dataset: {e}")
except Exception as e:
    st.error(f"An error occurred while reading the dataset: {e}")

# Define the Streamlit interface
def main():
    st.title('Student Progress Report')

    # Initialize 'student_name' in session state if it's not already done
    if 'student_name' not in st.session_state:
        st.session_state['student_name'] = ''

    # Get user input for student name and update session state
    st.session_state.student_name = st.text_input('**Enter your name**', value=st.session_state.student_name)

    # Check if 'student_name' is empty and display a warning
    if not st.session_state.student_name:
        st.warning('*Please enter a valid name.*')

    # Degree options based on available data
    st.session_state.qualified_degrees = df['Degree'].unique()
    st.session_state.selected_degree = st.selectbox('**Select the Degree you want to pursue next (Your Aspiration Degree)**', st.session_state.qualified_degrees)

    # Filter the fields based on the selected degree
    st.session_state.filtered_fields = sorted([i for i in df[df['Degree'] == st.session_state.selected_degree]['Field'].unique() if isinstance(i, str)])
    st.session_state.selected_field = st.selectbox('**Select Area of Interest**', st.session_state.filtered_fields)

    # Filter subfields based on selected degree and field
    st.session_state.filtered_subfields = sorted([i for i in df[(df['Degree'] == st.session_state.selected_degree) & (df['Field'] == st.session_state.selected_field)]['SubField'].unique() if isinstance(i, str)])
    st.session_state.selected_subfield = st.selectbox('**Select Specialization between this Field**', st.session_state.filtered_subfields)

    # Filter colleges based on selected degree, field, and subfield
    st.session_state.filtered_colleges = sorted([i for i in df[(df['Degree'] == st.session_state.selected_degree) & (df['Field'] == st.session_state.selected_field) & (df['SubField'] == st.session_state.selected_subfield)]['College_Name'].unique() if isinstance(i, str)])
    st.session_state.selected_college = st.selectbox('**Select college**', st.session_state.filtered_colleges)

    # Show college details when a selection is made
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
        st.warning(f"*A complete list of all relevant scholarships will be provided when you download the report (PDF) on the next page.*")

    # Display the "Explore Career" button and handle the page transition
    if st.button('Explore Career'):
        st.session_state.next_page = True
        st.experimental_rerun()

# Check if the next page should be displayed
if 'next_page' in st.session_state and st.session_state.next_page:
    # Assuming Job is another Streamlit app or function to be run next
    import Job
    Job.main()
else:
    # Display the main page if not transitioning to the next page
    main()
