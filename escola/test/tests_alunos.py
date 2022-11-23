from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status

class AlunosTestCase(APITestCase):

    def setUp(self):
        
        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome='Teste', rg='123456789', cpf='12345678901', data_nascimento='2000-12-02',
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Teste 2', rg='123456788', cpf='12345678902', data_nascimento='2000-12-03',
        )
 
    def test_get_alunos(self):
        """Teste para verificar a requisição GET de valores para alunos"""

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_aluno(self):
        """Teste para verificar a requisição POST para criar um aluno"""

        data = {
            'nome':'Teste',
            'rg':'123456789',
            'cpf':'12345679801',
            'data_nascimento': '2000-12-04'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_aluno(self):
        """Teste para verificar a requisição DELETE não é permitida para deletar um aluno"""
        
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_para_atualizar_aluno(self):
        """Teste para verificar a requisição PUT para atualizar um aluno"""
        
        data = {
            'nome':'Teste 2',
            'rg':'123456785',
            'cpf':'12345679811',
            'data_nascimento': '2000-12-22'
        }
        response = self.client.put('/alunos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)