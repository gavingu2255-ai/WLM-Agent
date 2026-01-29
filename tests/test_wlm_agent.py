import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import json
import pytest

from src.wlm_agent_langchain import run_wlm_agent


class DummyResponse:
    """A fake LLM response object with a .content attribute."""
    def __init__(self, content: str):
        self.content = content


class DummyLLM:
    """A fake LLM that returns a fixed JSON response."""
    def __init__(self, output: dict):
        self.output = output

    def invoke(self, messages):
        return DummyResponse(json.dumps(self.output))


@pytest.fixture
def sample_output():
    """A minimal valid WLM-Agent output for testing."""
    return {
        "structure_diagnosis": {
            "dimension": "3D",
            "subject_position": "foregrounded",
            "fold_state": "unfolded",
            "noise_sources": []
        },
        "tension_map": [],
        "unfolded_expression": "A structural rendering.",
        "recommended_shift": "A minimal structural shift.",
        "rewritten_structure_language": "A rewritten structural sentence."
    }


def test_run_wlm_agent(monkeypatch, sample_output):
    """
    Test that run_wlm_agent returns valid JSON and respects the schema structure.
    """

    # Patch the internal _get_llm() to return our dummy LLM
    monkeypatch.setattr(
        "src.wlm_agent_langchain._get_llm",
        lambda: DummyLLM(sample_output)
    )

    result = run_wlm_agent("test input")

    # Basic structure checks
    assert isinstance(result, dict)
    assert "structure_diagnosis" in result
    assert "tension_map" in result
    assert "unfolded_expression" in result
    assert "recommended_shift" in result
    assert "rewritten_structure_language" in result

    # Ensure the dummy output is passed through unchanged
    assert result == sample_output
