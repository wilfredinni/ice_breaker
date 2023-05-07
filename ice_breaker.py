from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv(find_dotenv())

linkedin_profile_url = linkedin_lookup_agent("Eden Marco")

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

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(info=linkedin_data))
