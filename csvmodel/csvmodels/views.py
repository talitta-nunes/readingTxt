from django.shortcuts import HttpResponse, render

from .forms import Form
from .models import ClientForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        print(form.as_p)

        if form.is_valid():
            nome = form.cleaned_data["file_name"]
            arquivo = form.cleaned_data["files_data"]

            ClientForm(name=nome, file=arquivo).save()

            return HttpResponse("file upload")
        else:
            return HttpResponse("error")
    else:

        context = {"form": Form()}

        return render(request, "index.html", context)


def show_file(request):
    all_data = ClientForm.objects.all()

    context = {"data": all_data}

    return render(request, "view.html", context)
