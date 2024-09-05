def company_users(company: str, id: str, companies_dict: dict):
    if company not in companies_dict:
        companies_dict[company] = []
    if id not in companies_dict[company]:
        companies_dict[company].append(id)

registered_companies = {}
while 1:
    staff_info = input().split(" -> ")
    if staff_info[0] == "End":
        break
    employee_company, employee_id = staff_info
    company_users(employee_company, employee_id, registered_companies)

for company_name, total_employees in registered_companies.items():
    print(f"{company_name}")
    print(*[f" -- {employee}" for employee in total_employees], sep="\n")
