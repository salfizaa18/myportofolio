from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm       


def show_main(request):
    context = {
        "name": "Salwa Hafiza Aqila",
        "npm": "2506624392",
        "study_program": "S1 Information Systems",
        "bio": (
            "Hi! I’m Salwa, an Information Systems student at Universitas Indonesia who loves trying new things and taking on new challenges. I’m passionate about growing through every experience, meeting new people, and continuously improving myself along the way."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salwa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Salwa",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Salwa",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_education_json(request):
    education = Education.objects.all()
    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def show_education(request):
    json_response = get_education_json(request)
    education_entries = serializers.deserialize("json", json_response.content.decode("utf-8"))
    education_list = [entry.object for entry in education_entries]
    context = {"name": "Salwa", "education_list": education_list}
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")
    context = {"name": "Salwa", "form": form, "form_title": "Tambah Pendidikan"}
    return render(request, "education_form.html", context)

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")
    context = {"name": "Salwa", "form": form, "form_title": "Edit Pendidikan"}
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")