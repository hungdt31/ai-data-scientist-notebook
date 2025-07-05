#!/usr/bin/env python3
"""
Export Flask app to static files for GitHub Pages
"""
import os
import shutil
import glob

from app import app


def export_static_site():
    """Export Flask app to static HTML files"""

    # Create output directory
    output_dir = "docs"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    os.makedirs(os.path.join(output_dir, "blog"))

    # Copy static files
    if os.path.exists("static"):
        shutil.copytree("static", os.path.join(output_dir, "static"))

    # Routes to export
    routes = [
        ("/", "index.html"),
        ("/about", "about.html"),
        ("/services", "services.html"),
        ("/contact", "contact.html"),
        ("/blog", "blog/index.html"),  # Blog list page
    ]

    # Get all markdown files to generate blog post pages
    md_files = glob.glob("posts/*.md")
    for md_file in md_files:
        # Extract slug from filename (remove .md extension)
        slug = os.path.basename(md_file)[:-3]
        routes.append((f"/blog/{slug}", f"blog/{slug}.html"))

    with app.test_client() as client:
        for route, filename in routes:
            print(f"Exporting {route} -> {filename}")

            # Get response from Flask
            response = client.get(route)

            if response.status_code == 200:
                # Create necessary subdirectories
                output_path = os.path.join(output_dir, filename)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Fix static file paths and navigation links for GitHub Pages
                html_content = response.get_data(as_text=True)
                html_content = html_content.replace("/static/", "../static/" if "/" in filename else "./static/")

                # Fix navigation links
                html_content = html_content.replace('href="/"', 'href="../index.html"' if "/" in filename else 'href="./index.html"')
                html_content = html_content.replace(
                    'href="/about"', 'href="../about.html"' if "/" in filename else 'href="./about.html"'
                )
                html_content = html_content.replace(
                    'href="/services"', 'href="../services.html"' if "/" in filename else 'href="./services.html"'
                )
                html_content = html_content.replace(
                    'href="/contact"', 'href="../contact.html"' if "/" in filename else 'href="./contact.html"'
                )
                html_content = html_content.replace(
                    'href="/blog"', 'href="../blog/index.html"' if "/" in filename else 'href="./blog/index.html"'
                )

                # Fix blog post links in blog list
                if "blog/index.html" in filename:
                    for md_file in md_files:
                        slug = os.path.basename(md_file)[:-3]
                        html_content = html_content.replace(
                            f'href="/blog/{slug}"', f'href="./{slug}.html"'
                        )
                
                # Fix "back to blog list" links in blog posts
                if "/blog/" in route and route != "/blog":
                    html_content = html_content.replace(
                        'href="/blog"', 'href="./index.html"'
                    )

                # Write to file
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(html_content)

                print(f"✅ Exported {filename}")
            else:
                print(f"❌ Error exporting {route}: {response.status_code}")

    print(f"\n🎉 Static site exported to '{output_dir}' directory")
    print("You can now deploy this to GitHub Pages!")


if __name__ == "__main__":
    export_static_site()
