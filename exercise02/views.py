from django.shortcuts import render
from .forms import PromotionEligibilityForm
from datetime import date

def promotion_eligibility(request):
    form = PromotionEligibilityForm()
    eligibility = None

    if request.method == 'POST':
        form = PromotionEligibilityForm(request.POST)
        if form.is_valid():
            # Extract date of joining
            date_of_joining = form.cleaned_data['date_of_joining']
            # Calculate experience
            experience = (date.today() - date_of_joining).days // 365
            # Check eligibility
            eligibility = "YES" if experience > 5 else "NO"

    return render(request, 'employees/promotion_eligibility.html', {
        'form': form,
        'eligibility': eligibility,
    })
