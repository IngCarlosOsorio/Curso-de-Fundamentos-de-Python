@app.callback(Output('my_graph', 'figure'), [Input('DropdownMicroService', 'value')])
def update_graph(value):
    if not value:
        return {}

    df = get_df(value)
    if df.empty:
        return {}

    figBar = px.bar(
        data_frame=df,
        x='ApiController',
        y='StatusCode',
        labels={'ApiController': 'Nombre del controlador', 'StatusCode': 'Códgio de estado'}
    )
    return figBar