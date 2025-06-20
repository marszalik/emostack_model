from __future__ import annotations
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

class OpenAiSrv():

    _instance = None

    @staticmethod
    def getInstance():
        if OpenAiSrv._instance is None:
            OpenAiSrv._instance = OpenAiSrv()
        return OpenAiSrv._instance


    def __init__(self) -> None:

       self.client = OpenAI(
           api_key=os.getenv("OPENAI_API_KEY")
            ,
        )
        

    def askQuestion(self, question, instruction = ""):
        completion = self.client.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4",
            messages=[
                # {"role": "system", "content": "Answer in polish language with twisted, black humor"},
                {"role": "system", "content": instruction},
                {"role": "user", "content": question}
            ]
        )

        return completion.choices[0].message.content