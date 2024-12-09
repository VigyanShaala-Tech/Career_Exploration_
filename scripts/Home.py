import pandas as pd
import streamlit as st
import boto3
import io
from streamlit_option_menu import option_menu
import Job  # Import the Job12 module
from PIL import Image
import base64
from io import BytesIO
import requests


# Define Supabase storage file URL
supabase_file_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/College_S3.csv?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vQ29sbGVnZV9TMy5jc3YiLCJpYXQiOjE3MzM1MTMwODUsImV4cCI6MTczNDExNzg4NX0.M3-pafyxmPzSVzl_p8cIB94-WcSHFQwD607p1q1hxF4&t=2024-12-06T19%3A24%3A45.500Z"

# Function to fetch data from the Supabase URL
@st.cache_data
def fetch_college_data():
    try:
        response = requests.get(supabase_file_url)
        response.raise_for_status()  # Raise an error for bad status codes
        # Read the content as a pandas DataFrame
        return pd.read_csv(BytesIO(response.content), encoding='latin1')
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while accessing the data: {e}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occurred while reading the data: {e}")
        return pd.DataFrame()

# Main Streamlit app
def main():
    st.title('Student Progress Report')

    # Fetch data from Supabase
    df = fetch_college_data()
    if df.empty:
        st.error("Failed to load data. Please try again later.")
        return

    # Initialize 'student_name' in session state if it's not already done
    if 'student_name' not in st.session_state:
        st.session_state['student_name'] = ''

    # User input for 'student_name'
    st.session_state.student_name = st.text_input('**Enter your name**', value=st.session_state.student_name)

    # Check if 'student_name' is empty and display a warning
    if not st.session_state.student_name.strip():
        st.warning('*Please enter a valid name.*')

    # Degree selection
    st.session_state.qualified_degrees = sorted(df['Degree'].dropna().unique())
    st.session_state.selected_degree = st.selectbox(
        '**Select the Degree you want to pursue next (Your Aspiration Degree)**',
        st.session_state.qualified_degrees
    )

    # Field selection
    st.session_state.filtered_fields = sorted(
        df[df['Degree'] == st.session_state.selected_degree]['Field'].dropna().unique()
    )
    st.session_state.selected_field = st.selectbox('**Select Area of Interest**', st.session_state.filtered_fields)

    # Subfield selection
    st.session_state.filtered_subfields = sorted(
        df[(df['Degree'] == st.session_state.selected_degree) &
           (df['Field'] == st.session_state.selected_field)]['SubField'].dropna().unique()
    )
    st.session_state.selected_subfield = st.selectbox('**Select Specialization in this Field**', st.session_state.filtered_subfields)

    # College selection
    st.session_state.filtered_colleges = sorted(
        df[(df['Degree'] == st.session_state.selected_degree) &
           (df['Field'] == st.session_state.selected_field) &
           (df['SubField'] == st.session_state.selected_subfield)]['COLLEGE'].dropna().unique()
    )
    st.session_state.selected_college = st.selectbox('**Select College**', st.session_state.filtered_colleges)

    # Display college details if selected
    if st.session_state.selected_college:
        st.session_state.college_details = df[
            (df['Degree'] == st.session_state.selected_degree) &
            (df['Field'] == st.session_state.selected_field) &
            (df['SubField'] == st.session_state.selected_subfield) &
            (df['COLLEGE'] == st.session_state.selected_college)
        ]

        st.header('**College Details**')
        for column in [
            "DURATION", "COLLEGE FEE", "NIRF AND OTHER RANK(2022)", "MIN MARKS FOR ELIGIBILITY",
            "ENTRANCE NAME AND DURATION", "EXAM DETAILS", "TEST DATE", "APPLICATION PROCESS",
            "APPLICATION FEE", "SELECTION PROCESS", "INTAKE", "LINK", "Scholarships/Fellowships"
        ]:
            value = st.session_state.college_details[column].values[0]
            st.markdown(f"**{column.replace('_', ' ').title()}:** {value}")

        st.warning("*A complete list of all relevant scholarships will be provided when you download the report (PDF) on the next page.*")

    if st.button('Explore Career'):
        st.session_state.next_page = True
        st.experimental_rerun()

# Check if the next page should be displayed
if 'next_page' in st.session_state and st.session_state.next_page:
    # Display the next page logic
    # Assuming there's a module `Job` with a `main()` function
    import Job
    Job.main()
else:
    # Display the home page
    main()
