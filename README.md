<p align="center">
  <h1>WLM‑Agent</h1>
  <p>The official implementation layer of the Wujie Language Model (WLM)</p>
</p>

---

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

https://github.com/gavingu2255-ai/WLM

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
└── src/
    ├── wlm_agent_n8n.md
    ├── wlm_agent_langchain.py
    └── wlm_agent_livekit.py
    
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
