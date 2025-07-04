from flask import Flask, render_template

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
        page_title="Về chúng tôi",
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


if __name__ == "__main__":
    app.run(debug=True)
