from flask import Flask, render_template, abort
import markdown
import os
import re
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    # Định nghĩa các biến để truyền vào template
    title = "Trang chủ AI & Data Science"
    username = "Nguyễn Văn A"
    technologies = ["Python", "Flask", "Machine Learning", "Data Science"]
    user_info = {
        "name": "Nguyễn Văn A",
        "role": "Data Scientist",
        "experience": "3 năm",
    }

    # Truyền biến vào template
    return render_template(
        "index.html",
        page_title=title,
        user=username,
        tech_list=technologies,
        user_data=user_info,
        active_page="home",  # Thêm để đánh dấu trang hiện tại
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About us",
        active_page="about",
    )


@app.route("/services")
def services():
    services_list = [
        "Phân tích dữ liệu",
        "Machine Learning",
        "Xây dựng Dashboard",
        "Tư vấn AI",
        "Đào tạo Data Science",
    ]
    return render_template(
        "services.html",
        page_title="Dịch vụ",
        services=services_list,
        active_page="services",
    )


@app.route("/contact")
def contact():
    contact_info = {
        "email": "contact@aidatascience.com",
        "phone": "+84 123 456 789",
        "address": "123 Đường ABC, Quận 1, TP.HCM",
    }
    return render_template(
        "contact.html",
        page_title="Liên hệ",
        contact=contact_info,
        active_page="contact",
    )


def parse_markdown_metadata(content):
    """Phân tích metadata từ nội dung markdown."""
    metadata = {}
    match = re.match(r'---\s+(.*?)\s+---\s+(.*)', content, re.DOTALL)
    if match:
        metadata_text = match.group(1)
        content = match.group(2)
        
        for line in metadata_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
                
    return metadata, content


@app.route("/blog")
def blog_list():
    """Hiển thị danh sách bài viết blog từ các file markdown."""
    posts = []
    
    # Lấy tất cả file markdown trong thư mục posts
    for filename in os.listdir('posts'):
        if filename.endswith('.md'):
            file_path = os.path.join('posts', filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Phân tích metadata và nội dung
            metadata, _ = parse_markdown_metadata(content)
            
            # Tạo slug từ tên file
            slug = filename[:-3]  # Bỏ phần .md
            
            posts.append({
                'slug': slug,
                'title': metadata.get('title', 'Không có tiêu đề'),
                'date': metadata.get('date', ''),
                'summary': metadata.get('summary', ''),
                'author': metadata.get('author', '')
            })
    
    # Sắp xếp bài viết theo ngày (mới nhất trước)
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    return render_template(
        "blog_list.html",
        page_title="Blog",
        posts=posts,
        active_page="blog",
    )


@app.route("/blog/<slug>")
def blog_post(slug):
    """Hiển thị bài viết blog cụ thể từ file markdown."""
    file_path = os.path.join('posts', f"{slug}.md")
    
    if not os.path.exists(file_path):
        abort(404)
        
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Phân tích metadata và nội dung
    metadata, content = parse_markdown_metadata(content)
    
    # Chuyển đổi markdown thành HTML
    html_content = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
    
    return render_template(
        "blog_post.html",
        page_title=metadata.get('title', 'Blog Post'),
        post_title=metadata.get('title', 'Không có tiêu đề'),
        post_date=metadata.get('date', ''),
        post_author=metadata.get('author', ''),
        post_content=html_content,
        active_page="blog",
    )


if __name__ == "__main__":
    app.run(debug=True)
