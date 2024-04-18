import os
from dotenv import load_dotenv, find_dotenv

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from services.third_parties.linkedin_scraper import LinkedinScraper
from services.third_parties.twitter_scrapper import TwitterScraper
from services.agents.linkedin_lookup_agent import LinkedInLookAgent
from services.agents.twitter_lookup_agent import TwitterLookAgent


class IceBreaker:
    SUMMARY_TEMPLATE = """
    Based on the provided LinkedIn profile information {linkedin_data} and recent Twitter posts {twitter_data}, please create:
    1. A concise summary of the person's professional background and recent activities, primarily based on LinkedIn data. Include the Twitter username if it is provided.
    2. Two notable facts about the individual, drawing on insights from both LinkedIn and any available Twitter data.

    Note: If the Twitter data shows little relevance to the LinkedIn information or is limited, explicitly mention the Twitter username.
    Alert: Importantly, always clarify at the end as a alert that the Twitter username might not accurate if you take any information from twitter or its twitter user
    Finnal message: At the end it also leaves a message saying that this info-statement was taken from linkedin and twitter.
    """
    def __init__(self) -> None:
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        self.linkedin_scraper = LinkedinScraper()
        self.twitter_scraper = TwitterScraper()
        self.linkedin_agent = LinkedInLookAgent()
        self.twitter_agent = TwitterLookAgent()


    def run_prompt(self, linkedin_data: str, twitter_data: str) -> str:
        summary_prompt_template = PromptTemplate(
            input_variables=["information"], template=self.SUMMARY_TEMPLATE
        )
        chain = LLMChain(llm=self.llm, prompt=summary_prompt_template)
        res = chain.invoke(input={"linkedin_data": linkedin_data, "twitter_data": twitter_data})
        return res

    def run(self, name, company):
        linkedin_profile_url = self.linkedin_agent.lookup(name, company)
        print(linkedin_profile_url)
        linkedin_data = self.linkedin_scraper.linkedin_profile(linkedin_profile_url)

        twitter_username = self.twitter_agent.lookup(name, company)
        twitter_data = self.twitter_scraper.fetch_tweets(twitter_username)


        response = self.run_prompt(linkedin_data, twitter_data)
        print(response)
