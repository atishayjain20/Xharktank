from rest_framework  import serializers
from .models import Entre,Investors


# For serializing the data and to convert the Python Objects in Json.

class InvestorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Investors
        fields=['id','investor','amount','equity','comment']

class EntreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entre
        fields=('id','entrepreneur','pitchTitle','pitchIdea','askAmount','equity','offers')
        depth=1


