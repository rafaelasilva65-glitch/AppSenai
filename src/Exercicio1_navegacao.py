import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton, FontWeight


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK # ou ThemeMode Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    # Componentes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")


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
                    input_sobrenome,


                    Button("Salvar", on_click=lambda: navegar("/segunda_tela")),
                ]
            )
        )
        if page.route == "/segunda_tela":
            text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Exibir nome",
                        ),
                        text,
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