from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

information = """
Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business
magnate and investor. He is the founder, CEO and chief engineer of SpaceX;
angel investor, CEO and product architect of Tesla, Inc.; owner and CEO of
Twitter; founder of the Boring Company; co-founder of Neuralink and OpenAI;
and president of the philanthropic Musk Foundation. With an estimated net
worth of around $192 billion as of March 27, 2023, primarily from his
ownership stakes in Tesla and SpaceX,[4][5] Musk is the second-wealthiest
person in the world, according to both the Bloomberg Billionaires Index and
Forbes's real-time billionaires list.
"""

if __name__ == "__main__":

    summary_template = """
    Given the information {info} about a person from I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(info=information))
