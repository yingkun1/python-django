from django.http import HttpResponse
import csv

def index(request):
    response = HttpResponse(content_type="text/csv")
    # with open("xx.csv","w") as fp:
    #     csv.writer(fp)

    writer = csv.writer(response)
    writer.writerow(['username','age'])
    writer.writerow(['zhiliao','18'])
    return response