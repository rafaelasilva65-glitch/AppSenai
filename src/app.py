from datetime import date
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Number
from flet.controls.border_radius import horizontal


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

    def salvar_numero():
        try:
            numero = int(input_numero.value)
            tipo = "par" if numero % 2 == 0 else "impar"
            text1.value = f"O número {numero} é {tipo}"
        except ValueError:
            text1.value = "Por favor, digite um número valido"
        page.update()

    def verficar_idade():
        try:
            ano = int(input_ano.value)
            hoje = date.today().year
            idade = hoje - ano
            if idade < 18:
                text2.value = f'Você tem {idade} anos, é menor de idade'
            elif idade == 18 or idade > 18:
                text2.value = f'Você tem {idade} anos, é maior de idade'
        except ValueError:
            text.value = "Por favor, digite seu ano de nascimento"
        page.update()





    # Componentes
    text = Text()
    text1 = Text()
    text2 = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Número")
    input_ano = TextField(label="Ano")


    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_salvar1 = OutlinedButton("Salvar numero", on_click=salvar_numero)
    btn_salvar2 = OutlinedButton("Verificar idade", on_click=verficar_idade)


    # Construção da tela

    page.add(
         Column(
             [
                 input_nome,
                 input_sobrenome,
                 btn_salvar,
                 text,

                 input_numero,
                 btn_salvar1,
                 text1,

                 input_ano,
                 btn_salvar2,
                 text2
             ],
             width=400,
             horizontal_alignment=CrossAxisAlignment.CENTER
         )
    )


flet.app(main)