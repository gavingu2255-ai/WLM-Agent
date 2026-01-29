# WLM‑Agent — LiveKit Agents Integration Example

from livekit.agents import AutoAgent, llm

# Load system prompt
with open("prompts/system_prompt_wlm_agent.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

class WLMAgent(AutoAgent):
    def on_start(self):
        self.set_system_prompt(SYSTEM_PROMPT)

    async def on_user_message(self, message: str):
        """
        Processes a user message through WLM‑Agent and returns JSON output.
        """
        result = await self.llm.complete(message)
        await self.say(result.text)

if __name__ == "__main__":
    agent = WLMAgent()
    agent.run()
