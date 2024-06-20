import openai
import os

# Get your API key from your OpenAI account
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your API key as an environment variable

def generate_story(prompt):
    """Generates a story using OpenAI's GPT model based on the given prompt."""

    response = openai.Completion.create(
        engine="text-davinci-003", # Or another suitable model like 'text-davinci-002' 
        prompt=prompt,
        max_tokens=1000,  # Adjust for desired story length
        n=1,
        stop=None,
        temperature=0.7,  # Adjust for creativity (0.2 for conservative, 0.8 for adventurous)
    )

    story = response.choices[0].text.strip()
    return story

def main():
    """Gets user prompts and generates a story."""

    while True:
        user_prompt = input("Enter your story prompt (or type 'quit' to exit): ")
        if user_prompt.lower() == 'quit':
            break

        story = generate_story(user_prompt)
        print("\nHere's your story:\n")
        print(story)

if __name__ == "__main__":
    main()
