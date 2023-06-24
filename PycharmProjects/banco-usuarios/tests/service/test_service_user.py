from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        # Setup
        name_1 = "Daniele Seixas"
        job_1 = "QA"
        resultado_esperado = "Usuario adicionado"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado


    def test_add_user_usuario_invalido(self):
        # Setup
        name_1 = None
        job_1 = "QA"
        resultado_esperado = "Usuario invalido"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_user_value_number(self):
        # Setup
        name_1 = 98645
        job_1 = "QA"
        resultado_esperado = "Usuario invalido"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_user_duplicado(self):
        # Setup
        name_1 = "Eva Vilma"
        job_1 = "Singer"
        resultado_esperado = "Usuario ja existe"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)
        resultado = service.add_user(name=name_1, job=job_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_user_nao_encontrado(self):
        # Setup
        name_1 = "Paulo"
        job_1 = "QA"
        resultado_esperado = "Usuario nao encontrado"
        service = ServiceUser()

        # Chamada
        resultado = service.remove_user(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_user_job_atualizado(self):
        # Setup
        name_1 = "Tadeu"
        job_1 = "QA"
        job_2 = "PO"
        resultado_esperado = "Job do usuario atualizado com sucesso"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)
        resultado = service.update_user(name=name_1, new_job=job_2)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_location_job_user(self):
        # Setup
        name_1 = "Fernando"
        job_1 = "Finance"
        name_2 = "Josy"
        job_2 = "Finance"
        name_3 = "Amanda"
        job_3 = "UX"
        job_4 = "Finance"
        resultado_esperado = [('Fernando', 'Finance'), ('Josy', 'Finance')]
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)
        resultado = service.add_user(name=name_2, job=job_2)
        resultado = service.add_user(name=name_3, job=job_3)
        resultado = service.list_user(job=job_4)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_location_not_job_user(self):
        # Setup
        name_1 = "Fernado"
        job_1 = "Finance"
        name_2 = "Josy"
        job_2 = "Finance"
        name_3 = "Amanda"
        job_3 = "Dev"
        job_4 = "PO"
        resultado_esperado = "Nenhum usuário encontrado com o job informado"
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_1, job=job_1)
        resultado = service.add_user(name=name_2, job=job_2)
        resultado = service.add_user(name=name_3, job=job_3)
        resultado = service.list_user(job=job_4)

        # Avaliacao
        assert resultado_esperado == resultado