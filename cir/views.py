from django.shortcuts import render
import xlwt
from django.http import HttpResponse
# Create your views here.
from cir.models import Company_details


def post_list(request,ak):
    if request.method == "POST":
        cname = request.POST.get('name')
        cctc = request.POST.get('ctc')
        date = request.POST.get('date')
        e = request.POST.getlist('e[]')
        e1 = '-'.join(e)
        b = request.POST.getlist('b[]')
        b1 = '-'.join(b)
        u = Company_details.objects.create(comp_name=cname, comp_ctc=cctc, comp_date=date,eligibility=e1, branch=b1)
        u.save()
        template = "cir/home.html"
        return render(request,template,{})
    model = Company_details
    object_list = Company_details.objects.get(id=ak)
    print(object_list)
    context = {'object_list':object_list}
    temp = 'cir/index.html'
    return render(request,temp,context)


def export_data(request):
    response = HttpResponse(content_type='cir/home.html')
    response['Content-Disposition'] = 'attachment; filename="sheets/data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Company_details')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['comp_name', 'comp_ctc', 'comp_date', 'eligibility', 'branch']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Company_details.objects.all().values_list( 'comp_name', 'comp_ctc', 'comp_date', 'eligibility', 'branch')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



