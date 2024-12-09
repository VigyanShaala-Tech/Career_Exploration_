#%pip install fpdf2
import io
import tempfile
from io import BytesIO
from fpdf import FPDF, HTMLMixin
import pandas as pd
import streamlit as st
import base64
import requests
import PIL.Image as Image




class PDF(FPDF,HTMLMixin):
    def __init__(self, width, height):
        super().__init__('P', 'mm', (width, height))
        self.width = width
        self.height = height

    def header(self):
         # Reset the text color to black before adding the header
        self.set_text_color(0, 0, 0)
        
        
        # Load the original image
        from PIL import Image
        from PIL import ImageShow

        # Open the PNG image file
        

# Function to get image from URL
        def get_image_from_url(image_url):
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            return img

# URL of the image from Supabase
        image_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/VS-logo.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vVlMtbG9nby5wbmciLCJpYXQiOjE3MzM3MTUwOTQsImV4cCI6MTczNDMxOTg5NH0.gtfDA2Hhzeu12q9j4Ee8maC6jMLvFicS0O9xwdToXn8&t=2024-12-09T03%3A31%3A28.858Z"

# Load the image from the URL
        img = get_image_from_url(image_url)


        # Function to get image from URL
        def get_image_from_url(image_url):
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            return img

# URL of the image from Supabase
        image_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Watermark.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vV2F0ZXJtYXJrLnBuZyIsImlhdCI6MTczMzcxNTEyMiwiZXhwIjoxNzM0MzE5OTIyfQ.nO6QFtU94xh6B8K5J-MAYUvS4hHJwjfm46BpHEhod1o&t=2024-12-09T03%3A31%3A57.073Z"

# Load the image from the URL
        bg_image = get_image_from_url(image_url)




        #bg_image = r"C:\Users\User\Desktop\Career-Exploration-main\graphics\Watermark.png"

        #Set the background image as the page background
        temp_bg_file = tempfile.mktemp(suffix=".png")
        bg_image.save(temp_bg_file, format="PNG")
        self.image(temp_bg_file, x=50, y=50, w=self.width/2, h=self.height/2)

        # Load the logo
        #logo = r"C:\Users\User\Desktop\Career-Exploration-main\graphics\VS-logo.png"
        #img = Image.open(logo)
        
        # Save the logo to a temporary file
        temp_image_file = tempfile.mktemp(suffix=".png")
        img.save(temp_image_file, format="PNG")
       
        
        # Define logo size
        logo_width = 26  # You can adjust the size as you need
        logo_height = 20  # You can adjust the size as you need

        # Add the logo on the top right corner
        self.image(temp_image_file, x = self.width - logo_width - 10, y = 10, w = logo_width, h = logo_height)

        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Career Exploration Report', 0, 1, 'C')
        self.cell(0, 10, '', 0, 1, 'C')
        
    
    def add_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'C')
        self.cell(0, 10, '', 0, 1, 'C')
       

    def add_college_details_title(self):
        self.add_title('College Details Report')

    def add_job_details_title(self):
        self.add_title('Job Details Report')

    def add_scholarship_details_title(self):
        self.add_title('Scholarship Details Report')
    

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, content):
        self.set_font('Arial', '', 12)
        line_height = 5  # Set the desired interline spacing
        lines = content.split('\n')
        for line in lines:
            if ":" in line:
                # If the line contains a colon (":"), consider it as a content header and display it in bold
                parts = line.split(":")
                self.set_font('Arial', 'B', 12)
                self.cell(0, line_height, txt=parts[0] + ":", ln=False)
                self.set_font('Arial', '', 12)
                self.cell(0, line_height, txt=parts[1], ln=True)
            else:
                self.cell(0, line_height, txt=line, ln=True)
        self.ln()

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        
        # Set the text color to black before adding page numbers
        self.set_text_color(0, 0, 0)
        
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

        # Reset text color to black
        self.set_text_color(0, 0, 0)
        
    def add_bold_text(self, text):
        self.set_font('Arial', 'B', 12)
        line_height = 5  # Set the desired interline spacing
        lines = text.split('\n')
        for line in lines:
            self.cell(0, line_height, txt=line, ln=True)
        self.ln()  # Add a line after each detail
        self.set_font('Arial', '', 12)  # Set the font back to normal for the next line
        
    def add_scholarship_table(self, data):
        # Set column names for the table
        column_names = ['Scholarship Name']

        # Set column widths
        col_widths = [100]

        # Set font for table header
        self.set_font('Arial', 'B', 12)

        # Add table header
        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()

        # Set font for table content
        self.set_font('Arial', '', 10)  # Reduce font size to fit the content

        # Add table content
        for row in data:
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()

    def add_scholarship_offered_by_table(self, data):
        column_names = ['Offered by', 'Govt./Private', 'For study in']
        col_widths = [70, 40, 60]

        self.set_font('Arial', 'B', 12)

        # Ensure the column names have the same number of elements as col_widths
        assert len(column_names) == len(col_widths)


        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()

        self.set_font('Arial', '', 10)

        for row in data:
            assert len(row) == len(col_widths)
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()

    def add_scholarship_duration_table(self, data):
        column_names = ['Duration', 'Award amount', 'Application deadline']
        col_widths = [70, 40, 60]

        self.set_font('Arial', 'B', 12)

        assert len(column_names) == len(col_widths)


        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()

        self.set_font('Arial', '', 10)

        for row in data:
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()
            
    def add_scholarship_details(self, scholarship_name, details):
        # Set font for scholarship details content
        self.set_font('Arial', '', 12)

        # Define the width for the keys and values
        key_width = 60
        value_width = self.w - key_width - self.r_margin - self.l_margin

        # Define the space after the colon for value
        colon_space = 4  # Adjust this value as needed
        
        # Loop through scholarship details and add them to the PDF
        for key, value in details.items():
            # Convert the key and value to strings using 'utf-8' encoding
            key_str = str(key).encode('latin-1', 'replace').decode('latin-1')
            value_str = str(value).encode('latin-1', 'replace').decode('latin-1')

                
        # Calculate the combined width of key and value
            # Calculate the width of the key without considering value or colon
            key_colon_width = self.get_string_width(key_str + ": ")
        
        # Check if the combined width fits within the available width
            if key_colon_width + self.get_string_width(value_str) <= value_width:
            # Set font to bold for the key
                self.set_font('Arial', 'B', 12)
                # Print the key in bold
                self.cell(key_colon_width, 8, txt=f"{key_str}:", ln=False)
            # Reset font to regular for the value
                self.set_font('Arial', '', 12)
                
                # Check if the value is a URL
                if "http" in value:
                # Set the text color to blue
                    self.set_text_color(0, 0, 255)
                    
                # Print the wrapped value
                self.cell(colon_space)  # Add the desired space after the colon
                self.cell(0, 8, txt=value_str, ln=True)
                # Reset text color to black
                self.set_text_color(0, 0, 0)
            else:
                # Set font to bold for the key
                self.set_font('Arial', 'B', 12)
                # Print the key in bold with a colon
                self.cell(0, 8, txt=f"{key_str}:", ln=True)

                # Reset font back to normal for the value
                self.set_font('Arial', '', 12)

                # Print wrapped value
                # Check if the value is a URL
                if "http" in value:
                # Set the text color to blue
                    self.set_text_color(0, 0, 255)
            # Print the wrapped value
                self.multi_cell(self.w - self.r_margin - self.l_margin, 8, txt=value_str, align='L')
            # Reset text color to black
                self.set_text_color(0, 0, 0)

        self.ln()

        # Reset font back to normal
        self.set_font('Arial', '', 12)
        

def add_detail(self, detail, separator="\n"):
    # Split into column name and value
    column_name, value = detail.split(": ", 1)

    # Remove leading and trailing whitespace from the value
    value = value.strip()

    # Replace newline characters with spaces in the value
    value = value.replace("\n", " ")

    # Check for URL and set color
    url_detected = "http" in value or "www." in value

    # Set font for column name (bold) and value (regular)
    self.set_font('Arial', 'B', 12)

    # Calculate width for the value
    value_width = self.w - self.l_margin - self.r_margin

    # Check if the value is longer than the available space
    if self.get_string_width(column_name) + self.get_string_width(": ") + self.get_string_width(value) <= value_width:
        # Print column name
        self.cell(self.get_string_width(column_name) + self.get_string_width(": "), 7, txt=column_name + ": ", ln=False)

        # Print value
        self.set_font('Arial', '', 12)
        
        # Set text color to blue if URL is detected
        if url_detected:
            self.set_text_color(0, 0, 255)  # Set text color to blue
        
        self.multi_cell(value_width - self.get_string_width(column_name) - self.get_string_width(": "), 7, txt=value, align='L')
        
        # Reset text color to black
        self.set_text_color(0, 0, 0)
    else:
        # Print concatenated column name and value with a 2-space gap
        column_value = f"{column_name}:  "
        self.cell(0, 7, txt=column_value, ln=True)

        # Reset font to regular for value
        self.set_font('Arial', '', 12)

        # Split multi-line value into individual lines
        lines = value.split('\n')

        for line in lines:
            # Check for URL and set color
            url_detected = "http" in line or "www." in line
            
            if url_detected:
                self.set_text_color(0, 0, 255)  # Set text color to blue

        # Print value
            self.multi_cell(value_width, 7, txt=value, align='L')  # Adjust line_height as needed

        # Reset text color to black
        self.set_text_color(0, 0, 0)

    # Add the custom separator after each detail
    self.set_font('Arial', '', 5)  # Adjust font size for the separator
    self.cell(0, 2, separator, ln=True)

# Load the Excel file into a pandas DataFrame

# URL pointing to the CSV file

# Load the Excel file into a pandas DataFrame
# Define file URLs for Supabase storage
job_file_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Job_S3.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vSm9iX1MzLnhsc3giLCJpYXQiOjE3MzM1MTI3MjAsImV4cCI6MTczNDExNzUyMH0.zQfwABwUJtnA41UQ_Q8L8YbYZkBfGfxsiM5iXHbQ5fo&t=2024-12-06T19%3A18%3A41.253Z"
scholarship_file_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Scholarship_S3.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vU2Nob2xhcnNoaXBfUzMueGxzeCIsImlhdCI6MTczMzUxMjc0MywiZXhwIjoxNzM0MTE3NTQzfQ.JzGv8Mub-PS_GJKOVUyZMj7NS_oGRofX6wlJodoX9EI&t=2024-12-06T19%3A19%3A03.629Z"

@st.cache_resource
def load_excel_from_url(file_url):
    """Load an Excel file from a given URL."""
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        return pd.read_excel(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the file: {e}")
        return pd.DataFrame()

@st.cache_resource
def filter_job_titles(df, selected_field):
    """Filter job titles based on the selected field."""
    if df.empty:
        return []
    return df[df["Field"] == selected_field]["Job Titles"].unique()

class PDF(FPDF):
    """Custom PDF class for generating formatted PDFs."""
    
    def add_title(self, title):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, title, ln=True, align="C")
        self.ln(10)
    
    def add_section(self, heading, content_list):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, heading, ln=True)
        self.set_font("Arial", "", 11)
        for item in content_list:
            self.multi_cell(0, 10, item)
        self.ln(5)
    
    def add_bold_text(self, text):
        self.set_font("Arial", "B", 11)
        self.multi_cell(0, 10, text)
    
    def add_scholarship_details_title(self):
        self.add_title("Scholarship Details")
    
    def add_scholarship_details(self, name, details):
        self.add_bold_text(f"Scholarship Name: {name}")
        for key, value in details.items():
            self.multi_cell(0, 8, f"{key}: {value}")
        self.ln(5)

def clean_text(text):
    """Clean text to handle non-Latin-1 characters."""
    try:
        return text.encode("latin-1", "replace").decode("latin-1")
    except UnicodeEncodeError:
        return "[Non-Latin-1 Character]"

def main():
    st.title("Job and Scholarship Details Report")

    # Load data from Supabase URLs
    job_df = load_excel_from_url(job_file_url)
    scholarship_df = load_excel_from_url(scholarship_file_url)

    if job_df.empty or scholarship_df.empty:
        st.error("Failed to load job or scholarship details. Please try again later.")
        return

    # Select a field
    fields = sorted(job_df["Field"].unique())
    selected_field = st.selectbox("Select Field", options=["Select a field"] + fields)

    if selected_field == "Select a field":
        st.warning("Please select a valid field.")
        return

    # Filter job titles
    filtered_job_titles = filter_job_titles(job_df, selected_field)
    selected_job_title = st.selectbox("Select Job Title", options=["Select a job title"] + list(filtered_job_titles))

    if selected_job_title == "Select a job title":
        st.warning("Please select a valid job title.")
        return

    # Display job details
    job_details = job_df[(job_df["Field"] == selected_field) & (job_df["Job Titles"] == selected_job_title)]
    st.header("Job Details")
    st.markdown(f"**Field:** {selected_field}")
    st.markdown(f"**Job Title:** {selected_job_title}")
    st.markdown(f"**Job Description:** {job_details['Job Description'].values[0]}")
    st.markdown(f"**Work Environment:** {job_details['Work Environment'].values[0]}")
    st.markdown(f"**Key Competency:** {job_details['Key Competancy'].values[0]}")

    # Filter scholarships
    scholarships = scholarship_df[scholarship_df["Field"] == selected_field]

    # Generate PDF using the custom PDF class
    pdf = PDF()  # Use the custom PDF class
    pdf.add_page()

    # Add title
    pdf.add_title("Progress Report")
    pdf.set_left_margin(20)  # Adjust the left margin (default is 10 mm)
    pdf.set_right_margin(20)  

    # Set font 
    pdf.set_font("Arial", "B", 14)


    # Add college details
    #pdf.add_college_details_title()

    # Add college content
    college_content = [
        f"Student Name: {st.session_state.student_name}",
        f"Qualified Degree: {st.session_state.selected_degree}",
        f"Field: {st.session_state.selected_field}",
        f"Subfield: {st.session_state.selected_subfield}",
        f"College: {st.session_state.selected_college}",
        f"Duration: {st.session_state.college_details['DURATION'].values[0]}",
        f"College Fee: {st.session_state.college_details['COLLEGE FEE'].values[0]}",
        
    ]
    pdf.add_section("College Details", college_content)

    # Add separator line
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(10)  # Add space after the separator line

    pdf.set_font("Arial", "B", 14)


    # Add job details
    job_content = [
        f"Job Title: {selected_job_title}",
        f"Job Description: {job_details['Job Description'].values[0]}",
        f"Work Environment: {job_details['Work Environment'].values[0]}",
        f"Key Competancy: {job_details['Key Competancy'].values[0]}",
        f"Available Skill Training Schemes: {job_details['Available skill training schemes'].values[0]}",
        f"Sample Training & Courses: {job_details['Sample training & courses'].values[0]}",
        f"Career Path Progression: {job_details['Career path progression'].values[0]}",
        f"Probable Employers: {job_details['Probable Employers'].values[0]}",
    ]
    pdf.add_section("Job Details", job_content)

    # Draw a separator line after job content
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(10)
            
    # Set font for the "Scholarship Details" section to bold
    pdf.set_font("Arial", "B", 14)

    # Add scholarship details
    if not scholarships.empty:
        pdf.add_scholarship_details_title()
        for _, row in scholarships.iterrows():
            details = {
                "Scholarship name":row["Scholarship Name"],
                "Offered by": row["Offered by"],
                "Govt./Private": row["Govt./Private"],
                "Eligibility Criteria":row["Eligibility criteria"],
                "Award Amount": row["Award amount"],
                "Things covered by the award":row["Things covered by the award"],
                "Application Deadline": row["Application deadline"],
            }
            pdf.add_scholarship_details(row["Scholarship Name"], details)

# Allow PDF download
    pdf_output = pdf.output(dest="S").replace('\u200b', '').encode("latin1", errors="replace")
    st.download_button(
        label="Download PDF",
        data=pdf_output,
        file_name=f"{selected_field}_progress_report.pdf",
        mime="application/pdf",
    )
