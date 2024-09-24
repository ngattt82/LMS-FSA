from django.shortcuts import render,redirect, get_object_or_404
from .models import Certificate
from .forms import CertificateForm



def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificate_list.html', {'certificates': certificates})

def certificate_detail(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    return render(request, 'certificate_detail.html', {'certificate': certificate})

def certificate_add(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('certificate:certificate_detail', pk=certificate.pk)
    else:
        form = CertificateForm()
    return render(request, 'certificate_form.html', {'form': form})

def certificate_edit(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            certificate = form.save()
            return redirect('certificate:certificate_detail', pk=certificate.pk)
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'certificate_form.html', {'form': form})

def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificate:certificate_list')
    return render(request, 'certificate_confirm_delete.html', {'certificate': certificate})