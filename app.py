import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

# Page config
st.set_page_config(page_title="LLM Temperature Explorer", page_icon="🔥")
st.title("🔥 LLM Temperature Explorer (Groq + LangChain)")
st.markdown("Enter a topic and explore how **temperature** affects creativity.")

# User input
topic = st.text_input("Enter your story topic", placeholder="a robot that wants to become a chef")
temperature = st.slider("Select Temperature", 0.0, 1.0, 0.7, 0.1)

# On submit
if st.button("Generate Story"):
    if not topic.strip():
        st.warning("Please enter a valid topic.")
    else:
        # Construct prompt securely
        template = PromptTemplate.from_template("Write a short story about: {topic}")
        prompt_text = template.format(topic=topic.strip())
        message = HumanMessage(content=prompt_text)

        # Create model (Groq + LangSmith tracking enabled via env vars)
        llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=temperature)
        response = llm.invoke([message])

        st.markdown("### 📝 Generated Story")
        st.write(response.content)