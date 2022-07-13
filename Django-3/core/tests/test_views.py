from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.views import IndexView


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Alexsandro',
            'email': 'alexsandro@bol.com',
            'assunto': 'Chopp',
            'mensagem': 'Me ve mais um chopp'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Alexsandro',
            'email': 'alexsandro@bol.com',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)
