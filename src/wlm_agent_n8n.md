# WLM‑Agent — n8n Integration Guide

This document provides a minimal and clean reference for using WLM‑Agent inside
an n8n workflow. It assumes you are using an OpenAI‑compatible LLM node.

## 1. Required Inputs

Use the following fields in your LLM node:

- **Model**: any OpenAI‑compatible model  
- **System Prompt**: contents of `prompts/system_prompt_wlm_agent.txt`  
- **User Input**: the sentence you want to analyze  
- **Response Format**: JSON  

## 2. Example Node Configuration

### System Prompt
Paste the full WLM‑Agent system prompt.

### User Prompt
{{ $json["sentence"] }}

### Output
The model will return a JSON object matching the schemas in `/schemas`.

## 3. Example Workflow Structure

- **Trigger Node**  
- **Set Node** (define `sentence`)  
- **LLM Node** (WLM‑Agent)  
- **JSON Parse Node** (optional)  
- **Webhook / Database / Further Processing**

## 4. Notes

- n8n does not enforce JSON schema validation; use a JSON Parse node if needed.  
- The examples in `/examples` can be used to test your workflow.  
