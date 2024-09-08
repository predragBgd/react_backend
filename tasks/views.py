from tasks.models import Task
from django.http import JsonResponse, Http404
from tasks.serializers import TaskSerializer

def tasks(request):
    data = Task.objects.all()
    serializer = TaskSerializer(data, many=True)
    return JsonResponse({'tasks': serializer.data})

def task(request,id):
    try:
       data = Task.objects.get(pk=id)
    except Task.DoesNotExist:
       raise Http404('Task does not exist')    
    serializer = TaskSerializer(data)
    return JsonResponse({'task': serializer.data})