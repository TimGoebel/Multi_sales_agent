# Multi-Agent AI Sales Assistant 🤖

## Overview
The **Multi-Agent AI Sales Assistant** is a Streamlit-powered web application that automates lead discovery, outreach, content authority, and deal closing for AI-related sales. It integrates with OpenAI's API to provide intelligent sales insights and personalized automation.

## Features
- 🔍 **AI Lead Discovery Agent** - Identifies high-value prospects from LinkedIn, GitHub, and company websites.
- ✉️ **AI Engagement & Outreach Agent** - Automates and personalizes LinkedIn messages, follow-ups, and emails.
- 📝 **AI Content & Authority Agent** - Generates thought leadership content and engages with LinkedIn posts.
- 📅 **AI Deal Closing & Scheduling Agent** - Automates meeting scheduling and proposal generation.
- 📄 **PDF Export** - Save and download a PDF report of AI-generated sales insights.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/multi_sales_agent.git
cd multi-agent-sales-assistant
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run main.py
```
Alternatively, you can run the application using the `run.bat` file on Windows.
```bash
run.bat
```


## Usage
1. **Enter your OpenAI API Key** into the designated input field.
2. **Enter a query/topic** related to AI sales and lead generation.
3. **Run the Multi-Agent AI Sales Assistant** by clicking the button.
4. **Review the AI-generated responses** for lead discovery, outreach, content, and deal closing.
5. **Download a PDF report** by clicking "Save & Download PDF".

## Requirements
- Python 3.8+
- Streamlit
- OpenAI Python SDK (`openai`)
- FPDF for PDF generation

## Contributing
Feel free to submit issues and pull requests to enhance the functionality of the AI Sales Assistant!

## License
MIT License

### Future Summary of Enhancements
- Error Handling & Logging – Prevent silent failures
- Multi-Query Batch Processing – Query multiple agents at once
- API Rate Limit Handling – Handle API rate limits gracefully
- AI Response Analysis & Scoring – Score responses before returning
- Integration with External CRM – Automate lead storage into a CRM
- Personalization with User Context – AI remembers past conversations

---
🚀 Built for AI-driven sales automation!
