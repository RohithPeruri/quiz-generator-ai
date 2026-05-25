import time
import msvcrt

score = 0
questions = []

# Load questions from file
with open("questions.txt", "r") as file:

    for line in file:

        data = line.strip().split("|")

        if len(data) == 2:
            question = data[0]
            answer = data[1].lower()

            questions.append((question, answer))


print("===================================")
print(" Welcome to AI Quiz Generator ")
print("===================================")


# Timed Input Function
def timed_input(question, timeout=30):

    print("\n" + question)
    print("Your Answer: ", end="", flush=True)

    answer = ""
    start_time = time.time()

    while True:

        elapsed = time.time() - start_time
        remaining = int(timeout - elapsed)

        print(f"\rTime Left: {remaining:2d} sec | Your Answer: {answer}", end="", flush=True)

        if remaining <= 0:
            print("\nTime's Up!")
            return None

        if msvcrt.kbhit():

            char = msvcrt.getwche()

            if char == '\r':
                print()
                return answer.strip().lower()

            elif char == '\b':
                answer = answer[:-1]

            else:
                answer += char

        time.sleep(0.1)


# Quiz Loop
for question, correct_answer in questions:

    user_answer = timed_input(question, 30)

    if user_answer is None:
        continue

    if user_answer == correct_answer:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer:", correct_answer)


# Final Score
print("\n===================================")
print(f"Final Score: {score}/{len(questions)}")
print("===================================")

# Save Score
with open("scores.txt", "a") as file:
    file.write(f"Score: {score}/{len(questions)}\n")

print("Score saved successfully!")