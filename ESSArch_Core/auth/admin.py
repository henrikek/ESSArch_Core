# -*- coding: UTF-8 -*-


from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.admin import GroupAdmin as DjangoGroupAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group as DjangoGroup
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from groups_manager.models import Group as GroupManagerGroup
from groups_manager.models import GroupEntity, GroupMemberRole as GroupManagerGroupMemberRole, GroupType as GroupManagerGroupType
from groups_manager.models import GroupMember as GroupManagerGroupMember
from groups_manager.models import Member as GroupManagerMember
from nested_inline.admin import NestedModelAdmin, NestedTabularInline

from ESSArch_Core.admin import NestedStackedInlineWithoutHeader
from ESSArch_Core.auth.models import (Group, GroupMember, GroupMemberRole, GroupType, Member, ProxyGroup,
                                      ProxyUser, ProxyPermission)

User = get_user_model()

admin.site.unregister(
    [GroupManagerMember, GroupManagerGroup, GroupManagerGroupMember, GroupEntity, GroupManagerGroupMemberRole, GroupManagerGroupType])


def filter_permissions(qs):
    apps = ['groups_manager']
    excluded = Q(~Q(content_type__model='grouptype'), content_type__app_label__in=apps)
    return qs.exclude(excluded)


class GroupMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupMemberForm, self).__init__(*args, **kwargs)
        self.fields['expiration_date'].required = False
        self.fields['roles'].required = False
        self.fields['group'].disabled = True

    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupMemberInline(NestedTabularInline):
    form = GroupMemberForm
    filter_horizontal = ['roles']
    fields = ['group', 'member', 'expiration_date', 'roles']
    model = GroupMember
    extra = 0
    verbose_name_plural = _('group settings')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class MemberInline(NestedStackedInlineWithoutHeader):
    model = Member
    exclude = ['username', 'first_name', 'last_name', 'email', 'django_auth_sync']
    inlines = [GroupMemberInline]
    fieldsets = (
        (None, {
            'fields': [],
            'description': _("Groups added above appears here when saving")
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class UserAdmin(DjangoUserAdmin, NestedModelAdmin):
    add_form_template = 'essauth/admin/user/add_form.html'
    inlines = [MemberInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)})
    )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'user_permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            kwargs['queryset'] = filter_permissions(qs)
        return super(UserAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)

    def has_add_permission(self, request):
        return request.user.has_perm("%s.%s" % ('auth', 'add_user'))

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('auth', 'change_user'))

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('auth', 'delete_user'))

    def has_module_permission(self, request):
        return request.user.has_module_perms('auth')


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['group_type'].required = False

    def save(self, commit=True):
        group = super(GroupForm, self).save(commit=False)
        group.name = group.django_group.name
        if commit:
            group.save()
            self._save_m2m()
        return group

    class Meta:
        model = Group
        fields = ['group_type', 'parent']


class GroupInline(admin.StackedInline):
    form = GroupForm
    model = Group

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class GroupAdmin(DjangoGroupAdmin):
    add_form_template = 'essauth/admin/group/add_form.html'
    change_list_template = 'admin/mptt_change_list.html'
    inlines = [GroupInline]

    def get_ordering(self, request):
        """
        Changes the default ordering for changelists to tree-order.
        """
        mptt_opts = Group._mptt_meta
        return ('essauth_group__{}'.format(mptt_opts.tree_id_attr), 'essauth_group__{}'.format(mptt_opts.left_attr))

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            kwargs['queryset'] = filter_permissions(qs)
        return super(GroupAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)

    def has_add_permission(self, request):
        return request.user.has_perm("%s.%s" % ('auth', 'add_group'))

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('auth', 'change_group'))

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('auth', 'delete_group'))

    def has_module_permission(self, request):
        return request.user.has_module_perms('auth')


class GroupTypeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.has_perm("%s.%s" % ('groups_manager', 'add_grouptype'))

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('groups_manager', 'change_grouptype'))

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm("%s.%s" % ('groups_manager', 'delete_grouptype'))

    def has_module_permission(self, request):
        return request.user.has_module_perms('groups_manager')


class GroupMemberRoleAdmin(admin.ModelAdmin):
    filter_horizontal = ['permissions']


admin.site.unregister(DjangoGroup)
admin.site.unregister(User)
admin.site.register(ProxyPermission)
admin.site.register(ProxyGroup, GroupAdmin)
admin.site.register(ProxyUser, UserAdmin)
admin.site.register(GroupType, GroupTypeAdmin)
admin.site.register(GroupMemberRole, GroupMemberRoleAdmin)
