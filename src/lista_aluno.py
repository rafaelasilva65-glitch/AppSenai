import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, FloatingActionButton, Icons, \
    ListView, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, dropdown, Row


class Pessoa:
    def __init__(self, nome, idade, data_nascimento, ano_atual, genero):
        self.nome = nome
        self.genero = None

def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    def navegar(route):
        asyncio.create_task(page.push_route(route))

    def ver_detalhes():
        text_nome.value = input_nome.value
        text_idade.value = input_idade.value
        text_data_nascimento.value = input_data_nascimento.value
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

        if input_data_nascimento.value:
            input_data_nascimento.error = None
        else:
            tem_erro = True
            input_data_nascimento.error = "Campo obrigatorio"

        if input_ano_atual.value:
            input_ano_atual.error = None
        else:
            tem_erro = True
            input_ano_atual.error = "Campo obrigatorio"


        if not tem_erro:
            input_nome.value = ""
            input_idade.value = ""
            input_data_nascimento.value = ""
            input_ano_atual.value = ""
            navegar("/ver_detalhes")

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            # Lógica para mudar o ícone dependendo do gênero
            icone_genero = Icons.PERSON  # Padrão
            if item["genero"] == "Masculino":
                icone_genero = Icons.MAN
            elif item["genero"] == "Feminino":
                icone_genero = Icons.WOMAN

            list_view.controls.append(
                ListTile(
                    leading=Icon(icone_genero),  # Usa o ícone definido acima
                    title=Text(item["nome"]),
                    subtitle=Text(f" {item['ano atual']}"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda ver_detalhes:  navegar("/ver_detalhes")),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda _, i=item: excluir(i)),
                        ]
                    )
                )
            )
        page.update()

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value.strip()
        idade = input_idade.value.strip()
        data_nascimento = input_data_nascimento.value
        ano_atual = input_ano_atual.value.strip()
        genero = input_genero.value  # Pega o valor do Dropdown

        if nome and idade and data_nascimento and ano_atual and genero:
            # Salva nome, profissão e gênero no dicionário
            lista_dados.append({
                "nome": nome,
                "idade": idade,
                "data de nascimento": data_nascimento,
                "ano atual": ano_atual,
                "genero": genero
            })

            # Limpa os campos
            input_nome.value = ""
            input_idade.value = ""
            input_data_nascimento.value = ""
            input_ano_atual.value = ""
            input_genero.value = None

            montar_lista_padrao()
            navegar("/lista_padrao")
        else:
            if not nome: input_nome.error_text = "campo obrigatório"
            if not idade: input_idade.error_text = "campo obrigatório"
            if not data_nascimento: input_data_nascimento.error_text = "campo obrigatório"
            if not ano_atual: input_ano_atual.error_text = "campo obrigatório"
            if not genero: input_genero.error_text = "selecione um gênero"

        page.update()

    def route_change():
        page.views.clear()
        page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(title="Lista de Alunos"),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda _: navegar("/form_cadastro")
                    )
                )
            )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(title="Formulário de cadastro"),
                        input_nome,
                        input_idade,
                        input_data_nascimento,
                        input_ano_atual,
                        input_genero,  # Adiciona o seletor na tela
                        btn_salvar
                    ]
                )
            )


        elif page.route == "/ver_detalhes":
            page.views.append(
            View(
                route="/ver_detalhes",
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
                        text_data_nascimento
                    ]),

                    Row([
                        Icon(Icons.NUMBERS, color=Colors.PRIMARY, size=20),
                        text_ano_atual
                    ]),

                    Row([
                        Icon(Icons.PERSON, color=Colors.PRIMARY, size=20),
                        text_genero
                    ])
                ]
            )
        )

    page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            page.update()

    # componentes
    text_nome = Text()
    text_idade = Text()
    text_data_nascimento = Text()
    text_ano_atual = Text()
    text_genero = Text()
    input_nome = TextField(label="Nome", hint_text="Digite seu nome")
    input_idade = TextField(label="Idade", hint_text="Digite sua idade")
    input_data_nascimento = TextField(label="Data de nascimento", hint_text="Digite sua data de nascimento")
    input_ano_atual = TextField(label="Ano escolar atual", hint_text="Digite o seu ano atual")

    # Dropdown para selecionar o gênero
    input_genero = Dropdown(
        label="Gênero",
        hint_text="Escolha o gênero",
        options=[
            dropdown.Option("Masculino"),
            dropdown.Option("Feminino"),
            dropdown.Option("Outro"),
        ],
    )

    list_view = ListView(height=500)
    btn_salvar = Button("Salvar", width=400, on_click=lambda _: salvar_dados())

    # eventos
    page.on_route_change = lambda _: route_change()
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
