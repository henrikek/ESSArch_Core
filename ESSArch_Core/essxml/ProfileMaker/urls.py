from django.conf.urls import url
from views import (
    create,
    edit,
    demo,
    index,
    add,
    # SubmitIPCreate,
)
# from views import {
#     create,
# }
from . import views

urlpatterns = [
    url(r'^$', index.as_view(), name='template_index'),
    url(r'^edit/(?P<name>[A-z0-9]+)/$', edit.as_view(), name='template_edit'),
    url(r'^add/$', add.as_view(), name='template_add'),
    url(r'^reset/$', views.resetData, name='reset_data_template'),
    url(r'^generate/(?P<name>[A-z]+)/$', views.generateTemplate, name='generate_template'),
    url(r'^struct/addChild/(?P<name>[A-z]+)/(?P<newElementName>[A-z]+)/(?P<elementUuid>[A-z0-9-]+)/$', views.addChild, name='add_data_template'),
    # url(r'^struct/addUserChild/(?P<name>[A-z]+)/$', views.addUserChild, name='add_userdata_template'),
    url(r'^struct/removeChild/(?P<name>[A-z]+)/(?P<uuid>[A-z0-9-]+)/$', views.deleteChild, name='add_data_template'),
    url(r'^struct/addAttrib/(?P<name>[A-z]+)/(?P<uuid>[A-z0-9-]+)/$', views.addAttribute, name='add_attrib_template'),
    url(r'^struct/setContainsFiles/(?P<name>[A-z]+)/(?P<uuid>[A-z0-9-]+)/(?P<containsFiles>[0-1])/$', views.setContainsFiles, name='setContainsFiles_template'),
    url(r'^struct/(?P<name>[A-z]+)/$', views.getStruct, name='get_data_template'),
    url(r'^struct/elements/(?P<name>[A-z0-9-]+)/$', views.getElements, name='get_element_template'),
    url(r'^make/$', create.as_view(), name='create_template'),
    # url(r'^edit/(?P<name>[A-z0-9-]+)/$', views.saveForm, name='update_template'),
    # url(r'^edit/$', edit.as_view(), name='edit_template'),
    url(r'^demo/$', demo.as_view(), name='demo'),
    url(r'^form/(?P<name>[A-z0-9-]+)/$', views.getForm, name='get_demo_form'),
    url(r'^data/(?P<name>[A-z0-9-]+)/$', views.getData, name='get_demo_data'),
    # url(r'^submitipcreate/(?P<id>\d+)$', SubmitIPCreate.as_view(), name='submit_submitipcreate'),
]
