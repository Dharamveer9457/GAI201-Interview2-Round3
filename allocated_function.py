def allocate_projects(employees, projects):
    skill_to_employees = {}

    for employee in employees:
        for skill in employee['skills']:
            if skill not in skill_to_employees:
                skill_to_employees[skill] = []
                skill_to_employees[skill].append(employee)

    available_projects = projects.copy()

    for project in projects:
        required_skills = project["required_skills"]
        for skill in required_skills:
            if skill not in skill_to_employees or not skill_to_employees[skill]:
                break
            else:
                available_projects.append(project)

    assignments = []

    for employee in employees:
        for project in available_projects:
            required_skills = project["required_skills"]
            for skill in required_skills:
                if skill not in employee["skills"]:
                    break
                else:
                    assignments.append({"employee":employee["name"], "project": project["name"]})
                    employee["current_project"] = project["name"]
                    available_projects.remove(project)
                    for skill in required_skills:
                        skill_to_employees[skill].remove(employee)

    return assignments

        