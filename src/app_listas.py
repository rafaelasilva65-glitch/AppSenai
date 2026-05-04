import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, Column, \
    Row, Icon, ListTile, PopupMenuButton, PopupMenuItem


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de lista"
    page.theme_mode = ThemeMode.DARK # ou ThemeMode Light
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                            Icon(Icons.PERSON),
                            Text(item)
                    ],
                    margin=8
                    ),
                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.PERSON),
                    title=item,
                    subtitle="Subtitulo",
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao(),

    def salvar_dados():
        nome = input_nome.value.strip()

        if nome:
            lista_dados.append(nome)
            input_nome.error = None
            input_nome.value = ""
        else:
            input_nome.error = "Campo obrigatorio"

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Exemplos de listas",
                        bgcolor=Colors.CYAN_700
                    ),
                    Button("Lista de texto", on_click= lambda: navegar("/lista_texto")),
                    Button("Lista de card", on_click= lambda: navegar("/lista_card")),
                    Button("Lista padrão Android", on_click= lambda: navegar("/lista_padrao")),
                ]
            )
        )
        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(
                            title="Lista de Texto",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_card":
            page.views.append(
                View(
                    route="/listar_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de Card",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="Lista Padrão Android",
                        ),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda : navegar("/form-cadastro"),
                    )
                )
            )

        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        btn_salvar,
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
    input_nome = TextField(label="Nome", hint_text="Digite seu nome", on_submit=salvar_dados)

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)
    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()
flet.run(main)