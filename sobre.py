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
        html.H1("Gráficos"),
        html.Div([
            html.P("Somos uma equipe de desenvolvimento dedicada a criar soluções inovadoras para análise de dados."),
            html.P("Nosso projeto visa proporcionar uma plataforma intuitiva para visualização de informações complexas."),
        ]),
        html.Div([
            html.H2("Nossa Equipe"),
            html.P("Artur, Caio, Cassiel, Guilherme, João, Pedro e Yuri.")
        ]),
    ], className="main-content"),

    # Footer (rodapé)
    html.Footer([
        html.Span("Todos os direitos reservados ©"),
        html.Span(" Desenvolvido por: Artur, Caio, Cassiel, Guilherme, João, Pedro e Yuri")
    ], className="footer")
])
