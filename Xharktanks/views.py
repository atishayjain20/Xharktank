from django.http import HttpResponse,JsonResponse
from Xharktanks.models import Entre, Investors
from rest_framework.parsers import JSONParser
from django.core import serializers
import io
from rest_framework import viewsets
from .serializers import EntreSerializer, InvestorsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.

#Endpoint to post a pitch to the backend 
#Endpoint to fetch the all the pitches in the reverse chronological order ( i.e. last created one first ) from the backend
class InvestorsViewSet(viewsets.ViewSet):
    serializer_class = EntreSerializer

#Function to fetch the all the pitches in the reverse chronological order ( i.e. last created one first ) from the backend
    
    def list(self, request):
        queryset = Entre.objects.all()
        serializer = EntreSerializer(queryset, many=True)
        return Response(serializer.data)

#Function to post a pitch to the backend

    def create(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        if not ('entrepreneur' in data):
            return HttpResponse('Invalid Request Body',status=400)
        if not ('pitchTitle' in data):
            return HttpResponse('Invalid Request Body',status=400)
        if not ('pitchIdea' in data):
            return HttpResponse('Invalid Request Body',status=400)
        if not ('equity' in data):
            return HttpResponse('Invalid Request Body',status=400)
        if not ('askAmount' in data):
            return HttpResponse('Invalid Request Body',status=400)
        Name=data.get('entrepreneur')
        Title=data.get('pitchTitle')
        Idea=data.get('pitchIdea')
        Amount=data.get('askAmount')
        Equity=data.get('equity')
        enterpreneur=Entre(entrepreneur=Name,pitchTitle=Title,pitchIdea=Idea,askAmount=Amount,equity=Equity)
        enterpreneur.save()
        data={
            'id':str(enterpreneur.id)
        }
        return JsonResponse(data,status=201)


# Endpoint to specify a particular id (identifying the pitch) to fetch a single Pitch.

def get_query(request,m):
    if request.method=='GET':
        queryset = Entre.objects.filter(id=m)
        investor_names = []
        for category in queryset[0].offers.all():
            investor_names.append(category)
        print(queryset[0].offers.all())
        data={
                'id':str(queryset[0].id),
                'entrepreneur':str(queryset[0].entrepreneur),
                'pitchTitle':str(queryset[0].pitchTitle),
                'pitchIdea':str(queryset[0].pitchIdea),
                'askAmount':float(queryset[0].askAmount),
                'equity':float(queryset[0].equity),
                'offers':investor_names
            }
        return JsonResponse(data)



#Endpoint to make a counter offer for a pitch to the backend

@csrf_exempt
def makeOffer(request,id):
    if request.method=='POST':
        if not Entre.objects.filter(id=id).first():
            return HttpResponse("Pitch Not Found",status=404)
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        Name=data.get('investor')
        Amount=data.get('amount')
        Equity=data.get('equity')
        Comment=data.get('comment')
        user=Investors.objects.create(investor=Name,amount=Amount,equity=Equity,comment=Comment)
        user.save()
        invest=Entre.objects.get(id=id)
        invest.offers.add(user)
        data={
            'id':str(user.id)
        }
        return JsonResponse(data,status=201)








# class InvestorsView(viewsets.ModelViewSet):
#     serializer_class=EntreSerializer

#     def get_queryset(self):
#         obj_id=self.kwargs['m']
#         print(obj_id)
#         print(Entre.objects.filter(id=obj_id))
#         if len(Entre.objects.filter(id=obj_id))==0:
#             print("Hello")
#             return HttpResponse('Pitch Not Found',status=404)
#         else:
#             queryset = Entre.objects.filter(id=obj_id)
#             # queryset=list(queryset)
#             print(type(queryset))
#             print(queryset)
#             return queryset