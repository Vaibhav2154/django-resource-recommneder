from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Interest, Resource
from .ml_model import recommend_resources
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Recommender System!")


class RecommendResourcesView(APIView):
    def post(self, request):
        # Get user interests from request
        interests = request.data.get('interests', [])
        
        # Fetch all resources
        resources = Resource.objects.all()

        # ML-based recommendations
        recommendations = recommend_resources(interests, resources)

        # Serialize recommendations
        data = [
            {
                'title': rec[0].title,
                'type': rec[0].type,
                'url': rec[0].url,
                'similarity_score': rec[1],
            }
            for rec in recommendations[:10]  # Top 10 recommendations
        ]
        return Response(data)
