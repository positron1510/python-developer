from docxtpl import DocxTemplate
import csv, json, time

data = []
start_time = 0
time_execute = 0

def docx_report():
    """
    Отчет в формате docx
    :return: None
    """
    global time_execute
    template = DocxTemplate('reports/templates/report_tpl.docx')
    template.render({'data': data})
    template.save('reports/report_files/report.docx')
    time_execute = time.time() - start_time

def csv_report():
    """
    Отчет в формате csv
    :return: None
    """""
    fieldnames = ['model', 'volume', 'price']
    with open('reports/report_files/report.csv', 'w') as f:
        writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(data)):
            writer.writerow(data[i])
        writer.writerow({'model': '', 'volume' :'', 'price': ''})
        writer.writerow({'model': 'Время генерации отчета:', 'volume' :'', 'price': time_execute})

def json_report():
    """
    Отчет в формате json
    :return: None
    """""
    data.append({'Время генерации отчета': str(time_execute)})
    with open('reports/report_files/report.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == '__main__':
    print('This is report module')
else:
    # Получаем исходные данные по тачкам для дальнейшей работы
    start_time = time.time()
    with open('reports/../data.txt') as f:
        data = [dict(zip(['model', 'volume', 'price'], s.split())) for s in f]
