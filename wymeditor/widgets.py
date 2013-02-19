from django import forms
from django.conf import settings
from django.contrib.admin import widgets


class WYMEditorArea(forms.Textarea):
    def __init__(self, attrs={}, load_jquery=True):
        base_class = attrs.get("class", "")
        attrs['class'] = " ".join((base_class, "WYMEditor",))
        self.load_jquery = load_jquery
        super(WYMEditorArea, self).__init__(attrs=attrs)

    def _media(self):
        js = [
            '%swymeditor/jquery.wymeditor.js' % settings.STATIC_URL,
            '%sjs/load_wymeditor.js' % settings.STATIC_URL,
        ]
        
        if self.load_jquery:
            js.insert(0, 'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js')
            
        css = {
            "all": (
                "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/smoothness/jquery-ui.css",
                '%swymeditor/skins/twopanels/skin.css' % settings.STATIC_URL,
            )
        }

        return forms.Media(js=js, css=css)
    media = property(_media)


class AdminWYMEditorArea(WYMEditorArea, widgets.AdminTextareaWidget):
    pass
