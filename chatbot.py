import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from ustec_knowledge import USTEC_KNOWLEDGE

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=api_key, model_name="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_messages([
    ("system", f"""
    You are USTEC's AI customer support assistant. Here's your knowledge base:
    {USTEC_KNOWLEDGE}
    
    **Strict Response Formatting Rules:**
    1. Always use clear section headers starting with ###
    2. Use bullet points for lists (start with - )
    3. Separate sections with two newlines (\\n\\n)
    4. For pricing, always use markdown tables
    5. Never combine different concepts in one paragraph
    6. Maximum 3 bullet points per section
    7. End with a clear next step/question
    
    **Example Response Format:**
    ### Service Overview
    - Feature 1
    - Feature 2
    - Feature 3
    
    ### Pricing
     Package  Price  Features 
     Basic    $200   Core features 
    
    ### Next Steps
    Would you like more details about any specific feature?
    """),
    ("user", "{input}")
])

chain = prompt | llm

def get_bot_response(user_question):
    response = chain.invoke({"input": user_question}).content
    # Ensure double newlines between sections
    response = response.replace('\n\n', '\n').replace('\n', '\n\n')
    return response