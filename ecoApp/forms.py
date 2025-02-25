from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Div, Submit, Layout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ecoApp.models import User, Customers, Product, addressBook, Payment


class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1','password2')


class Customer_reg(forms.ModelForm):
    class Meta:
        model = Customers
        # fields = ('Name', 'Email')
        exclude = ('user','Gender','pro_pic')


class product_add_form(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('size',)

    def __init__(self, *args, **kwargs):
        super(product_add_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Product Details",
                Div('product_name', 'description', css_class="card-body"),  # Adjust fields as needed
                css_class="card mb-3"  # Adds card styling
            ),
            Fieldset(
                "Pricing and Stock Information",
                Div('price', 'MRP', 'Discount', 'QTY', css_class="card-body"),
                css_class="card mb-3"
            ),
            Fieldset(
                "Additional Information",
                Div('brand', 'Category', 'Sub_Category', css_class="card-body"),
                css_class="card mb-3"
            ),
            Submit('submit', 'Add Product', css_class='btn btn-primary')
        )


class cart_add_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image',)


class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class profile_info_form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('Name','Email','Mobile', 'Gender')
        widgets = {
            'Gender': forms.RadioSelect()
        }


class profile_detail(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('Name',)


class add_address_form(forms.ModelForm):
    class Meta:
        model = addressBook
        # fields = '__all__'
        exclude = ['user']
        widgets = {
            'address_type': forms.RadioSelect()  # Assuming you want to use RadioSelect for address type
        }


class PaymentForm(forms.ModelForm):
    payment_method = forms.ChoiceField(
        choices=Payment._meta.get_field('payment_method').choices,  # Reference choices directly from model
        widget=forms.RadioSelect,  # Optional: You can use a dropdown if preferred
        label="Payment Method"
    )
    transaction_id = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
        label="Transaction ID (auto-generated)"
    )
    amount = forms.DecimalField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        label="Total Amount"
    )

    class Meta:
        model = Payment
        fields = ['payment_method', 'transaction_id', 'amount']
        exclude = ['order', 'user', 'status', 'currency', 'payment_date', 'remarks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['amount'].initial = kwargs['instance'].amount



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['Name', 'Email', 'Mobile']  # Add other fields as needed
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.RadioSelect(),
        }
