# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Xử lý file ở đây
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('File đã được upload thành công!')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('uploaded_file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
