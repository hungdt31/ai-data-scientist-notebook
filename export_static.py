#!/usr/bin/env python3
"""
Export Flask app to static files for GitHub Pages
"""
import os
import shutil
from urllib.parse import urljoin

from app import app


def export_static_site():
    """Export Flask app to static HTML files"""

    # Create output directory
    output_dir = "docs"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Copy static files
    if os.path.exists("static"):
        shutil.copytree("static", os.path.join(output_dir, "static"))

    # Routes to export
    routes = [
        ("/", "index.html"),
        ("/about", "about.html"),
        ("/services", "services.html"),
        ("/contact", "contact.html"),
    ]

    with app.test_client() as client:
        for route, filename in routes:
            print(f"Exporting {route} -> {filename}")

            # Get response from Flask
            response = client.get(route)

            if response.status_code == 200:
                # Fix static file paths and navigation links for GitHub Pages
                html_content = response.get_data(as_text=True)
                html_content = html_content.replace("/static/", "./static/")

                # Fix navigation links
                html_content = html_content.replace('href="/"', 'href="./index.html"')
                html_content = html_content.replace(
                    'href="/about"', 'href="./about.html"'
                )
                html_content = html_content.replace(
                    'href="/services"', 'href="./services.html"'
                )
                html_content = html_content.replace(
                    'href="/contact"', 'href="./contact.html"'
                )

                # Write to file
                with open(
                    os.path.join(output_dir, filename), "w", encoding="utf-8"
                ) as f:
                    f.write(html_content)

                print(f"✅ Exported {filename}")
            else:
                print(f"❌ Error exporting {route}: {response.status_code}")

    print(f"\n🎉 Static site exported to '{output_dir}' directory")
    print("You can now deploy this to GitHub Pages!")


if __name__ == "__main__":
    export_static_site()
