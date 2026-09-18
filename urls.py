from django.urls import path

from .views import submit, show_exam_result


urlpatterns = [
    path(
        'submit/',
        submit,
        name='submit'
    ),

    path(
        'show_exam_result/',
        show_exam_result,
        name='show_exam_result'
    ),
]
