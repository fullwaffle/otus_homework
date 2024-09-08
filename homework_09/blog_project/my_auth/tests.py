from django.contrib.auth import get_user_model
from django.test import TestCase


class BlogUserRegisterTest(TestCase):
    def setUp(self):
        self.username = "otus"
        self.email = "admin@otus.local"
        self.password1 = "OtusOtus"
        self.password2 = "OtusOtus"
        self.bad_password2 = "Otus"

    def test_succ_register(self):
        response = self.client.get("/auth/register/")

        self.assertContains(response, "Username:", status_code=200)

        response = self.client.post(
            "/auth/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password1,
                "password2": self.password2,
            },
        )

        self.assertEqual(302, response.status_code)

        new_user = get_user_model().objects.get(username=self.username)

        self.assertEqual(self.email, new_user.email)

    def test_fail_register(self):
        response = self.client.post(
            "/auth/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password1,
                "password2": self.bad_password2,
            },
        )
        self.assertEqual(200, response.status_code)

        self.assertFormError(
            response.context["form"],
            "password2",
            ["The two password fields didn’t match."],
        )

    def tearDown(self):
        del self.username
        del self.email
        del self.password1
        del self.password2
