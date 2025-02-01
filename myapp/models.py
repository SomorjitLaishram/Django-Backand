from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator  # googletrans or googletrans==4.0.0-rc1 for translation

class FAQ(models.Model):
    question = models.TextField()  # Default question (in English)
    answer = RichTextField()  # WYSIWYG editor for the answer

    # Language-specific translations for the question and answer
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.question
    
    def get_translated_text(self, lang='en'):
        """
        Method to get translated question and answer based on the language selection.
        """
        question_field = f"question_{lang}" if hasattr(self, f"question_{lang}") else 'question'
        answer_field = f"answer_{lang}" if hasattr(self, f"answer_{lang}") else 'answer'

        # Translate text if not present in the specified language
        question = getattr(self, question_field, self.question)
        answer = getattr(self, answer_field, self.answer)

        return {
            "question": question,
            "answer": answer
        }

    def save(self, *args, **kwargs):
        """
        Override save method to handle automatic translation during object creation.
        """
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')

        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')
        
        super().save(*args, **kwargs)
    
    def translate_text(self, text, lang):
        """
        Helper function to handle automatic translation using googletrans API.
        """
        try:
            translator = Translator()
            translated = translator.translate(text, dest=lang)
            return translated.text
        except Exception as e:
            return text  # Return original text if translation fails

