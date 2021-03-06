from nested_inline.admin import (NestedModelAdmin, NestedStackedInline,
                                 NestedTabularInline)

default_app_config = 'ESSArch_Core.admin.apps.AdminConfig'


class NestedStackedInlineWithoutHeader(NestedStackedInline):
    template = "essadmin/edit_inline/stacked-nested-without-header.html"
