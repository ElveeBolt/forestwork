from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin


class UserCheckTypeEmployerMixin(UserPassesTestMixin):
    """
    Mixin of check type user.
    """
    def test_func(self):
        return self.request.user.type == 1

    def handle_no_permission(self):
        raise Http404('User type is not employer')


class UserCheckJobAuthorMixin(UserPassesTestMixin):
    """
    Mixin of check if user author of this job.
    """
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.user

    def handle_no_permission(self):
        raise Http404('User is not author of this job')