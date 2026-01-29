# WLM‑Agent Examples

This folder contains 20 example inputs and outputs demonstrating how WLM‑Agent
transforms natural‑language sentences into structured WLM representations.

The examples are designed to show:

- how everyday sentences are interpreted structurally  
- how WLM‑Agent identifies dimension, fold‑state, and boundary behavior  
- how tension maps are generated  
- how natural language is rewritten into structure‑language  
- how minimal structural shifts are recommended  

The dataset includes:

- **10 everyday sentences**  
- **10 structural sentences**  
- **20 JSON outputs** following the schemas in `/schemas`  
- **two reference READMEs** (this file and the engineer version)

## Folder Structure
examples/
│
├── README.md
├── README_engineer.md
│
├── input/
│   ├── sentence_01.txt
│   ├── sentence_02.txt
│   ├── sentence_03.txt
│   ├── sentence_04.txt
│   ├── sentence_05.txt
│   ├── sentence_06.txt
│   ├── sentence_07.txt
│   ├── sentence_08.txt
│   ├── sentence_09.txt
│   ├── sentence_10.txt
│   ├── sentence_11.txt
│   ├── sentence_12.txt
│   ├── sentence_13.txt
│   ├── sentence_14.txt
│   ├── sentence_15.txt
│   ├── sentence_16.txt
│   ├── sentence_17.txt
│   ├── sentence_18.txt
│   ├── sentence_19.txt
│   └── sentence_20.txt
│
└── output/
    ├── sentence_01.json
    ├── sentence_02.json
    ├── sentence_03.json
    ├── sentence_04.json
    ├── sentence_05.json
    ├── sentence_06.json
    ├── sentence_07.json
    ├── sentence_08.json
    ├── sentence_09.json
    ├── sentence_10.json
    ├── sentence_11.json
    ├── sentence_12.json
    ├── sentence_13.json
    ├── sentence_14.json
    ├── sentence_15.json
    ├── sentence_16.json
    ├── sentence_17.json
    ├── sentence_18.json
    ├── sentence_19.json
    └── sentence_20.json

    
## Purpose

These examples serve as:

- a reference for understanding WLM‑Agent behavior  
- a demonstration of the WLM structure‑diagnosis protocol  
- a test set for validating new implementations  
- a guide for developers integrating WLM‑Agent into their systems  

For technical details, see `README_engineer.md`.
