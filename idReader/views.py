from django.shortcuts import render
from django.http import JsonResponse
import os, shutil
from math import ceil
from idReader import models

from idcardReader_django import settings

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import Frame, PageTemplate, SimpleDocTemplate, Paragraph, Image, Table, TableStyle


def paginator(obj, page='1', limit='10'):
    return len(obj), ceil(len(obj) / int(limit)), list(obj)[
                                                  (int(page) * int(limit)) - int(limit):int(page) * int(limit)], int(
        page), int(limit)


def index_bk(request):
    if request.is_ajax():
        del_id = request.GET.get('del_id')
        if del_id:
            try:
                models.Visitors.objects.get(id=del_id).delete()
                ret = {'status': 1}
                return JsonResponse(ret)
            except Exception as e:
                return render(request, 'id_reader/template/tips/showMeError.html', {'error': e})
        else:
            return render(request, 'id_reader/template/tips/showMeError.html', {'error': '未传入删除记录参数'})
    elif request.method == 'POST':
        modify_id = request.GET.get('modify_id')
        visitor = request.POST.get('visitor')
        gender = request.POST.get('gender')
        id_no = request.POST.get('id_no')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        temp = request.POST.get('temp')
        visitee = request.POST.get('visitee')
        try:
            if modify_id:
                models.Visitors.objects.filter(id=modify_id).update(visitor=visitor, gender=1 if visitor == '男' else 0,
                                                                    id_no=id_no, address=address, phone=phone,
                                                                    temp=temp,
                                                                    visitee=visitee)
            else:
                models.Visitors.objects.create(visitor=visitor, gender=1 if gender == '男' else 0, id_no=id_no,
                                               address=address, phone=phone, temp=temp, visitee=visitee)
            order = models.Visitors.objects.all().order_by('-create_time')
            total, max_page, order, page, limit = paginator(order)
            msg = True
            
            if os.path.exists(r'd:\wid\photo.jpg'):
                shutil.copyfile(r'd:\wid\photo.jpg',
                                'C:\\Users\\mxyzptlk\\PycharmProjects\\idcardReader_django\\static\\img\\' + id_no + '.jpg')
                os.remove(r'd:\wid\photo.jpg')
            return render(request, 'id_reader/id_reader.html', locals())
        except Exception as e:
            return render(request, 'id_reader/template/tips/showMeError.html', {'error': e})
    else:
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        order = models.Visitors.objects.all().order_by('-create_time')
        if page and limit:
            total, max_page, order, page, limit = paginator(order, page, limit)
            return render(request, 'id_reader/id_reader.html', locals())
        else:
            total, max_page, order, page, limit = paginator(order)
            return render(request, 'id_reader/id_reader.html', locals())


font_path = os.path.join(settings.MEDIA_ROOT, "report_pdfs", 'syht.ttf')
pdfmetrics.registerFont(TTFont('syht', font_path))


def generate_report(identifier):
    # pdf_path = os.path.join(settings.MEDIA_ROOT, "report_pdfs", f'{identifier}.pdf')
    pdf_path = os.path.join(os.path.expanduser("~"), 'Desktop', f'{identifier}.pdf')
    pdf_report = []
    stylesheet = getSampleStyleSheet()
    normal_style = stylesheet['Normal']
    
    rpt_title = '<para autoLeading="off" fontSize=20 align=center><b><font face="syht">省外返（来）阜人员信息登记表</font></b><br/></para>'
    pdf_report.append(Paragraph(rpt_title, normal_style))
    pdf_report.append(Paragraph(' \n', normal_style))
    sub_title = f'<para autoLeading="off" fontSize=8 align=right><b><font face="syht">标本号：{identifier}</font></b><br/></para>'
    pdf_report.append(Paragraph(sub_title, normal_style))
    
    order = models.Visitors.objects.filter(bk1=identifier)
    component_data = [['序号', '姓名', '性别', '身份证号', '户籍地址', '手机号', '返（来）阜前所在地（市区街道）', '目的地', '是否中高'+'\n风险地区', '车次/航班']]
    for i in range(len(order)):
        component_data.append(
            [i + 1, order[i].visitor, '男' if order[i].gender else '女', order[i].id_no, order[i].address[0:13] + '\n' + order[i].address[13:],
             order[i].phone, order[i].addr_b4[0:13] + '\n' + order[i].addr_b4[13:], order[i].desti_addr[0:13] + '\n' + order[i].desti_addr[13:],
             '是' if order[i].is_danger else '否', order[i].train_no])
    
    # 创建表格对象，并设定各列宽度
    component_table = Table(component_data, colWidths=[30, 50, 25, 110, 150, 70, 150, 150, 40, 50])
    # 添加表格样式
    component_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'syht'),  # 字体
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # 字体大小
        ('ALIGN', (0, 0), (11, 0), 'CENTER'),  # 表头对齐
        ('LINEBEFORE', (0, 0), (0, -1), 0.1, colors.black),  # 设置表格左边线颜色，线宽
        ('TEXTCOLOR', (0, 1), (-2, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为，线宽
    ]))
    pdf_report.append(component_table)
    
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=1.05 * inch, rightMargin=1.05 * inch)
    landscape_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.height, doc.width, id='landscape_frame ')
    doc.addPageTemplates([PageTemplate(id='landscape', frames=landscape_frame, pagesize=landscape(A4)), ])
    
    doc.build(pdf_report)


def check_bbh():
    last_bbh = models.Visitors.objects.filter(bk1__isnull=False).last()
    if last_bbh:
        bbh_last = last_bbh.bk1
        bbh_count = models.Visitors.objects.filter(bk1=bbh_last).count()
        if bbh_count < 10:
            bbh = bbh_last
        else:
            try:
                pdf_path = os.path.join(settings.MEDIA_ROOT, "report_pdfs", f'{bbh_last}.pdf')
                if not os.path.exists(pdf_path):
                    generate_report(bbh_last)
            except PermissionError:
                pass
            bbh = 'B1-' + str(int(bbh_last.split('-')[1]) + 1)
    else:
        bbh = 'B1-1'
    return bbh


def index(request):  # todo 前端页面id_reader2有个bug：中高风险，即第二个下拉选择无法通过jQuery修改变更(因为选择器与性别下拉选择相同)
    if request.is_ajax():
        del_id = request.GET.get('del_id')
        if del_id:
            try:
                models.Visitors.objects.get(id=del_id).delete()
                ret = {'status': 1}
                return JsonResponse(ret)
            except Exception as e:
                return render(request, 'id_reader/template/tips/showMeError.html', {'error': e})
        else:
            return render(request, 'id_reader/template/tips/showMeError.html', {'error': '未传入删除记录参数'})
    elif request.method == 'POST':
        partyName = request.POST.get('partyName')
        gender = request.POST.get('gender')
        certNumber = request.POST.get('certNumber')
        certAddress = request.POST.get('certAddress')
        addr_b4 = request.POST.get('addr_b4')
        phone = request.POST.get('phone')
        desti_addr = request.POST.get('desti_addr')
        is_danger = request.POST.get('is_danger')
        train_no = request.POST.get('train_no')
        bbh = request.POST.get('bbh')
        modify_id = request.POST.get('vid')
        try:
            if modify_id:
                models.Visitors.objects.filter(id=modify_id).update(visitor=partyName,
                                                                    gender=1 if gender == '1' else 0,
                                                                    id_no=certNumber, address=certAddress, phone=phone,
                                                                    addr_b4=addr_b4, desti_addr=desti_addr,
                                                                    is_danger=1 if is_danger == '1' else 0,
                                                                    train_no=train_no, bk1=bbh)
            else:
                models.Visitors.objects.create(visitor=partyName,
                                               gender=1 if gender == '1' else 0, is_danger=1 if is_danger == '1' else 0,
                                               id_no=certNumber, address=certAddress, phone=phone,
                                               addr_b4=addr_b4, desti_addr=desti_addr, train_no=train_no, bk1=bbh)
            order = models.Visitors.objects.all().order_by('-create_time')
            total, max_page, order, page, limit = paginator(order)
            bbh = check_bbh()
            msg = True
            return render(request, 'id_reader/id_reader2.html', locals())
        except Exception as e:
            return render(request, 'id_reader/template/tips/showMeError.html', {'error': e})
    else:
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        order = models.Visitors.objects.all().order_by('-create_time')
        bbh = check_bbh()
        if page and limit:
            total, max_page, order, page, limit = paginator(order, page, limit)
            return render(request, 'id_reader/id_reader2.html', locals())
        else:
            total, max_page, order, page, limit = paginator(order)
            return render(request, 'id_reader/id_reader2.html', locals())
