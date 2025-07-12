from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "tinyllama.gguf")
llm = Llama(model_path=MODEL_PATH, n_ctx=512, verbose=False)

def ai_reply(user_msg, personality, interests):
    system_prompt = (
        f"You are {personality}, chatting on a fake Linux dating terminal. "
        f"Your interests: {', '.join(interests)}. "
        "Respond with a fun, short, and casual message. Stay in character. No narrator talk. No backstory. Be human, weird, or funny."
    )

    prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_msg}\n<|assistant|>\n"

    response = llm(prompt, max_tokens=60, stop=["<|user|>", "<|end|>"])

    # Clean up junk tokens
    text = response["choices"][0]["text"].strip()
    cleaned = (
        text.replace("<|user|>", "")
            .replace("<|assistant|>", "")
            .replace("<|system|>", "")
            .replace("</s>", "")
            .strip()
    )

    # Optional: truncate excessive rambling
    cleaned = cleaned.split("\n")[0].strip()  # use only the first line

    return cleaned
