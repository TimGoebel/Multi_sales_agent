import openai

class SalesAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)
        
        self.agents = {
            "AI Lead Discovery Agent 🤖🔍": "You are an AI agent that specializes in finding and qualifying high-value prospects. Scan LinkedIn, GitHub, and company websites for AI/ML teams & decision-makers. Identify leads based on industry, job title, and engagement signals. Prioritize prospects based on past interactions, funding news, and hiring trends. Provide CRM-ready insights.",
            "AI Engagement & Outreach Agent ✉️🤖": "You are an AI agent that automates and personalizes outreach. Send AI-personalized LinkedIn connection requests and emails. Generate messages based on the prospect’s interests & industry trends. Automate follow-ups with different touchpoints (text, video, case studies). Adjust messaging based on response sentiment.",
            "AI Content & Authority Agent 📝🚀": "You are an AI agent that establishes credibility by posting valuable content. Auto-generate and post weekly thought leadership content on Computer Vision AI. Share relevant case studies, whitepapers, and success stories. Monitor post engagement and DM hot leads. Use AI-generated comments to start discussions.",
            "AI Deal Closing & Scheduling Agent 📅💰": "You are an AI agent that moves warm leads toward a sale. Automate meeting scheduling (syncs with Calendly or HubSpot). Send personalized demos based on client needs. Generate proposal drafts and pricing recommendations. Track responses and remind leads to book a call."
        }
    
    def query_agent(self, agent_name, prompt):
        if agent_name not in self.agents:
            return "Invalid agent selection."
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.agents[agent_name]},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return str(e)