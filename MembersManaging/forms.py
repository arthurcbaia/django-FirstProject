from .models import MembersManage
from django.forms import ModelForm


class MemberForm(ModelForm):
    class Meta:
        model = MembersManage
        fields = ['name','surname','email','phone']