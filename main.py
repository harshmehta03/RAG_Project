from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant 

Here are some revelant reviews : {reviews}

Here is the question : {question}
""" 

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True :
    print("\n\n---------------------------------------------------")
    question = input("Ask a question (q to quit) : ")
    print("---------------------------------------------------")
    if question.lower() == "q":
        break
    
    reviews = retriver.invoke(question)
    result = chain.invoke({"reviews": [], "question" : question})
    print(result)



