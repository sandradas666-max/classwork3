from django.shortcuts import render

def index(request):
    employees = [
        {'name': 'John Doe', 'job_title': 'Software Engineer','salary': 80000,'is_full_time': True},
        {'name': 'Jane Smith', 'job_title': 'Project Manager','salary': 75000,'is_full_time': True},
        {'name': 'Mike Johnson', 'job_title': 'Data Analyst','salary': 65000,'is_full_time': False},
        {'name': 'Emily Davis', 'job_title': 'UX Designer','salary': 70000,'is_full_time': False},
        {'name': 'David Wilson', 'job_title': 'DevOps Engineer','salary': 85000,'is_full_time': True},
    ]
    return render(request,'index.html',{'employees':employees})

# Create your views here.
