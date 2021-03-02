from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MembersManage
from .forms import MemberForm

# Create your views here.
@login_required
def listMembers(request):
    person = MembersManage.objects.all()
    print(person)
    return render(request,'Members.html',{'people':person})

@login_required
def createMember(request):
    form = MemberForm(request.POST or  None)
    if form.is_valid():
        form.save()
        
    return render(request,'newMember.html', {'form':form})

@login_required
def updateMember(request, id):
    person = get_object_or_404(MembersManage, pk = id)
    form = MemberForm(request.POST or None, instance = person)
    if form.is_valid():
        form.save() 
    return render(request, 'newMember.html',{'form':form})

@login_required
def deleteMember(request, id):
    person = get_object_or_404(MembersManage, pk = id)
    form = MemberForm(request.POST or None, instance = person)
    if request.method == 'POST':
        person.delete()
    return render(request, 'deleteMember.html',{'form':form})
    
    