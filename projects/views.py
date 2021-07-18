from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': 'commerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'portfolio Website',
        'description': 'Project build by me'
    },
    {
        'id': '3',
        'title': 'social Website',
        'description': 'open source website'
    }
]


def projects(request):
    page = 'projects'
    number = 11
    context = {'page': page, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
