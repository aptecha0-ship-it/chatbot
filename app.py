from google import genai
import streamlit as st



st.title("CHATBOT")

api_key = st.secrets["GOOGLE_API_KEY"]



client = genai.Client(api_key = api_key )




if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



user_input = st.chat_input("Ask anything")


if user_input:
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

   
    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"   
        contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}]             
        })

 
    response = client.models.generate_content(
        model="gemini-3-flash-preview",   
        contents=contents,
    )

    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)
