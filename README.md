# ShortStory
Writes a 600 word essay from user prompts

improvements and explanations:

Environment Variable: Stores your OpenAI API key securely. You'll need to replace os.getenv("OPENAI_API_KEY") with your actual key or set it as an environment variable.
text-davinci-003: Uses the latest GPT-3 model, text-davinci-003, known for improved performance.
Token Control: max_tokens=1000 gives you control over the approximate length of the story. You can adjust this based on your preference.
Temperature: Allows you to fine-tune the creativity of the generated story. Lower values produce more focused and deterministic text, while higher values result in more diverse and unexpected outputs.
Loop and Exit: The script continuously prompts the user for input until they type "quit."
Error Handling: Consider adding try-except blocks to handle potential API errors (e.g., rate limits, invalid requests).
How to use:

Install OpenAI library: pip install openai
Set API key: Either directly in the script or as an environment variable (OPENAI_API_KEY).
Run the script: python your_script_name.py
Important Note:

OpenAI API usage is not free. Refer to OpenAI's pricing for details.
The quality of the story depends heavily on the quality of the prompt you provide. Experiment with different prompts to get the best results.
You can adjust parameters like engine, max_tokens, and temperature to tailor the story generation to your needs.
