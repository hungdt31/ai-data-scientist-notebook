#!/usr/bin/env python3
"""
CSS formatter script
"""
import re
import sys

# Configuration
TAB_WIDTH = 4  # Number of spaces for indentation


def format_css(css_content):
    """Format CSS content with proper indentation"""
    # Remove extra whitespace and normalize
    css_content = re.sub(r"\s+", " ", css_content.strip())

    # Add newlines after opening braces
    css_content = re.sub(r"\s*{\s*", " {\n", css_content)

    # Add newlines before closing braces
    css_content = re.sub(r"\s*}\s*", "\n}\n\n", css_content)

    # Add newlines after semicolons (but not inside parentheses)
    css_content = re.sub(r";\s*(?![^()]*\))", ";\n", css_content)

    # Split into lines and format
    lines = css_content.split("\n")
    formatted_lines = []
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line:
            if formatted_lines and formatted_lines[-1].strip():
                formatted_lines.append("")
            continue

        # Handle comments
        if line.startswith("/*"):
            formatted_lines.append(line)
            continue

        # Handle closing braces
        if line.startswith("}"):
            indent_level = max(0, indent_level - 1)
            formatted_lines.append(" " * (TAB_WIDTH * indent_level) + line)
            continue

        # Handle selectors (lines ending with {)
        if line.endswith("{"):
            formatted_lines.append(" " * (TAB_WIDTH * indent_level) + line)
            indent_level += 1
            continue

        # Handle properties
        if ":" in line and line.endswith(";"):
            formatted_lines.append(" " * (TAB_WIDTH * indent_level) + line)
            continue

        # Handle other lines
        formatted_lines.append(" " * (TAB_WIDTH * indent_level) + line)

    # Clean up extra blank lines
    result = []
    prev_empty = False
    for line in formatted_lines:
        if line.strip() == "":
            if not prev_empty:
                result.append("")
            prev_empty = True
        else:
            result.append(line)
            prev_empty = False

    return "\n".join(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: python format_css.py <css_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            css_content = f.read()

        formatted_css = format_css(css_content)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted_css)

        print(f"✅ Formatted {filename}")

    except Exception as e:
        print(f"❌ Error formatting {filename}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
