import json
import csv


with open('people_db.json') as jsonfile:
    json_data = json.load(jsonfile)
    json_keys = [*json_data[0].keys()]
    if not all((json_keys.__contains__('company_name'), json_keys.__contains__('phone'), json_keys.__contains__('job_title'))):
        print('JSON file has invalid format, please choose another file')
        exit()
    with open('people_db.csv', 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=json_keys)
        csv_writer.writeheader()
        for el in json_data:
            if any((el['company_name'] is not None,
                el['phone'] is None,
                not isinstance(el['job_title'], str),
                el['job_title'].find('Software') == -1)):
                continue
            csv_writer.writerow(el)