from openai import OpenAI

def chat_with_llm_server(messages,url ) :
    try:
        print("inside chat mistral")
        client = OpenAI(
            base_url=url,api_key="hjbb",
           
        )
        chat_response = client.chat.completions.create(
            messages=messages,
            stream=True,
            model="mistralai/Mistral-7B-Instruct-v0.3",
            frequency_penalty=0.5,
            presence_penalty=-0.1,
            max_tokens=4000
        )
    
       
        print("initialized", chat_response)
        # print(type(chat_response))
        return chat_response
    except Exception as e:  
        print("Error in chat_with_llm_server", e)
        return None
