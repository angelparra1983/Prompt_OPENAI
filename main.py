import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/

The "typer" module is a Python library for creating command line (CLI) applications quickly and easily. Provides a
Simple and clear syntax for defining CLI commands and command line options in Python, allowing users to interact with scripts and programs from the command line.

The "rich" module is a Python library for enhancing the display of text in the terminal with formatting and styling features.
advanced, such as colors, bold, italics, among others.

The "rich.table" module is a Python library for creating tables in the terminal with advanced formatting and styling features, such as
colors and bold. This module is part of the "rich" library and provides a simple and easy to use solution for printing tables on the
terminal.

"""

def main():

    openai.api_key = "my-api"

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Description")
    table.add_row("exit", "Exit application")
    table.add_row("new", "Create a new conversation")

    print(table)

    # Wizard Context
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 New conversation created")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿What do you want to talk about? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿You're sure?")
        if exit:
            print("👋 ¡Bye!")
            raise typer.Abort()

        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)
