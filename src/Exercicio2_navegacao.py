import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton, FontWeight
from flet.controls import page


def main(page: flet.Page,):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK # ou ThemeMode Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    def exibir_msg():
        text_nome.value = input_nome.value
        text_cpf.value = input_cpf.value
        text_email.value = input_email.value
        text_salario.value = f"R$ {input_salario.value}"


        tem_erro = False
        if  input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if  input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatorio"

        if  input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio"

        if  input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio"


        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
            navegar("/tela_msg")


    # Componentes
    text_nome = Text()
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    input_nome = TextField(label="Nome")
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="E-mail")
    input_salario = TextField(label="Salario")



    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Escreva seu nome e sobrenome",
                        bgcolor=Colors.CYAN_700
                    ),

                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,


                    Button("Cadastrar", on_click=lambda: navegar("/exibir_msg")),
                ]
            )
        )
        if page.route == "/tela":
            text_nome.value = f"{input_nome.value}"
            text_cpf.value = f"{input_cpf.value}"
            text_email.value = f"{input_email.value}"
            text_salario.value = f"R$ {input_salario.value}"
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Exibir nome",
                        ),
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario,
                    ]
                )
            )


    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()
flet.run(main)