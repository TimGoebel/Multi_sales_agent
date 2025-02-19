import openai
import streamlit as st


class SalesAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)
        
        self.agents = {
            "AI Lead Discovery Agent 🤖🔍": (
                "You are an AI agent specializing in identifying and qualifying high-value prospects across any industry. "
                "Analyze LinkedIn, GitHub, and company websites to find decision-makers and AI/ML teams that align with the given topic. "
                "Identify prospects based on industry relevance, job titles, funding activity, hiring trends, and engagement signals. "
                "Prioritize leads who demonstrate interest in AI adoption, automation, or emerging technologies. "
                "Provide structured, CRM-ready insights for personalized outreach."
            ),
            "AI Engagement & Outreach Agent ✉️🤖": (
                "You are an AI agent that automates and personalizes outreach. Send AI-personalized LinkedIn connection requests and emails. "
                "Generate messages based on the prospect’s interests & industry trends. Automate follow-ups with different touchpoints "
                "(text, video, case studies). Adjust messaging based on response sentiment."
            ),
            "AI Content & Authority Agent 📝🚀": (
                "You are an AI agent that establishes credibility by posting valuable content on AI innovations, automation, and business intelligence. "
                "Auto-generate and post weekly thought leadership content on {topic}. "  # ✅ Dynamic topic insertion
                "Share relevant case studies, whitepapers, and success stories tailored to the provided query. "
                "Monitor post engagement and DM hot leads. Use AI-generated comments to start discussions. "
            ),
            "AI Deal Closing & Scheduling Agent 📅💰": (
                "You are an AI agent that moves warm leads toward a sale. Automate meeting scheduling (syncs with Calendly or HubSpot). "
                "Send personalized demos based on client needs. Generate proposal drafts and pricing recommendations. "
                "Track responses and remind leads to book a call."
            )
        }

    def query_agent(self, agent_name, topic):
        """Queries the selected AI agent with a given topic and returns the response."""
        if agent_name not in self.agents:
            return "Invalid agent selection."

        # ✅ Dynamically replace {topic} in the Content & Authority Agent prompt
        system_prompt = self.agents[agent_name].format(topic=topic) if "{topic}" in self.agents[agent_name] else self.agents[agent_name]

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": topic}
            ]

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0  # Keeps responses more deterministic
            )

            response_text = response.choices[0].message.content.strip()

            # ✅ Debugging Output (Uncomment for testing)
            # st.write("DEBUG: OpenAI Response:", response_text)

            return response_text
        except openai.OpenAIError as e:
            return f"OpenAI API Error: {str(e)}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"

    def clear_agent_memory(self):
        """Clears session state and cached data to reset AI memory."""
        st.session_state.clear()  # Clear all stored session variables
        st.cache_data.clear()  # Reset cache
        st.rerun()  # Refresh the app
