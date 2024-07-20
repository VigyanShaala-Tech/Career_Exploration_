# Career-Exploration

Welcome to the Career-Exploration GUI application! This app allows you to explore career details and generate PDF reports.

## Demo

Visit the [Demo](http://ec2-13-49-44-221.eu-north-1.compute.amazonaws.com:8501/) to explore the application.

## Objective:
This readme provides detailed instructions for running the Career-Exploration GUI application, exploring career and college details, and generating PDF reports. It serves as a guide for users, developers, and administrators, ensuring consistency, accuracy, and ease of use.

## Scope:
This readme applies to individuals involved in utilizing and managing the Career-Exploration GUI application and PDF report generation. It covers the end-to-end process from running the app to creating PDF reports.

## Repository Structure
- `scripts/`: Includes the Python script for generating PDF reports.
- `data_files/`: Placeholder for any data files required by the application.
- `sop/`: Documentation files related to the project.
- `graphics/`: Images and logo files related to the project.
- `s3_code/`: Python script to deploy files on s3.

## Prerequisites:
1. Python installed (version 3.6 or higher).
2. Required Python libraries installed (pandas, streamlit, boto3, PIL, etc.).
3. AWS S3 account with credentials.
4. Internet access for external resources.

## Instructions:

### Running the Streamlit Career Exploration App:

#### Method 1: Using GUI.bat File
1. Locate the `GUI.bat` file in the `scripts/` directory.
2. Double-click on `GUI.bat` to launch the application.
3. Alternatively, create a shortcut for `GUI.bat` on your desktop for convenient access.

#### Method 2: Using Streamlit Script
1. Open a command prompt or terminal.
2. Navigate to the `scripts/` directory using `cd path/to/your/application`.
3. Run the command: `streamlit run Home.py`.
4. Access the GUI at the provided URL (usually http://localhost:8501).
5. Enter your details and explore career options.

## Developer Instructions:

### Running the Streamlit Career Exploration App:

#### Importing Libraries:
1. Open a Python environment or code editor.
2. Import necessary libraries using the provided script.

#### Loading Data from AWS S3:
1. Obtain AWS S3 access credentials (AWS ID and Secret Access Key).
2. Replace AWS credentials and S3 bucket information in the code.
3. Load data from AWS S3 using provided code.

#### Converting Image to Base64 String:
1. Use the provided function to convert the logo image to a base64-encoded string.

#### Creating the Streamlit Interface:
1. Define the Streamlit interface within the `main()` function.
2. Implement user inputs and error handling as specified in the script.

#### Handling the Next Page:
1. Check if the next page should be displayed.
2. Display the next page using appropriate functions.

#### Running the Application:
- Follow Method 1 or Method 2 as mentioned in Instructions.

## Conclusion:
By following this comprehensive readme, users can effectively run the Career-Exploration GUI application, generate PDF reports, and developers can maintain and update the application.

## References:
- [Streamlit Documentation](https://streamlit.io/docs)
- [Python Documentation](https://www.python.org/doc/)
- [AWS S3 Documentation](https://aws.amazon.com/s3/)
- [FPDF Documentation](https://pyfpdf.readthedocs.io/)
