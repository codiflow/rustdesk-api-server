from django import forms
from api.models import UserProfile

class AddPeerForm(forms.Form):
    clientID = forms.CharField(label="Client Rustdesk ID", required=True)
    alias = forms.CharField(label="Client alias", required=True)
    tags = forms.CharField(label="Tags", required=False)
    username = forms.CharField(label="Username", required=False)
    hostname = forms.CharField(label="Hostname", required=False)
    platform = forms.CharField(label="Platform", required=False)
    ip = forms.CharField(label="IP", required=False)

class AssignPeerForm(forms.Form):
    uid = forms.ModelChoiceField(
        queryset=UserProfile.objects.all(),
        to_field_name='id',
        empty_label='Select a User',
        required=True
    )
    clientID = forms.CharField(label="Client Rustdesk ID", required=True)
    alias = forms.CharField(label="Client alias", required=True)
    tags = forms.CharField(label="Tags", required=False)
    username = forms.CharField(label="Username", required=False)
    hostname = forms.CharField(label="Hostname", required=False)
    platform = forms.CharField(label="Platform", required=False)
    ip = forms.CharField(label="IP", required=False)

class EditPeerForm(forms.Form):
    clientID = forms.CharField(label="Client Rustdesk ID", required=True)
    alias = forms.CharField(label="Client alias", required=True)
    tags = forms.CharField(label="Tags", required=False)
    username = forms.CharField(label="Username", required=False)
    hostname = forms.CharField(label="Hostname", required=False)
    platform = forms.CharField(label="Platform", required=False)
    ip = forms.CharField(label="IP", required=False)