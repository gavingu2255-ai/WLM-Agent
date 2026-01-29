# WLM‑Agent Examples — Engineering Reference

This document provides a technical overview of the example dataset and how it
should be used when implementing or validating WLM‑Agent.

## Purpose of This Dataset

The examples in this folder are intended to:

1. Validate that an implementation produces schema‑compliant output  
2. Provide regression tests for future model updates  
3. Demonstrate correct application of the WLM structure‑diagnosis protocol  
4. Serve as a reference for backend integrations (OpenAI, Anthropic, Grok, LangChain, n8n, LiveKit)

## Input Format

Each input file in `/input` contains a single English sentence.

There are two categories:

- **Everyday sentences (1–10)**  
  Natural expressions containing implicit structural patterns.

- **Structural sentences (11–20)**  
  Explicit statements describing structural behavior.

All inputs are plain text with no metadata.

## Output Format

Each output file in `/output` is a JSON object with the following fields:

- `structure_diagnosis`
  - `dimension`: `"2D" | "3D" | "4D"`
  - `subject_position`: `"foregrounded" | "collapsed" | "transparent"`
  - `fold_state`: `"folded" | "unfolded" | "multi-layer"`
  - `noise_sources`: `string[]`

- `tension_map`:  
  Array of tension objects following `tension_map_schema.json`

- `unfolded_expression`:  
  Structural rendering of the input sentence

- `recommended_shift`:  
  Minimal structural correction

- `rewritten_structure_language`:  
  Final structure‑language rewrite

All outputs strictly follow the schemas in `/schemas`.

## Validation

To validate an implementation:

1. Run each input sentence through your WLM‑Agent backend  
2. Compare the output JSON to the reference output  
3. Ensure:
   - all required fields exist  
   - no additional fields are added  
   - values match the expected types  
   - tension objects follow the tension map schema  

This dataset can be used with:

- JSON Schema validators  
- automated test suites  
- CI pipelines  
- backend comparison tools  

## Notes for Developers

- The examples are deterministic and should not be modified.  
- They represent the canonical behavior of WLM‑Agent v1.0.  
- Future versions may include additional test sets (multi‑sentence, paragraphs, dialogues).  
