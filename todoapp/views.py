from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import Myform
from django.views.generic import ListView
from .models import Task
# Create your views here.

def home(req):
    form=Myform()
    if req.method=='POST':
        temp=Myform(req.POST)
        if temp.is_valid():
            temp.save()
            return redirect("/")
    data=Task.objects.order_by("priority")
    return render(req,'home.html',{'data':form,'content':data})

# class based view starts here 
# detailview returns detail view about a specific record records
class details_view(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='content'
# update view returns raw html form  and upon success return to get_success_url()
class update_view(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='form'
    form_class=Myform
    def get_success_url(self):
        return reverse_lazy('todo:index')
# Create view used to add an objec to database and can render html form with form_class given
class add_task(CreateView):
    model=Task
    template_name='list.html'
    form_class=Myform
    def get_success_url(self):
        return reverse_lazy('todo:index')
# this is the main view or the home page for class based view
# Listview list out database entries 
# get_context_data function is overridden to add more context data to the template 
# in this we had place a form next to this listview in the html template 
class Listme(ListView):
    model=Task
    template_name='list.html'
    context_object_name='content'
    ordering=['priority']
    def get_context_data(self, **kwargs):
        form=Myform()
        context=super().get_context_data(**kwargs)
        context['data']=form
        return context
# generic deleteview to delete an entry upon confirmation redirect to index.html
class delete_me(DeleteView):
    model=Task
    template_name='task_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('todo:index')
    


def delete(req,taskid):
    chk_content=Task.objects.get(id=taskid)
    if req.method=='POST':
        pass
        chk_content.delete()
        return redirect("/")
    return render(req,'delete.html',{'task':chk_content})

def update_task(req,taskid):
    content=Task.objects.get(id=taskid)
    rawhtml=Myform(instance=content)
    if req.method=='POST':
        get_new_content=Myform(req.POST,instance=content)
        if get_new_content.is_valid():
            get_new_content.save()
            return redirect('/')
    return render(req,'edit.html',{'form':rawhtml})
# empty all records in the table
def empty(req):
    Task.objects.all().delete()
    return redirect('/list')