from rest_framework import permissions

# 添加特定动作的权限
class IsLoggedInUserOrAdmin(permissions.BasePermission):
    """验证请求的用户是否是本人或是管理员"""
    def has_object_permission(self, request, view, obj):
        print("$$: ", request.user, obj)
        return obj == request.user or request.user.is_superuser


class IsAdminUser(permissions.BasePermission):
    """has_permission在刚开始判断请求的时候调用, has_object_permission在get_object的时候调用"""
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        print(request.user)
        return request.user and request.user.is_superuser

class NoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False

    def has_permission(self, request, view):
        return False

class IsArticleOwnerOrAdmin(permissions.BasePermission):
    """检查是否是本人或者管理员"""
    def has_permission(self, request, view):
        # 如果是创建文章，则只允许创建作者为自己的文章
        if request.method == 'POST':
            if 'user' not in request.data:
                return False
            print(request.data['user'] == request.user.username)
            return request.data['user'] == request.user.username
        return True

    def has_object_permission(self, request, view, obj):
        print(request.user, obj.user)
        print(request.user.is_superuser)
        return obj.user == request.user or request.user.is_superuser

class IsAvatarOwnerOrAdmin(permissions.BasePermission):
    """检查是否是照片对应的用户或者管理员"""
    def has_object_permission(self, request, view, obj):
        return obj.userprofile.user_id == request.user.id or request.user.is_superuser



