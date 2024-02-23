from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # perms_map is defined in DjangoModelPermissions
    # override like below to create custom permissions
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # flaw in below, if you have one permission you get all
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         # app_name.verb_model_name
    #         if user.has_perm("product.view_product"):
    #             return True
    #         if user.has_perm("product.add_product"):
    #             return True
    #         if user.has_perm("product.change_product"):
    #             return True
    #         if user.has_perm("product.delete_product"):
    #             return True
    #     return False
