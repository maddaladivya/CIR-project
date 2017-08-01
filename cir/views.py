import datetime
from django.http import HttpResponse
from django.shortcuts import render
import xlwt

# Create your views here.

from cir.models import Company_details


def home(request):
    temp = 'cir/index.html'
    return render(request,temp,{})


def post_list(request):
    if request.method == "POST":
        cname = request.POST.get('name')
        cctc = request.POST.get('ctc')
        date = request.POST.get('date')
        e = request.POST.getlist('e[]')
        b = request.POST.getlist('b[]')
        u = Company_details.objects.create(comp_name=cname, comp_ctc=cctc, comp_date=date,eligibility=e, branch=b)
        u.save()
        template = "cir/post.html"
        return render(request,template,{})
    model = Company_details
    temp = 'cir/post.html'
    return render(request,temp,{})


def export_data(request):
    response = HttpResponse(content_type='cir/template.html')
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
    print rows
    for row in rows:
        print row
        row_num += 1
        for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_ctc(request):
    if request.method == "POST":
        response = HttpResponse(content_type='cir/home.html')
        response['Content-Disposition'] = 'attachment; filename="sheets/query.xls"'
        s = request.POST.get('search')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Company_details')
        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        ctc = Company_details.objects.values_list('comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch')
        rowno = 1
        colno = 0
        if s!=None:
            for row in ctc:
                row_num += 1
                for col_num in range(len(row)):
                    if col_num == 0:
                        if row[col_num + 1] >= int(s):
                            for i in range(0, 5, 1):
                                ws.write(rowno, colno + i, str(row[col_num + i]), font_style)
                            rowno += 1
                        else:
                            continue
                    else:
                        continue
        wb.save(response)
        return response
    temp = 'cir/search_ctc.html'
    return render(request, temp, {})


def export_date(request):
    if request.method == "POST":
        response = HttpResponse(content_type='cir/home.html')
        response['Content-Disposition'] = 'attachment; filename="sheets/query.xls"'
        fromdate = request.POST.get('Fromdate')
        todate = request.POST.get('Todate')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Company_details')
        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        ctc = Company_details.objects.values_list('comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch')
        rowno = 1
        colno = 0

        if fromdate != None:
            rowno = 1
            colno = 0
            for row in ctc:
                row_num += 1
                for col_num in range(len(row)):
                    if col_num == 0:
                        print type(row[col_num+2])
                        if str(row[col_num + 2]) >= (fromdate) and str(row[col_num + 2]) <= (todate):
                            i = 0
                            for i in range(0, 5, 1):
                                ws.write(rowno, colno + i, str(row[col_num + i]), font_style)
                            rowno += 1
        wb.save(response)
        return response
    temp = 'cir/search_date.html'
    return render(request, temp, {})

def export_branch(request):
    if request.method == "POST":
        response = HttpResponse(content_type='cir/home.html')
        response['Content-Disposition'] = 'attachment; filename="sheets/query.xls"'
        branch = request.POST.get('b[]')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Company_details')
        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        ctc = Company_details.objects.values_list('comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch')
        rowno = 1
        colno = 0
        if  branch != None:
            rowno = 1
            colno = 0
            for row in ctc:
                row_num += 1
                for col_num in range(len(row)):
                    if col_num == 0:
                        for j in row[col_num + 4]:
                            if j == branch:
                                for i in range(0, 5, 1):
                                    ws.write(rowno, colno + i, str(row[col_num + i]), font_style)
                                rowno += 1
        wb.save(response)
        return response
    temp = 'cir/search_branch.html'
    return render(request, temp, {})

def export_company(request):
    if request.method == "POST":
        response = HttpResponse(content_type='cir/home.html')
        response['Content-Disposition'] = 'attachment; filename="sheets/query.xls"'
        company = request.POST.get('search')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Company_details')
        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        ctc = Company_details.objects.values_list('comp_name', 'comp_ctc','comp_date', 'eligibility', 'branch')
        rowno = 1
        colno = 0
        if company != None:
            for row in ctc:
                row_num += 1
                for col_num in range(len(row)):
                    if col_num == 0:
                        if row[col_num] == company:
                            for i in range(0, 5, 1):
                                ws.write(rowno, colno + i, str(row[col_num + i]), font_style)
                            rowno += 1

        wb.save(response)
        return response
    temp = 'cir/search_company.html'
    return render(request, temp, {})








