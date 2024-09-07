from django.shortcuts import render, redirect
from .forms import InquireForm

def inquire_view(request):
    if request.method == 'POST':
        form = InquireForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid form to the database
            return redirect('home')  # Redirect to a success page
    else:
        form = InquireForm()

    return render(request, 'contact/inquire.html', {'form': form})
