from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request, "index.html")

def submit_message(request):
    if request.method == "POST":
        name = request.POST.get("demo-name", "Anonymous")
        email = request.POST.get("demo-email", "No email provided")
        category = request.POST.get("demo-category", "No category")
        message = request.POST.get("demo-message", "No message")
        
        # 组织消息格式
        msg_content = f"Name: {name}\nEmail: {email}\nCategory: {category}\nMessage:\n{message}\n{'-'*40}\n"
        
        # 确保存储路径
        file_path = os.path.join(os.path.dirname(__file__), "messages.txt")
        
        # 追加写入文件
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(msg_content)

        return HttpResponse("Message received! Thank you.")

    return HttpResponse("Invalid request method.", status=400)
