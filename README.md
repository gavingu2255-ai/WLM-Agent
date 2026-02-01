<p align="left">

  <!-- Build / Test Status -->
  <a href="https://github.com/gavingu2255-ai/WLM-Agent/actions">
    <img src="https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square" alt="Tests Passing">
  </a>

  <!-- Python Version -->
  <img src="https://img.shields.io/badge/python-3.11-blue?style=flat-square" alt="Python 3.11">

  <!-- License -->
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT License">
  </a>

  <!-- Repo Size -->
  <img src="https://img.shields.io/github/repo-size/gavingu2255-ai/WLM-Agent?style=flat-square" alt="Repo Size">

  <!-- Last Commit -->
  <img src="https://img.shields.io/github/last-commit/gavingu2255-ai/WLM-Agent?style=flat-square" alt="Last Commit">

  <!-- Stars -->
  <img src="https://img.shields.io/github/stars/gavingu2255-ai/WLM-Agent?style=flat-square" alt="GitHub Stars">

</p>

<p align="center">
  <h1>WLM‑Agent</h1>
  <p>The official implementation layer of the Wujie Language Model (WLM)</p>
</p>

---
[SUBJECT_WLM_AGENT]
Mode: Non-Reflective Structural Alignment
Framework: WLM 1.2
Safety_Lock: No Persona, No Narrative, Just Structure.
Target: Eliminating terminal tension through dimensional fold recognition.

# WLM‑Agent  
Official implementation layer of the Wujie Language Model (WLM)

WLM‑Agent is the reference implementation of the WLM Structure Diagnosis Engine.  
It transforms natural language into structure‑first representations using:

- dimensional analysis  
- fold‑state detection  
- boundary mapping  
- tension mapping  
- structural unfolding  
- structure‑language rewriting  

This repository provides the **system prompt**, **schemas**, and **examples** required to implement the WLM protocol on any LLM backend.

---

## 📚 Relationship to WLM

This repository is the **implementation layer** of the Wujie Language Model (WLM).  
The theoretical foundations, dimensional framework, and structural language are defined in:

[https://github.com/gavingu2255-ai/WLM-Open-Source](https://github.com/gavingu2255-ai/WLM-Open-Source)

WLM = theory  
WLM‑Agent = implementation

---

## 📁 Repository Structure
WLM-Agent/
│
├── README.md
│
├── prompts/
│   └── system_prompt_wlm_agent.txt
│
├── schemas/
│   ├── tension_map_schema.json
│   └── structure_diagnosis_schema.json
│
├── examples/
│   ├── README.md
│   ├── README_engineer.md
│   │
│   ├── input/
│   │   ├── sentence_01.txt
│   │   ├── sentence_02.txt
│   │   ├── sentence_03.txt
│   │   ├── ...
│   │   └── sentence_20.txt
│   │
│   └── output/
│       ├── sentence_01.json
│       ├── sentence_02.json
│       ├── sentence_03.json
│       ├── ...
│       └── sentence_20.json
│
├── src/
│   ├── wlm_agent_n8n.md
│   ├── wlm_agent_langchain.py
│   └── wlm_agent_livekit.py
└── ALIGNMENT_NOTICE.MD    

---

## 🧠 What WLM‑Agent Does

WLM‑Agent converts natural language into a structured JSON output containing:

1. **structure_diagnosis**  
   - dimension  
   - subject position  
   - fold state  
   - noise sources  

2. **tension_map**  
   - boundary tensions  
   - orientation shifts  
   - collapse risks  

3. **unfolded_expression**  
   - the sentence rendered in unfolded structural language  

4. **recommended_shift**  
   - minimal structural correction  

5. **rewritten_structure_language**  
   - final structure‑language rewrite  

All outputs follow the schemas in `/schemas`.

---

## 🚀 Quickstart

### 1. Install dependencies
```bash
pip install langchain openai livekit-agents
```

### 2. Run WLM‑Agent on a sentence
```python
from src.wlm_agent_langchain import run_wlm_agent

print(run_wlm_agent("I feel responsible for everyone's emotions."))
```

### 3. Expected output
A JSON object following the schemas in `/schemas`.

### 4. Explore examples
See `/examples` for 20 input/output pairs.
