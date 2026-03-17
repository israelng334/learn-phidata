from agent import agent

while True:
    user_input = input("Ask something: ")

    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)
    print("\nAgent:", response)