import datetime
import json
import random

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.context_processors import shop_count
from apps.index.models import *


@login_required
def list(reqeust):
    if reqeust.user.id:
        car_list = ShopCar.objects.filter(user_id=reqeust.user.id)
        for car in car_list:
            car.shop = car.shop_id
            car.img = ShopImage.objects.filter(shop_id=car.shop_id).first()
        return render(reqeust, 'cate_user.html', {'car_list': car_list})
    else:
        return HttpResponse('请先登录')


# @login_required
# def add_car(request):
#     # result = {'status': 200, 'msg': 'ok'}
#     if request.method == 'POST':
#         try:
#             number = request.POST.get("number")
#             shop_id = request.POST.get('shop_id')
#             if number and shop_id:
#                 car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id)
#
#                 if car.exists():
#                     car.update(shop_number=F('shop_number') + number)
#                 else:
#
#                     car = ShopCar(shop_number=number, shop_id_id=shop_id, user_id_id=request.user.id)
#                     car.save()
#                 count_dict = shop_count(request)
#                 # data['status'] = 200
#                 # data['msg'] = 'success'
#                 data = dict(
#                     status=200,
#                     msg='sucess',
#                     count=count_dict['count'],
#                 )
#                 return JsonResponse(data=data)
#         except Exception as e:
#             result = {'status': 400, 'msg': '添加失败'}
#             return JsonResponse(result)
#     else:
#         result = {'status': 2, 'msg': '不支持的请求方式'}
#         return JsonResponse(result)



@csrf_exempt
def add_car(request):
    # 判断是否是ajax请求
    if request.is_ajax():
        # 判断用户是否登录
        if request.user.is_authenticated:
            try:
                '''
              参数：商品的数量，商品id
              当商品已经存在用户的购物车的时候，更新数量，当不存在的时候创建该记录
              '''
                number = request.POST.get("number")
                shop_id = request.POST.get('shop_id')
                if number and shop_id:
                    car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id)

                    if car.exists():
                        car.update(shop_number=F('shop_number') + number)
                    else:

                        car = ShopCar(shop_number=number, shop_id_id=shop_id, user_id_id=request.user.id)
                        car.save()
                data = shop_count(request)
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                # 表示添加购物车失败
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            # 没有登录返回登录页面
            url = 'account/login/?next=%s' % request.path
            return JsonResponse(data={'status': 302, 'msg': 'success', 'url': url})
    elif request.method == 'GET':
        return redirect('/')


def update(request):
    pass


def detlete(request):
    pass

# # 开始事务
# @ajax
# @login_required
# def confirm(request):
#     if request.method == 'POST':
#         cars_str = request.POST.get('car')
#         if cars_str:
#             cars = json.loads(cars_str)
#             try:
#                 # 开启事务
#                 with transaction.atomic():
#                     # 生成订单
#                     oid = product_order(request, cars)
#                     #      做事务相关的操作
#                     for car in cars:
#                         ShopCar.objects.filter(car_id=car.get('car_id')).update(number=car.get('num'), order_id=oid)
#                 #    生成订单的操作
#                 return {'oid': oid}
#             except Exception as e:
#                 transaction.rollback()
#         else:
#             pass
#
#
# # 生成订单信息
# def product_order(request, cars):
#     # 第一步生成订单号  全站必须唯一   尽量大于8位
#     user_id = request.user.id
#     order_code = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100000,999999)}"
#     order = Order(order_code=order_code, user_id=user_id)
#     order.save()
#     return order.oid
#
#
# @login_required
# def order(request):
#     oid = request.GET.get('oid')
#     shops = ShopCar.objects.filter(order_id=oid)
#     return render(request, 'confirm.html', {'shops': shops})
