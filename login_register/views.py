from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse,reverse_lazy
from django.db.models import Q 


from datetime import datetime, timedelta

# # Create your views here.
# def homeview(request):
#     return render(request,'login_regi/home.html')




# # def  RegisterForms(request):
# #     registered = False
# #     if request.method == 'POST':
# #         form1 = Userform(request.POST)
# #         form2 = profilepictures(request.POST)
# #         if form1.is_valid() and form2.is_valid():
# #             obj = form1.save()
# #             obj.set_password(obj.password)
# #             obj.save()

# #             pro = form2.save()
# #             pro.user = obj
# #             if 'photo' in request.FILES:
# #                 pro.photo = request.FILES['photo']
# #                 pro.save()
# #             registered = True
# #             return redirect('home')

# #     else:
# #         form1 = Userform()
# #         form2 = profilepictures()
# #     context={
# #         'form1':form1,
# #         'form2':form2,
# #         'reg':registered
        
# #     }
# #     return render(request,'login_regi/contact.html',context)

# def  RegisterForms(request):

#     registered = False
#     if request.method == 'POST':
#         user_form = Userform(data=request.POST)
#         profile_form = profilepictures(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             obj = user_form.save()
#             obj.set_password(obj.password)
#             obj.save()
#             profilepicturess = profile_form.save(commit=False)
#             profilepicturess.user= obj
#             if 'photo' in request.FILES:
#                 profilepicturess.photo = request.FILES['photo']
#                 profilepicturess.save()
#                 registered= True
#             else:
#                 print('error')
#             return redirect('login')
#     else:
#         user_form = Userform()
#         profile_form = profilepictures()
       
#     return render(request,'login_regi/contact.html',{
#             'user_form':user_form,
#             'profile_form':profile_form,
#              'reg':registered,
#         })





# class ASn_POst(CreateView,LoginRequiredMixin):
#     form_class = PostNews
#     model = Post_Asn
#     template_name = 'goninda/post.html'

# class post_loc(CreateView,LoginRequiredMixin):
#     form_class = locs
#     model = location_model
#     template_name = 'goninda/location.html'



# class loc_list(LoginRequiredMixin,ListView):
#     context_object_name = 'loc_list'
#     model = location_model
#     template_name= 'goninda/loc_list.html'
#     queryset = location_model.objects.filter()





# class ASn_POst_listview(LoginRequiredMixin,ListView):
#     context_object_name = 'listdata'
#     model = Post_Asn
#     template_name= 'goninda/list.html'
#     queryset = Post_Asn.objects.filter()



# class postUpdate(LoginRequiredMixin, UpdateView):
#     form_class = PostNews
#     model = Post_Asn
#     template_name = 'uplode_news.html'




# class postUpdate_loc(LoginRequiredMixin, UpdateView):
#     form_class = locs
#     model = location_model
#     template_name = 'goninda/loc_update.html'

# class postdel_loc(LoginRequiredMixin, DeleteView):
#     model = location_model
#     template_name = 'goninda/loc_de.html'
#     success_url = reverse_lazy('lsoc')

# class postDelete(LoginRequiredMixin, DeleteView):
#     model = Post_Asn
#     template_name = 'delete_news.html'
#     success_url = reverse_lazy('homes')




# # class SearchResultsView(ListView):
# #     model = Post_Asn
# #     template_name = 'search_results.html'

# #     def get_queryset(self): # new
# #         query = self.request.GET.get('q')
# #         object_list = Post_Asn.objects.filter(
# #             Q(VLAN__icontains=query) | Q(LOCATION__icontains=query)
# #         )
# #         return object_list



# from django.shortcuts import render
# from django.db.models import Q


# def SearchResultsView(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')
#         submitbutton= request.GET.get('submit')
#         results= dailybilling.objects.filter(Q(date__icontains=query) | Q(cost_profile__cost_name__icontains=query))
#         context={'results': results,
#                      'submitbutton': submitbutton}
#         return render(request, 'goninda/search_results.html', context)
#     else:
#         return render(request, 'goninda/search_results.html')




# #   def get(self, request, category, *args, **kwargs):
# #         authors = tag_createors.objects.filter(selet_channel__query_slug=category).values('tagSlug', 'tagNameBG','selet_channel__query_slug')
# #         if authors:
# #             posts = PostCreate.objects.filter(selete_channel_tag__query_slug=category).values('title', 'slug', 'photo','view','is_active','Seoimgalt').order_by('-id')
# #             for author in list(authors):
# #                 response = {
# #                 'tagSlug': author['tagSlug'],
# #                 'tagNameBG': author['tagNameBG'],
# #                 'Main_Tag': author['selet_channel__query_slug']

# #                 }
# #             page = self.paginate_queryset(list(posts))
# #             response['List'] = page
# #             paginated_response = self.get_paginated_response(response)
# #             return JsonResponse(paginated_response.data, safe=False)
# #         return HttpResponse('No matching data found', status=404)



# class post_user_data(LoginRequiredMixin,CreateView):
#     form_class = userform
#     model = userinfo
#     template_name = 'nv/uplode_us.html'


# class list_user(LoginRequiredMixin,ListView):
#     context_object_name = 'list_user'
#     model = userinfo
#     template_name= 'nv/list_user.html'
#     queryset = userinfo.objects.order_by('id')


# class warning_user(LoginRequiredMixin,ListView):
#     template_name= 'nv/warning_page.html'





# def index(request):
#     context = {
#         'num_books': "This page only allowed super admin ('-')",
#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'nv/warning_page.html', context=context)




 

# def indexs(request):
#     context = {
#         'Pon_1': "Pon-1 : Tv center + Maijdee Bazar + AnswerCamp Rode",
#         'Pon_2': "Pon-2 : Bothola + Rajgonj + Chodan",
#         'Pon_3': "Pon-3 : Sonapur + Doterhat + Porobazar",
#         'Pon_4': "Pon-4 : Lokkinaron Pur + Studiam Pichone + Master Para + Notun Bus stand +Napiterpoll ",
#         'Pon_5': "Pon-5 : Soon",
#         'Pon_6': "Pon-6 : Gabua",
#         'Pon_7': "Pon-7 : Soon",
#         'Pon_8': "Pon-8 : Soon",


 

#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'nv/pon_list.html', context=context)




# def loc_lshotlist(request):
#     context = {
#         'LS': " LS - ????????????????????????????????????????????? + ?????????????????? ???????????????????????????",
#         'GT': " GT - ?????????????????? + ???????????? ????????????????????? ",
#         'RR': " RR - ??????????????? + ???????????? + ?????????????????????",
#         'CR': " CR - ???????????????????????? ?????????????????? ????????????",
#         'MB': " MB - ?????????????????? ???????????????",
#         'HR': " HR - ???????????????????????? ????????? ",
#         'AC': " AC - ??????????????? ????????????????????? ?????????",
#         'MP': " MP - ???????????????????????????????????? + ??????????????????????????? ???????????? ????????????",
#         'SP': " SP - ?????????????????? ??????????????? + ??????????????? ???????????? ?????????",
#         'SD': " SD - ????????????????????? + ??????????????????????????? + ????????????????????????",
#         'HG': " HG - ??????????????????",
#         'CC': " CC - Chorasta + Chawmuni",
#         'NP': " NP - Notun Busstand + Napiter poll",


 


#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'nv/area.html', context=context)







# # class post_user_dsata(LoginRequiredMixin,CreateView):
# #     form_class = profilecostform
# #     model = costprofile
# #     template_name = 'nv/uplode_us.html'



# # class posnt_user_dsata(LoginRequiredMixin,CreateView):
# #     form_class = profilecostform
# #     model = costprofile
# #     template_name = 'nv/uplode_us.html'



# class dailybing_view(LoginRequiredMixin,CreateView):

#     form_class = dailyscosst
#     model = dailybilling
#     template_name = 'nv/uplode_us.html'






# class daulycost_list(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/list.html'
#     #queryset = dailybilling.objects.filter(created_date__gte=datetime.now() - timedelta(days=1))
#     queryset = dailybilling.objects.filter(date__range=["2021-05-11", "2021-06-11"]).exclude(cost_profile__cost_name__contains='Advance salary')



# # class daulycost_list(LoginRequiredMixin,ListView):
# #     context_object_name = 'fulllist'
# #     model = dailybilling
# #     template_name= 'goninda/list.html'
# #     queryset = dailybilling.objects.filter(dateES__gt=datetime.now() - timedelta(hours=12))

# class datashort_profile(LoginRequiredMixin,ListView):
#     context_object_name = 'ssdxsx'
#     model = dailybilling
#     template_name= 'goninda/list.html'
#     # queryset = dailybilling.objects.filter(cost_profile__contains='Terry')






# class OFFICE_COST(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Office Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_bike(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Bike Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_family(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Family',date__range=["2021-05-11", "2021-06-11"])


# class OFFICE_product(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Product Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_salllery(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Salary',date__range=["2021-05-11", "2021-06-11"])


# class OFFICE_trnasportcost(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Transport Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_Chika(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Chika',date__range=["2021-05-11", "2021-06-11"])


# class OFFICE_internetbill(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='orange',date__range=["2021-05-11", "2021-06-11"])


# class OFFICE_Electric(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Electric Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_Employ(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Employ Cost',date__range=["2021-05-11", "2021-06-11"])



# class OFFICE_Pickup(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/cost.html'
#     queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Pickup Cost',date__range=["2021-05-11", "2021-06-11"])




# class updatedailyline(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = userupdate
#     template_name= 'goninda/dalyconnection.html'


# def updatessdata(request):
#     allupdatedate = userupdate.objects.all()
#     lastconnection = userupdate.objects.last()
#     return render(request,"goninda/dalyconnection.html",{"dataone":allupdatedate,"datatwo":lastconnection})






# # class loosan(LoginRequiredMixin,ListView):
# #     context_object_name = 'fulsllist'
# #     model = loon
# #     template_name= 'goninda/loon.html'




# def looan(request):
#     BDDDKASH = loon.objects.filter(loon_source__contains='B')
#     PREPAIDBILL = loon.objects.filter(loon_source__contains='P')
#     MONTHLYBILL = loon.objects.filter(loon_source__contains='M')
#     ROUTER = loon.objects.filter(loon_source__contains='R')
#     alldata = loon.objects.all()


#     return render(request,"goninda/loon.html",{'alldata':alldata,'BKASH':BDDDKASH,'PREPjjAIDBILL':PREPAIDBILL,'MONTHLYBILL':MONTHLYBILL,'ROUTER':ROUTER})





# # def montlybillview(request):
# #     bill = monthlybill.objects.all()
# #     paid_user = monthlybill.objects.filter(payment_status__name=True).count()
# #     print(paid_user)
# #     return render(request,"goninda/montlybill.html",{'bill':bill,'paidsuser':paid_user})

# class montlybillview(LoginRequiredMixin,ListView):
#     model = monthlybill
#     template_name= 'goninda/montlybill.html'
    

#     def get_context_data(self, **kwargs):
#          exclude_list = ['21507', '21547']
#          context = super(montlybillview, self).get_context_data(**kwargs)
#          context['alldata'] = monthlybill.objects.all().order_by('-id').exclude(user_id__contains=exclude_list)
#          context['totaluser'] = monthlybill.objects.all().count()
#          context['paiduser'] = monthlybill.objects.filter(payment_status=True).count()
#          context['unpaiduser'] = monthlybill.objects.filter(payment_status=False).count()
#          return context



# from django.db.models import Sum

# class bkashpayment(LoginRequiredMixin,ListView):
#     model = monthlybill
#     template_name= 'goninda/nk.html'

#     def get_context_data(self, **kwargs):
#          context = super(bkashpayment, self).get_context_data(**kwargs)
#          context['ddfcdc'] = monthlybill.objects.aggregate(Sum('pkg'))
#          context['bkshuser'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH')
#          context['countbkash'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH').count()
#          context['countCASH'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH').count()
#          context['countNAGAD'] = monthlybill.objects.filter(payment_method__methosd__contains='NAGAD').count()


#          context['totaluser'] = monthlybill.objects.all().count()
#          context['paiduser'] = monthlybill.objects.filter(payment_status=True).count()
#          context['unpaiduser'] = monthlybill.objects.filter(payment_status=False).count()
#          return context
  


# # class bkashpayment(LoginRequiredMixin,ListView):
# #     context_object_name = 'fulllist'
# #     model = bkashuserpaymanet
# #     template_name= 'goninda/nk.html'
  

# # objects.filter(payment_method__methosd__contains='CASH').annotate(due_taka_total=Sum('duetaka__customer_due')).order_by('-customer_updated')
# # class API_objedfcts(APIView, PaginationHandlerMixin):
# #     pagination_class = StandadrdResultsSetPagination

# #     def get(self, request, category, *args, **kwargs):
# #         authors = tag_createors.objects.filter(tagSlug=category).values('tagSlug','tag_name')
# #         if authors:
# #             posts = PostCreate.objects.filter(tag_creator__tagSlug=category).values('title', 'slug', 'photo','release_date','view','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
# #             for author in list(authors):
# #                 response = {
# #                 'tagSlug': author['tagSlug'],
# #                 'tag_name': author['tag_name']

# #                 }
# #             page = self.paginate_queryset(list(posts))
# #             response['List'] = page
# #             paginated_response = self.get_paginated_response(response)
# #             return JsonResponse(paginated_response.data, safe=False)
# #         return HttpResponse('No matching data found', status=404)





# def qurydata(request):
#     if request.method == 'GET':
#         query= request.GET.get('f')
#         submitbutton= request.GET.get('subtmit')
#         results= userupdate.objects.filter(Q(date_user__icontains=query))
#         context={'results': results,
#                      'submitbutton': submitbutton}
#         return render(request, 'query/connectionnew.html', context)
#     else:
#         return render(request, 'query/connectionnew.html')



# def dailyserach(request):
#     if request.method == 'GET':
#         query= request.GET.get('f')
#         submitbutton= request.GET.get('subtmit')
#         results= dailybilling.objects.filter(Q(date__icontains=query))
#         context={'results': results,
#                      'submitbutton': submitbutton}
#         return render(request, 'query/daulynilingserach.html', context)
#     else:
#         return render(request, 'query/daulynilingserach.html')





# class montlybill_update(LoginRequiredMixin, UpdateView):
#     form_class = dailybillupdatefoms
#     model = monthlybill
#     template_name = 'goninda/loc_update.html'









# class cash(LoginRequiredMixin,ListView):
#     context_object_name = 'bkshuser'
#     model = monthlybill
#     template_name= 'goninda/cash.html'
#     queryset = monthlybill.objects.filter(payment_method__methosd__contains='CASH')


# class nagad(LoginRequiredMixin,ListView):
#     context_object_name = 'bkshuser'
#     model = monthlybill
#     template_name= 'goninda/nagad.html'
#     queryset = monthlybill.objects.filter(payment_method__methosd__contains='NAGAD')


# class unpaid(LoginRequiredMixin,ListView):

#     context_object_name = 'alldata'
#     model = monthlybill
#     template_name= 'goninda/montlybill.html'
#     queryset =  monthlybill.objects.filter(payment_status=False)



    

# class paydate(LoginRequiredMixin,ListView):
#     model = monthlybill
#     template_name= 'goninda/montlybill.html'

#     def get_context_data(self, **kwargs):
#          context = super(paydate, self).get_context_data(**kwargs)
#          context['alldata'] = monthlybill.objects.filter(pay_date__range=["2021-05-09", "2021-05-11"])
#          context['count'] = monthlybill.objects.filter(pay_date__range=["2021-05-09", "2021-05-11"]).count()
#          return context
  






class marketing_classview(LoginRequiredMixin,CreateView):
    form_class = Markting_updatefrom
    model = Marketing_update
    template_name = 'nv/uplode_monthbill.html'





class bkashtotal(LoginRequiredMixin,ListView):
    model = Marketing_update
    template_name= 'goninda/bkashtotal.html'

    def get_context_data(self, **kwargs):
         context = super(bkashtotal, self).get_context_data(**kwargs)
         context['countfollowup'] = Marketing_update.objects.filter(status__status_cos__contains='Follow').count()
         context['bkshuser'] = Marketing_update.objects.all()
         return context




class OFFICE_Pickup(LoginRequiredMixin,ListView):
    model = Marketing_update
    template_name= 'goninda/bkashtotal.html'
   
    def get_context_data(self, **kwargs):
         context = super(OFFICE_Pickup, self).get_context_data(**kwargs)
         context['countfollowup'] = Marketing_update.objects.filter(status__status_cos__contains='Follow').count()
         context['bkshuser'] = Marketing_update.objects.filter(status__status_cos__contains='Follow')

         return context



class cnfm(LoginRequiredMixin,ListView):
    model = Marketing_update
    template_name= 'goninda/bkashtotal.html'
   
    def get_context_data(self, **kwargs):
         context = super(cnfm, self).get_context_data(**kwargs)
         context['countconfirm'] = Marketing_update.objects.filter(status__status_cos__contains='Confirm').count()
         context['bkshuser'] = Marketing_update.objects.filter(status__status_cos__contains='Confirm')

         return context

