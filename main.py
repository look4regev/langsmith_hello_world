#!/usr/bin/env python3

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
llm.invoke("Hello, world!")
