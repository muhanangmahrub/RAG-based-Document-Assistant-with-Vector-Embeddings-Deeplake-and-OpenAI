import re
import textwrap
import markdown
from IPython.display import display, HTML

def formatted_response(response: str) -> None:
    markdown_patterns = [
        r"^#+\s", r"^\*+", r"\*\*", r"_", r"\[.+\]\(.+\)", r"-\s", r"\`\`\`",
    ]
    if any(re.search(pattern, response, re.MULTILINE) for pattern in markdown_patterns):
        html_output = markdown.markdown(response)
        display(HTML(html_output))
    else:
        wrapper = textwrap.TextWrapper(width=80)
        wrapped_text = wrapper.fill(text=response)
        print("Text Response:")
        print("--------------------")
        print(wrapped_text)
        print("--------------------\n")