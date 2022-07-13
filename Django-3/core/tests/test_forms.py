from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Alex'
        self.email = 'alex@bol.com.br'
        self.assunto = 'Hora da cerveja'
        self.mensagem = 'Me ve uma brahma bem gelada'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # ContatoForm(request.Post)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        resposta_1 = form1.send_mail()

        form2 = ContatoForm(data=self.dados)
        form2.is_valid()
        resposta_2 = form2.send_mail()

        self.assertEqual(resposta_1, resposta_2)
