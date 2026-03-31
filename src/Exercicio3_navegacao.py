import asyncio
import flet
import row
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton, FontWeight, Icons, Icon, Row


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK # ou ThemeMode Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    def cadastrar_aluno():
        text_nome.value = input_nome.value
        text_idade.value = input_idade.value
        text_ano_nascimento.value = input_ano_nascimento.value
        text_ano_atual.value = input_ano_atual.value

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_idade.value:
            input_idade.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_ano_nascimento.value:
            input_ano_nascimento.error = None
        else:
            tem_erro = True
            input_ano_nascimento.error = "Campo obrigatorio"

        if input_ano_atual.value:
            input_ano_atual.error = None
        else:
            tem_erro = True
            input_ano_atual.error = "Campo obrigatorio"


        if not tem_erro:
            input_nome.value = ""
            input_idade.value = ""
            input_ano_nascimento.value = ""
            input_ano_atual.value = ""
            navegar("/segunda_tela")

    # Componentes
    text_nome = Text()
    text_idade = Text()
    text_ano_nascimento = Text()
    text_ano_atual = Text()
    input_nome = TextField(label="Nome")
    input_idade = TextField(label="Idade")
    input_ano_nascimento = TextField(label="DD/MM/AAAA")
    input_ano_atual = TextField(label="Ano atual")



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
                        title="Cadastrar Aluno",
                        bgcolor=Colors.CYAN_700
                    ),

                    input_nome,
                    input_idade,
                    input_ano_nascimento,
                    input_ano_atual,



                    Button("Cadastra-se", on_click= cadastrar_aluno),
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Exibir nome",
                        ),
                        Row([
                            Icon(Icons.DRIVE_FILE_RENAME_OUTLINE, color=Colors.PRIMARY, size=20),
                            text_nome
                        ]),
                        Row([
                           Icon(Icons.NUMBERS, color=Colors.PRIMARY, size=20),
                            text_idade
                        ]),

                        Row([
                            Icon(Icons.DATE_RANGE, color=Colors.PRIMARY, size=20),
                            text_ano_nascimento
                        ]),

                        Row([
                            Icon(Icons.NUMBERS, color=Colors.PRIMARY, size=20),
                            text_ano_atual
                        ])
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