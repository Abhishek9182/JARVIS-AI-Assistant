from core.wake_word import WakeWord


print("=" * 50)
print("       JARVIS WAKE WORD TEST")
print("=" * 50)

wake = WakeWord()

while True:

    detected = wake.wait()

    if detected:

        print()
        print("SUCCESS!")
        print("Hey Jarvis detected.")
        print()

        answer = input(
            "Press ENTER to test again, "
            "or type q to quit: "
        )

        if answer.lower() == "q":
            break
