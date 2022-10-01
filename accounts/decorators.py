# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib import messages


# default_message = "You must be approved to proceed."

# def applicant_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
#     '''
#     Decorator for views that checks that the logged in user is an applicant,
#     redirects to the log-in page if necessary.
#     '''
#     actual_decorator = user_passes_test(
#         lambda u: u.applicant_profile.approved and u.is_applicant,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
#     '''
#     Decorator for views that checks that the logged in user is a staff,
#     redirects to the log-in page if necessary.
#     '''
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_staff,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator

# try:
#     from functools import wraps
# except ImportError:
#     from django.utils.functional import wraps  # Python 2.4 fallback.

# # from django.utils.decorators import available_attrs

# from django.contrib import messages

# default_message = "You must be approved to proceed."

# def user_passes_test(test_func, message=default_message):
#     """
#     Decorator for views that checks that the user passes the given test,
#     setting a message in case of no success. The test should be a callable
#     that takes the user object and returns True if the user passes.
#     """
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             if not test_func(request.user):
#                 messages.error(request, message)
#             return view_func(request, *args, **kwargs)
#         return _wrapped_view
#     return decorator

# def login_required_message(function=None, message=default_message):
#     """
#     Decorator for views that checks that the user is logged in, redirecting
#     to the log-in page if necessary.
#     """
#     actual_decorator = user_passes_test(
#         lambda u: u.applicant_profile.approved and u.is_applicant,
#         #lambda u: u.is_authenticated, #fixed by removing ()
#         message=message,
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator        

from django.http import HttpResponse
# from django.shortcuts import redirect


def unapproved_users(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.applicant_profile.approved:
            return view_func(request, *args, **kwargs)
        else:
            url = request.META.get('HTTP_REFERER', '/')
            resp_body = '<script>alert("You cannot apply for a bursary unless your account has been approved");\
             window.location="%s"</script>' % url
            return HttpResponse(resp_body)
    return wrapper_func
    