# import ollama


# class JarvisBrain:

#     def __init__(self):

#         self.model = "llama3"

#         self.chat_history = [
#             {
#                 "role": "system",
#                 "content": (
#                     "You are JARVIS, a personal AI assistant. "
#                     "Answer clearly and briefly."
#                 )
#             }
#         ]

#     def ask(self, text):

#         self.chat_history.append({
#             "role": "user",
#             "content": text
#         })

#         response = ollama.chat(
#             model=self.model,
#             messages=self.chat_history
#         )

#         reply = response["message"]["content"]

#         self.chat_history.append({
#             "role": "assistant",
#             "content": reply
#         })

#         return reply

import ollama


class JarvisBrain:

    def __init__(self):

        self.model = "llama3.2:3b"

        self.system_prompt = (
            "You are JARVIS, a personal AI assistant. "
            "Answer clearly, naturally and briefly. "
            "Keep normal answers under 2 sentences unless "
            "the user asks for more detail."
        )

        # Keep only a small amount of conversation memory.
        self.chat_history = []

    def ask(self, text):

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        # Keep only the last 4 messages.
        messages.extend(
            self.chat_history[-4:]
        )

        messages.append({
            "role": "user",
            "content": text
        })

        response = ollama.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": 0.3,
                "num_predict": 80,
            }
        )

        reply = response["message"]["content"].strip()

        # Save conversation memory.
        self.chat_history.append({
            "role": "user",
            "content": text
        })

        self.chat_history.append({
            "role": "assistant",
            "content": reply
        })

        # Prevent unlimited memory growth.
        self.chat_history = self.chat_history[-6:]

        return reply