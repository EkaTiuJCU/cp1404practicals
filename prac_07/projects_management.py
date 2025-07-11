"""
File: project_management.py
This module contains the main program
Time Estimate: 2 hours
Actual Time: 2 hours
This felt like an assignment, and I rushed it. I copied functions from Assignment 1 and changed them up as well to implement classes.

"""
import csv
from datetime import datetime
from project import Project

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)dpdate project
- (Q)uit"""

import csv
from datetime import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    print(MENU)

    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    if input("Would you like to save to projects.txt? ").lower() in ['yes', 'y']:
        save_projects('projects.txt', projects)

    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # skip header
        for row in reader:
            projects.append(Project(*row))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost_estimate,
                project.completion_percentage
            ])

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()

    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for project in filtered:
        print(project)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    index = int(input("Project choice: "))
    project = projects[index]
    print(project)

    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(new_completion, new_priority)

if __name__ == '__main__':
    main()
