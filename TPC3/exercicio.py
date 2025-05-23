import re


patterns = {
    re.compile("^\\#[^#].*$"): ("<h1>", "</h1>"),
    re.compile("^\\#{2}[^#].*$"): ("<h2>", "</h2>"),
    re.compile("^\\#{3}[^#].*$"): ("<h3>", "</h3>"),
    re.compile("^\\*{2}[^\\*].*\\*{2}$"): ("<b>", "</b>"),
    re.compile("^\\*[^\\*].*\\*$"): ("<i>", "</i>"),
    re.compile("^>.*$"): ("<blockquote>", "</blockquote>"),
    re.compile("^\\d\\..*$"): ("<ol><li>", "</li></ol>"),
    re.compile("^-[^-].*$"): ("<ul><li>", "</li></ul>"),
    re.compile("^`[^`].*[^`]`$"): ("<code>", "</code>"),
    re.compile("^\\[\\w*\\]\\([\\w\\:/.]*\\)$"): ("<a href=\"", "\">link</a>"),
    re.compile("^!\\[[^\\]]*\\]\\(\\.{2}/[^\\)]*\\)$"): ("<img src=\"", "\" alt=\"image\"/>"),
}

def parse_md():
    with(open("markdown.md", "r")) as file:
        lines = file.readlines()
    html = ""
    for line in lines:
        for pattern, (open_tag, close_tag) in patterns.items():
            match = pattern.match(line)
            if match:
                html += f"\t{open_tag}{line.strip()}{close_tag}\n"
                break
    return html






html = """
<!DOCTYPE html>
<html>
"""
html += parse_md()
html += """
</html>
"""


with(open("index.html", "w")) as file:
    file.write(html) 