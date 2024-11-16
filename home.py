from dash import html

layout = html.Div([

    # Header (cabeçalho)
    html.Header([
        html.Nav([
            html.Ul([
                html.Li(html.A("HOME", href="/")),
                html.Li(html.A("SOBRE", href="/sobre")),
            ]),
        ]),
    ], className="header"),

    # Main content (conteúdo principal)
    html.Main([
        html.H1("ANÁLISE DE DADOS"),
        html.Div(className="card", children=[
            html.Img(id="logo1", src="/assets/logo1.webp"),
            html.Div(className="txt", children=[
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit...")
            ])
        ]),
        html.Div(className="card", children=[
            html.Img(id="logo2", src="/assets/logo2.webp"),
            html.Div(className="txt", children=[
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit...")
            ])
        ]),
    ], className="main-content"),

    # Footer (rodapé)
    html.Footer([
        html.Span("Todos os direitos reservados ©"),
        html.Span(" Desenvolvido por: Artur, Caio, Cassiel, Guilherme, João, Pedro e Yuri")
    ], className="footer")
])
