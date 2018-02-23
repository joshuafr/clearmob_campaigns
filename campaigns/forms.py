from django import forms

class InputForm(forms.Form):
    total_budget = forms.FloatField(label = "Total budget: ")
    camp1_mean = forms.FloatField(label = "Campaign 1 mean: ")
    camp1_dev = forms.FloatField(label = "Campaign 1 std dev: ")

    camp2_mean = forms.FloatField(label = "Campaign 2 mean: ")
    camp2_dev = forms.FloatField(label = "Campaign 2 std dev: ")

    camp3_mean = forms.FloatField(label = "Campaign 3 mean: ")
    camp3_dev = forms.FloatField(label = "Campaign 3 std dev: ")

class OutputForm(forms.Form):
    camp1_score = forms.FloatField(label="Campaign 1 score: ", disabled=True)
    camp2_score = forms.FloatField(label="Campaign 2 score: ", disabled=True)
    camp3_score = forms.FloatField(label="Campaign 3 score: ", disabled=True)