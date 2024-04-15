from django.urls import path
from .import views


urlpatterns=[
     path('login',views.loginpage,name='login'),
     path('logout',views.logoutpage,name='logout'),
     path('header',views.header),
     path('base',views.base),
     path('main',views.main),
     path('ba',views.ba,name='ba'),
     path('footer',views.footer),
     path('home',views.home),
     path('ahome',views.ahome),
     path('about',views.about,name='ab'),
     path('aupnoti',views.aupnoti,name='aupnoti'),
     path('anotif',views.anotif,name='anotif'),
     path('anoti',views.anoti,name='anoti'),
     path('back',views.back, name='back'),
     path('aedit/<int:id>',views.aup,name='aedit'),
     path('adelete/<int:id>',views.adtl,name='adelete'),
     path('profile',views.profile,name='profile'),
     path('go_back',views.go_back, name='go_back'),
     path('goback',views.goback, name='goback'),
     path('ho',views.ho),
     path('search',views.search,name='search'),
     path('btime',views.btime),
     path('create',views.Createupdate.as_view()),
     path('buslist',views.BusList,name='busli'),
     path('abuslist',views.AbusList,name='abusli'),
     path('notif',views.notif,name='notif'),
     path('register',views.Reg,name='register'),
     path('get',views.up,name='edit'),
     path('noti',views.noti,name='noti'),
     path('upnoti',views.upnoti,name='upnoti'),
     path('edit/<int:id>',views.eedit,name='ebdet'),
     path('delete/<int:id>',views.dtl,name='bdlt')
  
]