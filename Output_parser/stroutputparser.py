from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple terms"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke( { 
    "topic" : "Machine Learning"
 }  )


# print(result)

print(type(result))

