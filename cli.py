from research_agent import ResearchAgent

def main():
    agent = ResearchAgent()
    print("💬 Welcome to Auto-Researcher CLI. Type a topic to research or 'exit' to quit.")

    while True:
        user_input = input("\n🧑 You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        elif user_input:
            print("🤖 Thinking...\n")
            results = agent.research_topic(user_input)
            summary = agent.compile_summary(user_input, results)
            print(summary)

if __name__ == "__main__":
    main()
