import streamlit as st
import os
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader

os.environ['OPENAI_API_KEY'] = st.secrets.OPENAI_API_KEY
session = st.session_state


if 'job_url' not in session:
    session.job_url = ""

if 'document' not in session:
    session.document = None

if 'is_setup_done' not in session:
    session.is_setup_done = False

if 'query_engine' not in session:
    session.query_engine = None

if 'query' not in session:
    session.query = ""



st.title("Welcome to job-info app")

st.text_input("Enter the url of the job:", key='job_url')

st.write("For example: https://www.governmentjobs.com/careers/sanjoseca/jobs/4220478/school-crossing-guard-police-department?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic")

def create_query_engine(documents):
    index = SummaryIndex.from_documents(documents)
    return index.as_query_engine()

load_button = st.button("Load the document")

if session.job_url:
    with st.spinner("Loading the data..."):
        # st.write(session.job_url)
        documents = SimpleWebPageReader(
            html_to_text=True).load_data([session.job_url])

        session.document = documents
        session.query_engine = create_query_engine(documents)

        session.is_setup_done = True
    st.info("Sucessfully loaded the document")



st.text_input("Ask any question based on the document", key='query')

st.write("For example: What is the job posting about?")
submit_button = st.button("Search the document")

if session.query and submit_button:
    if not session.is_setup_done:
        st.error("Please complete the setup before making any query")
    else:
        with st.spinner("Generating output..."):
            response = session.query_engine.query(session.query)
        st.write(response.response)


