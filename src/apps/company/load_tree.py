import apps.company.models
from django.forms.models import model_to_dict


def generate_tree_department():

    def position_dict(department, position):
        position_list = model_to_dict(position, fields=['name', 'description', 'id'])
        employee_data = apps.company.models.Employee.objects.filter(department=department.id, position=position.id)
        position_list["employee"] = [employee_dict(employee) for employee in employee_data]
        return position_list

    def employee_dict(employee):
        return model_to_dict(employee, fields=['last_name', 'first_name', 'middle_name', 'recruitment', 'salary_size'])

    def get_tree_department(department):
        tree = model_to_dict(department, fields=['name', 'description', 'id'])
        position_data = apps.company.models.Position.objects.all()
        tree['position'] = [position_dict(department, position) for position in position_data]
        if department.children.all().exists():
            children = list()
            for child in department.children.all():
                children.append(get_tree_department(child))
            tree['children'] = children
        return tree

    final_tree = list()
    for department in apps.company.models.Department.objects.filter(parent_department__isnull=True):
        final_tree.append(get_tree_department(department))

    return final_tree
