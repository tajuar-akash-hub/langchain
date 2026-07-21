from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional
load_dotenv()


model = ChatGroq(model= "llama-3.3-70b-versatile")

#define the schema 

class ResumeAnalysis(TypedDict):

    key_skills : Annotated[  list[str], "Extract all important technical and soft skills from the resume" ]

    summary : Annotated[str, "write a brief summary of the Candidate's profile"]

    experience_level : Annotated[ Literal["entry_level","mid-level","senior-level"], "Classify the Candidate's Experience level" ]

    strengths : Annotated[ Optional[list[str]], "List the candidate's major strengths" ]

    weaknesses : Annotated[ Optional[list[str]], "List the candidate's possible weaknesses or ares for improvement" ]


    candidate_name : Annotated[ str, "Extract the name of the Candidate from the resume" ]



#create structured output 

structured_model = model.with_structured_output(ResumeAnalysis)


#invoke the model 

result = structured_model.invoke(
    """My name is  Mahir Tajuar Akash. I am a Computer Science graduate with two years
    of experience working as a Machine Learning Engineer.

    I have experience with Python, PyTorch, TensorFlow, Scikit-learn,
    FastAPI, Docker, Kubernetes, MLflow, and AWS. I have built machine
    learning pipelines, deployed deep learning models, and developed
    REST APIs for AI applications.

    I also have experience working with LangChain and Retrieval-Augmented
    Generation (RAG) systems.

    My main strength is my ability to build complete machine learning
    systems from data preprocessing to deployment. However, I have limited
    experience managing large engineering teams and need to improve my
    system design skills.

    Education:
    BSc in Computer Science and Engineering.
    """
)

# print(result)
# print(result['candidate_name'])

# print(type(result))

print(result)



