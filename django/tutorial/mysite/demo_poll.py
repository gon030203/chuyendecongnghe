import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Choice, Question
from django.utils import timezone

# Xóa dữ liệu cũ
Question.objects.all().delete()
Choice.objects.all().delete()

# Tạo câu hỏi mới
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
print(f"Created Question: {q} (ID={q.id})")

# Đổi nội dung câu hỏi
q.question_text = "What's up?"
q.save()

# In ra tất cả câu hỏi
print("All questions:", list(Question.objects.all()))

# Tìm kiếm câu hỏi bắt đầu bằng 'What'
qs = Question.objects.filter(question_text__startswith="What")
print("Questions start with 'What':", list(qs))

# Lấy câu hỏi theo năm hiện tại
current_year = timezone.now().year
q_current = Question.objects.get(pub_date__year=current_year)
print("Question published this year:", q_current)

# Test was_published_recently()
print("Was published recently?", q_current.was_published_recently())

# Thêm các lựa chọn
q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# In tất cả choices
print("Choices for question:", list(q.choice_set.all()))

# Tìm tất cả choices theo năm
choices_this_year = Choice.objects.filter(question__pub_date__year=current_year)
print("Choices this year:", list(choices_this_year))

# Xóa một choice
c_delete = q.choice_set.filter(choice_text__startswith="Just hacking")
c_delete.delete()
print("Choices after delete:", list(q.choice_set.all()))
