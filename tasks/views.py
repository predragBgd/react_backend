from tasks.models import Task
from django.http import JsonResponse
from tasks.serializers import TaskSerializer

def tasks(request):
    data = Task.objects.all()
    serializer = TaskSerializer(data, many=True)
    return JsonResponse({'tasks': serializer.data})