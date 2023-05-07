from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv(find_dotenv())

if __name__ == "__main__":
    summary_template = """
    Given the LinkedIn information {info} about a person from I
    want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        "https://www.linkedin.com/in/harrison-chase-961287118/"
    )

    print(chain.run(info=linkedin_data))
