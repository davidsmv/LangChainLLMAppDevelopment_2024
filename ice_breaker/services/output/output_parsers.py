from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="Consolidated profile summary from LinkedIn.")
    facts: List[str] = Field(description="List of interesting facts about the individual.")
    twitter_alert: str = Field(description="Warning related to the accuracy of Twitter username.")
    final_message: str = Field(description="Final compiled statement regarding the profile.")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "twitter_alert": self.twitter_alert,
            "final_message": self.final_message
        }
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)


