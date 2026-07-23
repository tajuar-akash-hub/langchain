from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()


#define the model 
model = ChatGroq(model = "llama-3.3-70b-versatile")

#define the parser 

parser = JsonOutputParser()


#define the prompt 

template = PromptTemplate(
    template = """
    Give me 5 facts about {topic}.
    {format_instruction}
     """, 
     input_variables=["topic"], 
     partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt = template.format(topic = "Machine Learning")

# print(prompt)

#Create the Chain
chain = template | model | parser


#invoke the chain 

result = chain.invoke({"topic": "Machine Learning"})

print(result)


