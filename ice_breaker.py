from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets

load_dotenv(find_dotenv())

name = "Carlos Montecinos Geisse"


def ice_break(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)
    twitter_username = twitter_lookup_agent(name)
    tweets = scrape_user_tweets(username=twitter_username)

    summary_template = """
    Given the LinkedIn information {linkedin_info} and twitter {twitter_info}
    about a person I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    3. A topic that may interest the person
    4. A creative Ice Breaker to open a conversation with the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_info", "twitter_info"],
        template=summary_template,
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(linkedin_info=linkedin_data, twitter_info=tweets))


if __name__ == "__main__":
    ice_break(name)
