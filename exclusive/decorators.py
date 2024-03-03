from django.shortcuts import redirect


# decorator to restrict views to registered users
def require_registered_user(view_func):
    def _wrapped_view(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated or not self.request.user.profile.registered:
            return redirect('course:pricing')
        return view_func(self, request, *args, **kwargs)

    return _wrapped_view
