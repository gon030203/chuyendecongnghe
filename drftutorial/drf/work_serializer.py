import os
import django
import io

# ----- Cấu hình Django -----
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf.settings")
django.setup()

# ----- Import sau khi đã setup Django -----
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# ----- Tạo dữ liệu mẫu -----
snippet1 = Snippet(code='foo = "bar"\n')
snippet1.save()

snippet2 = Snippet(code='print("hello, world")\n')
snippet2.save()

# ----- Serialize một instance -----
serializer = SnippetSerializer(snippet2)
print("Serialized instance (Python data):")
print(serializer.data)

# Render thành JSON
content = JSONRenderer().render(serializer.data)
print("\nSerialized JSON:")
print(content)

# ----- Deserialize (JSON → Python datatypes → Model) -----
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
if serializer.is_valid():
    print("\nDeserialized data (validated):")
    print(serializer.validated_data)
    obj = serializer.save()
    print(f"Saved object: {obj}")

# ----- Serialize queryset -----
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print("\nSerialized queryset:")
print(serializer.data)
