import os
import datetime
from django.utils import timezone
from django.test import Client
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from polls.models import Question

# 1. Tạo một Question với pub_date 30 ngày trong tương lai
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
print("Was published recently? ->", future_question.was_published_recently())

# 2. Tạo client test
client = Client()

# 3. Gửi request tới "/"
response = client.get("/")
print("\nGET / => status_code:", response.status_code)

# 4. Gửi request tới "/polls/"
url = reverse("polls:index")
response = client.get(url)
print("\nGET", url, "=> status_code:", response.status_code)

# In nội dung HTML
print("Response content:\n", response.content.decode())

# 5. In danh sách câu hỏi mới nhất nếu có
if response.context and "latest_question_list" in response.context:
    latest = response.context["latest_question_list"]
    print("\nLatest question list in context:")
    for q in latest:
        print("-", q)
else:
    print("\nNo 'latest_question_list' in context.")
