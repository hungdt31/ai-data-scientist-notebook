#!/usr/bin/env python3
"""
CSS formatter script
"""
import re
import sys

# Configuration
TAB_WIDTH = 4  # Number of spaces for indentation


def normalize_css(css_content):
    """Normalize CSS content"""
    # Remove extra whitespace and normalize
    css_content = re.sub(r"\s+", " ", css_content.strip())

    # Add newlines after opening braces
    css_content = re.sub(r"\s*{\s*", " {\n", css_content)

    # Add newlines before closing braces
    css_content = re.sub(r"\s*}\s*", "\n}\n\n", css_content)

    # Add newlines after semicolons (but not inside parentheses)
    css_content = re.sub(r";\s*(?![^()]*\))", ";\n", css_content)

    return css_content


def format_line(line, indent_level):
    """Format a single CSS line with proper indentation"""
    line = line.strip()
    if not line:
        return "", indent_level

    # Handle comments
    if line.startswith("/*"):
        return line, indent_level

    # Handle closing braces
    if line.startswith("}"):
        new_indent = max(0, indent_level - 1)
        return " " * (TAB_WIDTH * new_indent) + line, new_indent

    # Handle selectors (lines ending with {)
    if line.endswith("{"):
        formatted_line = " " * (TAB_WIDTH * indent_level) + line
        return formatted_line, indent_level + 1

    # Handle properties and other lines
    formatted_line = " " * (TAB_WIDTH * indent_level) + line
    return formatted_line, indent_level


def clean_blank_lines(lines):
    """Remove excessive blank lines"""
    result = []
    prev_empty = False
    for line in lines:
        if line.strip() == "":
            if not prev_empty:
                result.append("")
            prev_empty = True
        else:
            result.append(line)
            prev_empty = False
    return result


def format_css(css_content):
    """Format CSS content with proper indentation"""
    # Normalize CSS
    css_content = normalize_css(css_content)

    # Split into lines and format
    lines = css_content.split("\n")
    formatted_lines = []
    indent_level = 0

    for line in lines:
        formatted_line, indent_level = format_line(line, indent_level)
        if formatted_line or formatted_line == "":
            formatted_lines.append(formatted_line)

    # Clean up extra blank lines
    result = clean_blank_lines(formatted_lines)
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
