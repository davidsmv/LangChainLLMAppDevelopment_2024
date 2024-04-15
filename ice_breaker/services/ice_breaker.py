import os
from dotenv import load_dotenv, find_dotenv

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from services.third_parties.linkedin_scraper import LinkedinScraper
from services.agents.linkedin_lookup_agent import LinkedInLookAgent
from services.agents.twitter_lookup_agent import TwitterLookAgent


class IceBreaker:
    SUMMARY_TEMPLATE = """
    Given the information {information} about a person I want
    you to create:
    1. A short summary
    2. two interesting facts about them
    """
    def __init__(self) -> None:
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        self.linkedin_scraper = LinkedinScraper()
        self.linkedin_agent = LinkedInLookAgent()
        self.twitter_agent = TwitterLookAgent()


    def run_prompt(self, information: str) -> str:
        summary_prompt_template = PromptTemplate(
            input_variables=["information"], template=self.SUMMARY_TEMPLATE
        )
        chain = LLMChain(llm=self.llm, prompt=summary_prompt_template)
        res = chain.invoke(input={"information": information})
        return res

    def run(self, name, company):
        linkedin_profile_url = self.linkedin_agent.lookup(name, company)
        print(linkedin_profile_url)
        linkedin_data = self.linkedin_scraper.linkedin_profile(linkedin_profile_url)

        twitter_username = self.twitter_agent.lookup(name, company)
        print("username: ", twitter_username)

        response = self.run_prompt(linkedin_data)
        print(response)
