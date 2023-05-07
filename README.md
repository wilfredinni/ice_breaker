# Icebreaker

An example implementation of OpenAI and Langchain's ability to easily use third parties to produce internet aware outputs.

In this example, Twitter and Linkedin are used to produce a resume of a person.

## Installation

```bash
poetry install
```

Use the `.env.example` to create a new `.env` file with your own API keys and secrets.

```bash
python ice_breaker.py
```

If you asked for `Guido van Rossum` for example, you would get the following output:

```json
{
    "summary": "Guido van Rossum is a computer programmer and the creator of the Python programming language.",
    "facts": [
        "Van Rossum named Python after the British comedy group Monty Python.",
        "He was awarded the Free Software Foundation's Award for the Advancement of Free Software in 2001."
    ],
    "topics_of_interest": [
        "Programming languages",
        "Artificial intelligence"
    ],
    "ice_breaker": [
        "Have you ever attended a Monty Python show?",
        "What inspired you to create Python?"
    ]
}
```