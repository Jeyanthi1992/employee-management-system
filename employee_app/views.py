from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html")

@login_required   
def about(request):
    return render(request, "about.html")

@login_required
def service(request):
    return render(request, "service.html")


@login_required
def employee_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
        else:
            print(form.errors)
    else:
        form = EmployeeForm()

    return render(request, "employee_form.html", {"form": form})


@login_required
def employeeedit(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employee_form.html", {"form": form})


@login_required
def employeedelete(request, id):

    employee = get_object_or_404(Employee, id=id)

    employee.delete()

    return redirect("employee_list")


@login_required
def employee_list(request):

    employees = Employee.objects.all()

    # Search by Name
    search = request.GET.get("search")
    if search:
        employees = employees.filter(name__icontains=search)

    # Search by Department
    department_search = request.GET.get("department_search")
    if department_search:
        employees = employees.filter(department__icontains=department_search)

    # Search by Employee ID
    id_search = request.GET.get("id_search")
    if id_search:
        employees = employees.filter(id=id_search)

    return render(request, "employee_list.html", {
        "employees": employees
    })

@login_required
def singleemployee(request, id):

    employee = get_object_or_404(Employee, id=id)

    return render(request, "single_employee.html", {"employee": employee})

@login_required
def dashboard(request):

    total_employees = Employee.objects.count()

    return render(request, "dashboard.html", {
        "total_employees": total_employees
    })
