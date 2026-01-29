import json
import os
from pathlib import Path
from typing import Any, Dict

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


def _load_system_prompt() -> str:
    """
    Load the WLM-Agent system prompt from prompts/system_prompt_wlm_agent.txt,
    or from WLM_SYSTEM_PROMPT_PATH if set.
    """
    override_path = os.getenv("WLM_SYSTEM_PROMPT_PATH")
    if override_path:
        path = Path(override_path)
    else:
        # Resolve relative to this file: ../prompts/system_prompt_wlm_agent.txt
        path = Path(__file__).resolve().parent.parent / "prompts" / "system_prompt_wlm_agent.txt"

    with path.open("r", encoding="utf-8") as f:
        return f.read().strip()


def _get_llm() -> ChatOpenAI:
    """
    Construct the LangChain ChatOpenAI LLM.

    Expects OPENAI_API_KEY to be set in the environment.
    """
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.0,
    )


def run_wlm_agent(text: str) -> Dict[str, Any]:
    """
    Run WLM-Agent on a single input sentence.

    Parameters
    ----------
    text : str
        The natural-language input to diagnose.

    Returns
    -------
    Dict[str, Any]
        A JSON object matching the WLM-Agent output schema:
        - structure_diagnosis
        - tension_map
        - unfolded_expression
        - recommended_shift
        - rewritten_structure_language
    """
    system_prompt = _load_system_prompt()
    llm = _get_llm()

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text),
    ]

    response = llm.invoke(messages)
    raw_content = response.content

    # The system prompt requires: "All outputs must strictly follow the JSON schema
    # and must not include commentary outside the JSON object."
    # We still defensively parse JSON here.
    try:
        parsed = json.loads(raw_content)
    except json.JSONDecodeError as e:
        raise ValueError(f"WLM-Agent returned non-JSON output: {raw_content}") from e

    return parsed
