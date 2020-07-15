import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from register.models import User


@csrf_exempt
def user_list(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        search_query = json_data.get('query', '')
        if search_query == '':
            return JsonResponse({'users': []})
        users = User.objects.filter(username__icontains=search_query).exclude(id=request.user.id)

        result = []
        for user in users:
            result.append({
                'id': user.id,
                'username': user.username
            })

        data = {
            'users': result
        }
        return JsonResponse(data)
