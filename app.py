from dash import Dash, dcc, html, Input, Output
from home import layout as home_layout
from sobre import layout as sobre_layout

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Para implantar com serviços como o Heroku

# Layout principal
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback para alternar entre as páginas
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/sobre':
        return sobre_layout
    else:
        return home_layout  # Página inicial padrão

if __name__ == '__main__':
    app.run(debug=True)
