from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import (
    StructuredOutputParser, ResponseSchema
)


load_dotenv()

#define the model 
model = ChatGroq(model = "llama-3.3-70b-versatile")


#Define the Schema 

reponse_schema = [

    ResponseSchema(
        name= "Fact_1",
        description = "The first fact about the topic"
    ),
    ResponseSchema(
        name = "Fact_2",
        description = "The second fact about the topic"
    ),
    ResponseSchema(
        name= "Fact_3",
        description = "The third fact about the topic"
    ),
    ResponseSchema(
        name= "Fact_4",
        description = "The fourth fact about the topic"
    ),
    ResponseSchema(
        name= "Fact_5",
        description = "The fifth fact about the topic"
    ),

]

#create the parser 

parser = StructuredOutputParser.from_response_schemas(
    reponse_schema
)

#creat the prompt 

template = PromptTemplate(
    template = """
    Give me 5 facts about {topic}.
    {format_instruction}
     """, 
     input_variables=["topic"], 
     partial_variables={"format_instruction":parser.get_format_instructions()}
)


#create the chain 

chain = template | model | parser 


#invoke the chan 

result = chain.invoke(
    {"topic": "Machine Learning"}
)

# print(result)

print(result['Fact_1'])