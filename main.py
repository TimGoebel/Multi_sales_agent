import streamlit as st
from sales_agent import SalesAgent
from fpdf import FPDF
import os

# Streamlit Web App Title
st.title("Multi-Agent AI Sales Assistant 🤖")

# Input field for OpenAI API Key
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Input field for user query (topic)
topic = st.text_area("Enter your query (topic):")

# Display buttons in the same row
col1, col2, col3 = st.columns(3)

with col1:
    run_clicked = st.button("Run Multi-Agent AI Assistant")

with col2:
    clear_memory_clicked = st.button("Clear Session Data")

with col3:
    save_pdf_clicked = st.button("Save & Download PDF")

# **Clear all stored session data only when explicitly requested**
if clear_memory_clicked:
    st.session_state.filtered_results = [] # Clear only the results, not the whole session state
    st.rerun() # Restart the app to reflect changes

# Initialize the SalesAgent class
sales_agent = SalesAgent(api_key)

# Store results in session state
if "results" not in st.session_state:
    st.session_state.results = {}

# Display agent results
if run_clicked:
    if not api_key or not topic:
        st.warning("Please enter both your OpenAI API Key and a query.")
    else:
        for agent_name in sales_agent.agents.keys():
            st.subheader(agent_name)
            with st.spinner("🔎 Processing information..."):
                response = sales_agent.query_agent(agent_name, topic)
            st.write(response)
            st.session_state.results[agent_name] = response

# Function to save results as a PDF
def save_as_pdf(results):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Multi-Agent AI Assistant Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    
    for agent_name, response in results.items():
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, agent_name.encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, response.encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(5)
    
    pdf_output_path = "multi_agent_report.pdf"
    pdf.output(pdf_output_path, 'F')
    return pdf_output_path

# Save and Download PDF
if save_pdf_clicked and st.session_state.results:
    pdf_file = save_as_pdf(st.session_state.results)
    with open(pdf_file, "rb") as f:
        st.download_button("Download Report as PDF", f, file_name="multi_agent_report.pdf", mime="application/pdf")
    os.remove(pdf_file)  # Ensure the file is removed after download
