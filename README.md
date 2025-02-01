This project is a Multilingual FAQ System built with Django and Django REST Framework. 
It allows users to create and manage FAQs with support for multiple languages, including English, Hindi, and Bengali. 
The application uses Google Translate API for automatic translations and integrates a WYSIWYG editor for rich-text answers.


API Usages
API Root - http://127.0.0.1:8000/
Faq List - http://127.0.0.1:8000/faqs/
Admin - http://127.0.0.1:8000/admin/

Admin 
username: Somorjit
password: somorjit


Enter any question in Question Option and enter answer relevent to question. Then click on POST.

The project will translate the Question and Answer into HINDI and BENGALI. 

Example:
        question: what is your name"
        answer": My name is somorjit"
        question_hi: आपका क्या नाम है"
        answer_hi: मेरा नाम सोमोरजीत है"
        question_bn: আপনার নাম কি"
        answer_bn: আমার নাম সোমোরজিৎ"
