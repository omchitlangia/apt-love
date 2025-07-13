from llama_cpp import Llama
import os
import random

MODEL_PATH = os.path.join("models", "tinyllama.gguf")
llm = Llama(model_path=MODEL_PATH, n_ctx=512, verbose=False)

def ai_reply(user_msg, personality, interests):
    interest_text = ", ".join(interests)

    # Priming examples to anchor tone
    priming = (
        f"You are {personality}, a chaotic Linux terminal flirt.\n"
        f"You love: {interest_text}.\n"
        "Crush: hey\n"
        "You: yo 😏\n"
        "Crush: how are you\n"
        "You: busy crashing the kernel of my heart 💘\n"
        "Crush: let's code\n"
        "You: only if we pair-program in bed 😈\n"
        f"Crush: {user_msg.strip()}\n"
        "You:"
    )

    # Get model response
    response = llm(priming, max_tokens=60, stop=["\n", "</s>"])
    raw = response["choices"][0]["text"].strip()
    cleaned = raw.split("\n")[0].strip()

    # Filter weird AI/model mentions or off-tone lines
    unreal_flags = ["i am", "i’m an ai", "as an ai", "i'm a model", "you are a good person", "sure, it's great"]
    for flag in unreal_flags:
        if flag in cleaned.lower():
            cleaned = random.choice([
                "you’re crashing my emotional kernel rn 💻",
                "i was just editing my config… wanna join?",
                "i’ll sudo you into my heart anytime 😈",
                "lol okay but only if you bring snacks 🍜"
            ])
            break

    # Add emoji if it’s missing
    emojis = ["😏", "💻", "💕", "🔥", "👀", "😉", "😈", "🖤"]
    if not cleaned.endswith(tuple(emojis)):
        cleaned += " " + random.choice(emojis)

    return cleaned
