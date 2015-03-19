# -*-coding:utf-8 -*-
'''
Created on 2015-3-16

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django import forms
from lshare.models import Photo
from common.image_utils import GenericImageParser
from django.conf import settings
from common.image_utils import ModelImageParser
from lshare.models import Inter
from ueditor.widgets import UEditorWidget

class PhotoForm(forms.ModelForm):
	def clean(self):
		if 'image' in self.changed_data:
			image = self.cleaned_data.get('image', None)
			if image:
				handler = GenericImageParser([image], settings.PHOTO_CONF)
				if not handler.is_valid():
					self._errors['image'] = self.error_class([handler.error])
			else:
				self._errors['image'] = self.error_class([u'上传的图片无效'])
		return self.cleaned_data

	def save(self, commit=True):
		result = super(PhotoForm, self).save(commit=commit)
		result.save()

		if 'image' in self.changed_data:
			handler = ModelImageParser(result.image.path, settings.PHOTO_CONF)
			handler.parse()
			handler.save()

			if handler.parsed.size[0] > 950:
				result.has_large_size = True
			else:
				result.has_large_size = False
			result.save()

		return result

	class Meta:
		model = Photo
		widgets = {
			'description': forms.Textarea
		}

class FocusForm(forms.ModelForm):
    def clean(self):
        if 'cover' in self.changed_data:
            image = self.cleaned_data.get('cover', None)
            if image:
                handler = GenericImageParser([image], settings.INTER_IMAGE_CONF)
                if not handler.is_valid():
                    self._errors['cover'] = self.error_class([handler.error])
            else:
                self._errors['cover'] = self.error_class([u'上传的图片无效'])
        return self.cleaned_data

    def save(self, commit=True):
        result = super(FocusForm, self).save(commit=commit)
        result.save()

        if 'cover' in self.changed_data:
            handler = ModelImageParser(result.cover.path, settings.INTER_IMAGE_CONF)
            handler.parse()
            handler.save()

        return result

    class Meta:
        model = Inter
        widgets = {
            'abstract': forms.Textarea,
            'content': UEditorWidget(width=1000,
                                     file_path='/downloads/',
                                     image_path=settings.INTER_UPLOADED_IMAGE_URL,
                                     scrawl_path=settings.INTER_UPLOADED_IMAGE_URL)
        }
