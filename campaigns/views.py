from django.shortcuts import render
from .forms import InputForm, OutputForm
from scipy.stats import norm
import sys

def index(request):
    input_form = None
    output_form = None


    if request.GET.get('submit_button'):
        input_form = InputForm(request.GET)
        if input_form.is_valid():
            data = input_form.cleaned_data
            norm1 = norm(data["camp1_mean"], data["camp1_dev"])
            norm2 = norm(data["camp2_mean"], data["camp2_dev"])
            norm3 = norm(data["camp3_mean"], data["camp3_dev"])
            output_form = OutputForm()
            output_form.fields["camp1_score"].initial = norm1.pdf(50)
            output_form.fields["camp2_score"].initial = norm2.pdf(50)
            output_form.fields["camp3_score"].initial = norm3.pdf(50)
        else:
            print(input_form.errors, file=sys.stderr)
    else:
        input_form = InputForm()
        output_form = OutputForm()
    return render(request, 'index.html', {'input_form': input_form, 
                                            'output_form': output_form})