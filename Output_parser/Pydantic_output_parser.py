from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

#define the model 
model = ChatGroq(model = "llama-3.3-70b-versatile")


#Define the Schema 

class ModelEvaluation(BaseModel): 
    model_name : str = Field(description = "Name of the Machine Learning Model")

    accuracy : float = Field(
        gt = 0 , 
        lt = 1 , 
        description="Accuracy of the Model , greather than 0 and less than 1"
    )

    dataset : str = Field(
        description="Name of the Dataset used for evaluation"
    )


#parser 

parser = PydanticOutputParser(
    pydantic_object=ModelEvaluation
)


#prompt template 

template = PromptTemplate(
    template = """
             Generate the name, accuracy, and dataset of a fictional machine learning model trained for {task}
             {format_instruction}
             """, 
             input_variables=["task"], 
             partial_variables= {
                 "format_instruction": parser.get_format_instructions()
             }

)


#create chain 

chain = template | model | parser 


final_result = chain.invoke(
    {"task": "image_classification"}
)

print(final_result)