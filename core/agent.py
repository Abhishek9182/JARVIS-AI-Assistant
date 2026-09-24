# class JarvisAgent:

#     def __init__(self, brain):

#         self.brain = brain

#     def process(self, text):
#         action_reply = execute_action(text)

#         if action_reply:
#             return action_reply

#         wiki_reply = wikipedia_search(text)

#         if wiki_reply:
#             return wiki_reply

#         search_reply = web_search(text)

#         if search_reply:
#             return search_reply

#         return self.brain.ask(text)


#         # print("AGENT:", text)

#         # try:

#         #     response = self.brain.ask(text)

#         #     return response

#         # except Exception as e:

#         #     print("Agent error:", e)

#         #     return (
#         #         "I am sorry, sir. "
#         #         "I was unable to process that request."
#         #     )

    

# import wikipedia


# def wikipedia_search(text):

#     text = text.lower()

#     if not (
#         text.startswith("what is")
#         or text.startswith("who is")
#         or text.startswith("define")
#     ):
#         return None

#     search_term = (
#         text
#         .replace("what is", "")
#         .replace("who is", "")
#         .replace("define", "")
#         .strip()
#     )

#     if not search_term:
#         return None

#     try:

#         summary = wikipedia.summary(
#             search_term,
#             sentences=2,
#             auto_suggest=True
#         )

#         return summary

#     except Exception:

#         return None

# from duckduckgo_search import DDGS


# def web_search(text):

#     text = text.lower()

#     if not any(
#         word in text
#         for word in [
#             "search",
#             "latest",
#             "news",
#             "weather"
#         ]
#     ):
#         return None

#     try:

#         results = DDGS().text(
#             text,
#             max_results=3
#         )

#         if not results:
#             return None

#         response = "Here are the top results: "

#         for i, result in enumerate(
#             results[:3],
#             1
#         ):

#             response += (
#                 f"{i}. "
#                 f"{result['title']}. "
#             )

#         return response

#     except Exception as e:

#         print("Search error:", e)

#         return None

import wikipedia

from duckduckgo_search import DDGS

from core.actions import execute_action


class JarvisAgent:

    def __init__(self, brain):

        self.brain = brain

    def process(self, text):

        print(f"AGENT INPUT: {text}")

        # --------------------------------
        # TOOL 1: LOCAL PC ACTION
        # --------------------------------

        action_reply = execute_action(text)

        if action_reply:

            print("TOOL: PC ACTION")

            return action_reply

        # --------------------------------
        # TOOL 2: WIKIPEDIA
        # --------------------------------

        wiki_reply = wikipedia_search(text)

        if wiki_reply:

            print("TOOL: WIKIPEDIA")

            return wiki_reply

        # --------------------------------
        # TOOL 3: WEB SEARCH
        # --------------------------------

        search_reply = web_search(text)

        if search_reply:

            print("TOOL: WEB SEARCH")

            return search_reply

        # --------------------------------
        # TOOL 4: OLLAMA AI BRAIN
        # --------------------------------

        print("TOOL: OLLAMA")

        try:

            return self.brain.ask(text)

        except Exception as e:

            print("Agent error:", e)

            return (
                "I am sorry, sir. "
                "I was unable to process that request."
            )


# ==================================================
# WIKIPEDIA SEARCH
# ==================================================

def wikipedia_search(text):

    text = text.lower().strip()

    if not (
        text.startswith("what is")
        or text.startswith("who is")
        or text.startswith("define")
    ):

        return None

    search_term = (
        text
        .replace("what is", "", 1)
        .replace("who is", "", 1)
        .replace("define", "", 1)
        .strip()
    )

    if not search_term:

        return None

    try:

        summary = wikipedia.summary(
            search_term,
            sentences=2,
            auto_suggest=True
        )

        return (
            "According to Wikipedia, "
            + summary
        )

    except Exception as e:

        print("Wikipedia error:", e)

        return None


# ==================================================
# WEB SEARCH
# ==================================================

def web_search(text):

    text = text.lower().strip()

    search_keywords = [
        "search",
        "latest",
        "news",
        "weather"
    ]

    if not any(
        keyword in text
        for keyword in search_keywords
    ):

        return None

    try:

        results = DDGS().text(
            text,
            max_results=3
        )

        if not results:

            return None

        response = (
            "Here are the top results: "
        )

        for i, result in enumerate(
            results[:3],
            start=1
        ):

            title = result.get(
                "title",
                "Unknown result"
            )

            response += (
                f"{i}. {title}. "
            )

        return response

    except Exception as e:

        print(
            "Search error:",
            e
        )

        return None