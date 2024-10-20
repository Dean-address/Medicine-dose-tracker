from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML
from django.urls import reverse


class DosageForm(forms.Form):
    medicine_name = forms.CharField(label="MedicineName", required=True, max_length=50)
    quantity = forms.CharField(label="Quantity", required=True, max_length=50)
    units = forms.CharField(label="Units", required=True, max_length=100)
    frequency = forms.CharField(label="Frequency", required=True, max_length=50)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = reverse("mainApp:create_dosage")
        self.helper.form_class = ""
        self.helper.layout = Layout(
            Div("medicine_name", "quantity", "units", "frequency"),
            Div(
                HTML(
                    """ <a
            href="{% url 'mainApp:logout_user' %}"
            class="w-1/2 text-center bg-red-600 text-white py-2 rounded-md hover:bg-red-500 focus:outline-none"
            >Logout</a
        >
         <a
            href="{% url 'mainApp:index' username=user  %}"
            class="w-1/2 text-center bg-blue-600 text-white py-2 rounded-md hover:bg-blue-500 focus:outline-none"
            >View Existing Data</a
        >
        """
                ),
                css_class="mt-6 flex justify-between",
            ),
            Div(
                Submit(
                    "submit",
                    "Submit",
                    css_class='w-full mt-4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"',
                ),
                css_class="max-w-full",
            ),
        )
