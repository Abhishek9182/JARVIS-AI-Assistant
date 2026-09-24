from core.agent import JarvisAgent
from core.brain import JarvisBrain


def main():

    brain = JarvisBrain()

    agent = JarvisAgent(brain)

    print("=" * 50)
    print("          JARVIS AGENT TEST")
    print("=" * 50)

    while True:

        text = input("\nYou: ")

        if text.lower() in [
            "exit",
            "quit"
        ]:
            print("JARVIS: Goodbye, sir.")
            break

        reply = agent.process(text)

        print(f"\nJARVIS: {reply}")


if __name__ == "__main__":
    main()