# Job Info App

This is a Streamlit-based web application that extracts and queries information from job postings on websites. It uses the LlamaIndex and OpenAI APIs to process web pages and allows users to ask questions about job postings directly from the app.

## Features

- Load job postings from URLs and extract information.
- Query job postings using natural language questions.
- Use OpenAI GPT models to generate answers based on the content of job postings.

## Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.8+**
- **Streamlit** for building the web app.
- **OpenAI API key** for generating responses.
- **LlamaIndex** for processing and querying documents.

## Installation and Setup

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to Streamlit secrets:

   Create a `secrets.toml` file inside the `.streamlit` directory:

   ```bash
   mkdir -p .streamlit
   echo "[secrets]" > .streamlit/secrets.toml
   echo "OPENAI_API_KEY = '<your_openai_api_key>'" >> .streamlit/secrets.toml
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## How to Use

1. Enter the URL of the job posting you want to query.
2. Click the "Load the document" button to load and process the job posting.
3. Once the document is loaded, enter your questions in the input field.
4. Click the "Search the document" button to get the response based on the loaded document.

## Example Usage

- Enter the URL of the job posting:
  
  ```text
  https://www.governmentjobs.com/careers/sanjoseca/jobs/4220478/school-crossing-guard-police-department?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic
  ```

- Example query:
  
  ```text
  What is the job posting about?
  ```

## License

This project is licensed under the MIT License.
