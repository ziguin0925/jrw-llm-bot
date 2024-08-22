from crewai import Crew, Agent, Task
from langchain_ollama import ChatOllama
from openai import OpenAI

llm = ChatOllama(
    model = 'llama3.1',
    base_url = 'http://127.0.0.1:11434'
)
# Crew : 러닝 크루 => N명(조직)
# Agent : 요원 => 1명 조직원
# Task : 미션

# 쇼핑몰 Agent 생성
# ctrl누르고 클릭해보기.
book_agent = Agent(
    role ='책 구매 어시스턴트',
    goal ='고객이 어떤 상품인지 설명을 하면 해당 상황에 맞는 우리 서점에 있는 책을 소개합니다.',
    backstory = '당신은 우리 서점의 모든 책 정보를 알고 있으며, 사람들의 상황에 맞는 책을 소개하는 전문가입니다.',
    llm =llm
)

recommend_book_task = Task(
    description = '고객의 상황에 맞는 최고의 추천 도서 제안하기.',
    # description = user_question,
    expected_output ='고객의 상황에 맞는 5개의 도서를 추천해주고, 해당 책을 추천한 이유를 알려줘',
    agent = book_agent
    
)


#요원과 밈션을 관리
crew = Crew(
    tasks = [recommend_book_task],
    agents= [book_agent],
    verbose=True
)

result = crew.kickoff()

print(result)


