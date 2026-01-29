# WLM‑Agent — LangChain Reference Implementation

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Load system prompt
with open("prompts/system_prompt_wlm_agent.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

# Initialize model (OpenAI‑compatible)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

def run_wlm_agent(sentence: str) -> dict:
    """
    Runs WLM‑Agent on a single sentence and returns the JSON output.
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=sentence)
    ]

    response = llm(messages)
    return response.content  # JSON string

if __name__ == "__main__":
    test_sentence = "I always feel like people are judging me."
    output = run_wlm_agent(test_sentence)
    print(output)
