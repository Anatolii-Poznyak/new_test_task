from django.core.management.base import BaseCommand

import json

positions_list = [
    "CEO",
    "Team Lead",
    "Employee",
    "Intern",
    "Data Analyst",
    "Mechanical engineer",
    "HR",
    "UI Developer",
    "UI/UX ",
    "Backend Architect",
    "Frontend Architect",
    "Software Tester",
    "QA",
]


class Command(BaseCommand):
    help = "Create json file with fake positions for future load in DB"

    @staticmethod
    def print_success_message():
        print(f"\033[92m  Creation of positions was successful!\033[0m")

    @staticmethod
    def create_positions(data):
        for i, position_name in enumerate(positions_list):
            position_record = {
                "model": "employees_structure.position",
                "pk": i + 1,
                "fields": {
                    "name": position_name,
                }
            }
            data.append(position_record)
        return data

    @staticmethod
    def write_to_json(data):
        with open("/app/position_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4, separators=(",", ": "))

    def handle(self, *args, **options):
        data = []
        data = self.create_positions(data)
        self.write_to_json(data)
        self.print_success_message()
