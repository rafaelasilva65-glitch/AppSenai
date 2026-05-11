import asyncio
from calendar import leapdays

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, Card, Container, Row

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_personagens():
        list_view.controls.clear()

        lista_dados1 = get_personagens()

        for item in lista_dados1["items"]:
            # Usando ListTile dentro do Card para manter a estrutura de leading/title
            list_view.controls.append(
                Card(
                    content=Container(
                        height=120,
                        padding=10,
                        bgcolor=Colors.BLUE_50,
                        content=Row([

                            Image(src=item["image"], width=60),
                            Column([
                                Text(item["name"], weight=FontWeight.BOLD, color=Colors.BLUE_900),
                                Text(item["ki"], size=11, weight=FontWeight.BOLD),
                                Text(item["maxKi"], size=11, weight=FontWeight.BOLD),
                                Text(item["gender"], size=11, weight=FontWeight.BOLD),
                                Text(item["race"], max_lines=2, overflow=TextOverflow.ELLIPSIS,
                                     color=Colors.BLACK),
                            ], expand=True) # expand para o texto não quebrar o layout

                        ])
                    )
                )
            )
        print("Fazer")
        # TODO: Montar a lista de personagens do seu jeito, capricha ein

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=item["image"], width=60),
                    title=Text(item["name"], weight=FontWeight.BOLD, color=Colors.BLUE_900),
                    subtitle=Text(item["description"], max_lines=2, overflow=TextOverflow.ELLIPSIS, color=Colors.GREY),
                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():
        # carrega a primeira lista
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
                    list_view,
                ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)