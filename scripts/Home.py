import pandas as pd
import streamlit as st
import io
from streamlit_option_menu import option_menu
import Job  # Import the Job12 module
from PIL import Image
import base64
from io import BytesIO



import requests
import pandas as pd
from io import BytesIO

# URL pointing to the CSV file
file_url = 'https://bvvaailuzioczysisnoc.supabase.co/storage/v1/object/sign/Career%20Exploration/STEM_Colleges_in_India_Dataset(Sheet1).csv?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vU1RFTV9Db2xsZWdlc19pbl9JbmRpYV9EYXRhc2V0KFNoZWV0MSkuY3N2IiwiaWF0IjoxNzIxMDIyMDY5LCJleHAiOjE4MDczMzU2Njl9.IZ_FrbbMLq7UfGkWlSBvAmxJUxiAd3Y52Lql4Wx0g9c&t=2024-07-15T05%3A41%3A07.517Z'
# Make a GET request to the URL to retrieve the CSV file
try:
    response = requests.get(file_url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Read the content of the response as a pandas DataFrame, specifying the appropriate encoding
    df = pd.read_csv(BytesIO(response.content), encoding='latin1')  # You can try 'latin1' encoding as an alternative
    # Proceed with processing the data in the dataframe 'df'
except requests.exceptions.RequestException as e:
    print("An error occurred while accessing the CSV file:", e)
except Exception as e:
    print("An error occurred while reading the CSV file:", e)


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
    #degree_order = ['Bachelors', 'Integrated Bachelors + Masters', 'Masters', 'Integrated Masters + PhD', 'PhD']
    #degree_order = ['Bachelors', 'Masters', 'Integrated Masters + PhD', 'PhD']

    st.session_state.qualified_degrees = df['Degree'].unique() 
    st.session_state.selected_degree = st.selectbox('**Select the Degree you want to pursue next (Your Aspiration Degree)**', st.session_state.qualified_degrees)

    st.session_state.filtered_fields = sorted([i for i in df[df['Degree'] == st.session_state.selected_degree]['Field'].unique() if isinstance(i, str)])
    st.session_state.selected_field = st.selectbox('**Select Area of Interest**', st.session_state.filtered_fields)

    st.session_state.filtered_subfields = sorted([i for i in df[(df['Degree'] == st.session_state.selected_degree) & (df['Field'] == st.session_state.selected_field)]['SubField'].unique() if isinstance(i, str)])
    st.session_state.selected_subfield = st.selectbox('**Select Specilization between this Field**', st.session_state.filtered_subfields)

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
        #st.markdown(f"**NIRF and Other Rank (2022):** {st.session_state.college_details['NIRF AND OTHER RANK(2022)'].values[0]}")
        #st.markdown(f"**Minimum Marks for Eligibility:** {st.session_state.college_details['MIN MARKS FOR ELIGIBILITY'].values[0]}")
        st.markdown(f"**Minimum Eligibility:** {st.session_state.college_details['Eligiblity Criteria'].values[0]}")
        #st.markdown(f"**Entrance Name and Duration:** {st.session_state.college_details['ENTRANCE NAME AND DURATION'].values[0]}")
        #st.markdown(f"**Exam Details:** {st.session_state.college_details['EXAM DETAILS'].values[0]}")
        #st.markdown(f"**Test Date:** {st.session_state.college_details['TEST DATE'].values[0]}")
        #st.markdown(f"**Application Process:** {st.session_state.college_details['APPLICATION PROCESS'].values[0]}")
        #st.markdown(f"**Application Fee:** {st.session_state.college_details['APPLICATION FEE'].values[0]}")
        #st.markdown(f"**Selection Process:** {st.session_state.college_details['Selection Process'].values[0]}")
        #st.markdown(f"**Intake:** {st.session_state.college_details['INTAKE'].values[0]}")
        #st.markdown(f"**Link:** {st.session_state.college_details['LINK'].values[0]}")
        #st.markdown(f"**Scholarships for this College:** {st.session_state.college_details['Scholarships/Fellowships'].values[0]}")
        st.markdown(f"**Selection Criteria:** {st.session_state.college_details['Selection Process'].values[0]}")
        st.markdown(f"**Exam to Qualify:** {st.session_state.college_details['Exam'].values[0]}")
        st.markdown(f"**Available Seats:** {st.session_state.college_details['Seats'].values[0]}")
        st.markdown(f"**Mode of exam:** {st.session_state.college_details['Mode'].values[0]}")
        st.warning(f"*A complete list of all relevant scholarships will be provided when you download the report (pdf) on the next page.*")

    if st.button('Explore Career'):
        # Set a session state variable to indicate that the next page should be displayed
        st.session_state.next_page = True
        # Rerun the script
        st.experimental_rerun()

# Check if the next page should be displayed
if 'next_page' in st.session_state and st.session_state.next_page:
    # Display the Job12.py page
    Job.main()
else:
    # Display the Home.py page
    main()
