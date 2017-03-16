# -*-coding:utf-8 -*-
'''
Created on 2015-2-18

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django import forms
from lsite.models import Focus

class FocusForm(forms.ModelForm):
    def clean(self):
        if 'image' in self.changed_data:
            image = self.cleaned_data.get('image', None)
            if image:
                handler = GenericImageParser([image], settings.FOCUS_IMAGE_CONF)
                if not handler.is_valid():
                    self._errors['image'] = self.error_class([handler.error])
            else:
                self._errors['image'] = self.error_class([u'上传的图片无效'])
        return self.cleaned_data
    
    def save(self, commit=True):
        result = super(FocusForm, self).save(commit=commit)
        result.save()

        if 'image' in self.changed_data:
            handler = ModelImageParser(result.image.path, settings.FOCUS_IMAGE_CONF)
            handler.parse()
            handler.save()
        
        return result
    
    class Meta:
        model = Focus 
        widgets = {
            'description': forms.Textarea    
        }
