from django.urls import path
from . import views

urlpatterns = [

    path('shelves/', views.getShelves, name='get-Shelves'),
    path('shelf/add/', views.addShelf, name='add-Shelf'),
    path('shelf/delete/<str:shelf_id>/', views.deleteShelf, name='delete-Shelf'),
    path('shelf/update/<str:shelf_id>/', views.updateShelf, name='update-Shelf'),

    path('books/', views.getBooks, name='get-Boos'),
    path('book/add/', views.addBook, name='add-Book'),
    path('book/delete/<str:book_id>/', views.deleteBook, name='delete-Book'),
    path('book/update/<str:book_id>/', views.updateBook, name='update-Book'),

    path('chapters/', views.getChapters, name='get-Chapters'),
    path('chapter/add/', views.addChapter, name='add-Chapter'),
    path('chapter/delete/<str:chapter_id>/', views.deleteChapter, name='delete-Chapter'),
    path('chapter/update/<str:chapter_id>/', views.updateChapter, name='update-Chapter'),


    path('page/<str:page_id>/', views.getPage, name='get-Page'),
    path('pages/', views.getPages, name='get-Pages'),
    path('page/add/', views.addPage, name='add-Page'),
    path('page/delete/<str:page_id>/', views.deletePage, name='delete-Page'),
    path('page/update/<str:page_id>/', views.updatePage, name='update-Page'),

    path('last-activities/', views.last_activities_view, name='last-activities'),

]