import dash
from dash import html
from dash import dcc, Input, Output

# Importa as páginas
from pages import home, contato
from . import sobre

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

# Define o layout principal com links de navegação
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Componente de localização da URL
    html.Div([
        dcc.Link('Página Inicial', href='/'),
        html.Br(),
        dcc.Link('Sobre', href='/sobre'),
        html.Br(),
        dcc.Link('Contato', href='/contato'),
    ]),
    html.Div(id='page-content')  # Onde o conteúdo das páginas será mostrado
])

# Callback para renderizar o conteúdo da página conforme a URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/sobre':
        return sobre.layout
    elif pathname == '/contato':
        return contato.layout
    else:
        return home.layout

# Executa o servidor
if __name__ == "__main__":
    app.run_server(debug=True)
