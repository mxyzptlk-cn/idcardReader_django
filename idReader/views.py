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


def index(request):
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


