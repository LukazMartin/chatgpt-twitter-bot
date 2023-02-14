import openai

class OpenAI:

    openai.api_key = "API-KEY" # Set your API key
    model_engine = "text-davinci-002" # choose one here: https://platform.openai.com/docs/models/gpt-3

    def __init__(self, trends):

        prompt = trends

        # Generate a response from the API
        completions = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=52, # a token is aprox 4 char
            n=1, # amount of completitions
            temperature=1, # between 0 and 2, determines the randomness
        )

        message = completions.choices[0].text
        return message
