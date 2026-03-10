from django.shortcuts import render, redirect
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra
from django.core.files.storage import FileSystemStorage

def sammelan_37_mumbai_maharashtra_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        photo = request.FILES.get('photo')
        instance = Sammelan37MumbaiMaharashtra()
        for field in Sammelan37MumbaiMaharashtra._meta.fields:
            fname = field.name
            if fname == 'photo' and photo:
                instance.photo = photo
            elif fname in data:
                setattr(instance, fname, data.get(fname))
        instance.save()
        return redirect('37th_sammelan_mumbai_maharashtra_success')
    return render(request, 'biodata/37_sammelan_mumbai_maharashtra.html')

def sammelan_37_mumbai_maharashtra_success(request):
    return render(request, 'biodata/37_sammelan_success.html')
