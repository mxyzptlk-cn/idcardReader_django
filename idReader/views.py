from django.shortcuts import render
from django.http import JsonResponse
import os, shutil
from math import ceil
from idReader import models


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
        modify_id = request.POST.get('vid')
        try:
            if modify_id:
                print(modify_id)
                models.Visitors.objects.filter(id=modify_id).update(visitor=partyName,
                                                                    gender=1 if gender == '1' else 0,
                                                                    id_no=certNumber, address=certAddress, phone=phone,
                                                                    addr_b4=addr_b4, desti_addr=desti_addr,
                                                                    is_danger=1 if is_danger == '1' else 0,
                                                                    train_no=train_no)
            else:
                models.Visitors.objects.create(visitor=partyName,
                                               gender=1 if gender == '1' else 0, is_danger=1 if is_danger == '1' else 0,
                                               id_no=certNumber, address=certAddress, phone=phone,
                                               addr_b4=addr_b4, desti_addr=desti_addr, train_no=train_no)
            order = models.Visitors.objects.all().order_by('-create_time')
            total, max_page, order, page, limit = paginator(order)
            msg = True
            return render(request, 'id_reader/id_reader2.html', locals())
        except Exception as e:
            return render(request, 'id_reader/template/tips/showMeError.html', {'error': e})
    else:
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        order = models.Visitors.objects.all().order_by('-create_time')
        if page and limit:
            total, max_page, order, page, limit = paginator(order, page, limit)
            return render(request, 'id_reader/id_reader2.html', locals())
        else:
            total, max_page, order, page, limit = paginator(order)
            return render(request, 'id_reader/id_reader2.html', locals())
