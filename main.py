import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import statistics as stats
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



#######################CARGAR LA BASE###############
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQpBusm-7fE7d_bJQQYgUq_sWHxbRc3rhva48_eh8vxYA9s5M5EjcFcyFr3VZ620Q/pub?output=csv'
df=pd.read_csv(url)

url2='https://docs.google.com/spreadsheets/d/e/2PACX-1vTRsVAq_5SGisQBZXkdJpv9DcWVLZwzyQDrmEihhd9doYYLPTKsCNFIo62Ojo9MXAeKUHr3_s26EcbB/pub?output=csv'
df2=pd.read_csv(url2)

url3='https://docs.google.com/spreadsheets/d/e/2PACX-1vT2ZkhX_wxekZxQ-mCb3KuRWvmjOxshMZO962yYLgqzyX6ACjLevOJOCoTmXvWlR6ZX5tjLv3KMZBKz/pub?output=csv'
df4=pd.read_csv(url3)
df4['Año']=df4['AÑO'].astype(str)

######################PREPARACIÓN DE TARJETAS###############
card_graph1 = dbc.Card(
        dcc.Graph(id='chart1', figure={}, style={'height':'300px'}), body=False, color="primary"
)

card_graph2 = dbc.Card(
        dcc.Graph(id='chart2', figure={}, style={'height':'300px'}), body=False, color="primary"
)

card_graph3 = dbc.Card(
        dcc.Graph(id='chart3', figure={}, style={'height':'300px'}), body=False, color="primary"
)

card_graph4 = dbc.Card(
        dcc.Graph(id='funnel_chart', figure={}, style={'height':'300px'}), body=False, color="primary")

card_graph5 = dbc.Card(
        dcc.Graph(id='histo', figure={}, style={'height':'300px'}), body=False, color="primary"
)

card_graph6 = dbc.Card(
        dcc.Graph(id='box', figure={}, style={'height':'300px'}), body=False, color="primary"
)
######################PREPARACIÓN DE TARJETAS###############

app.layout = html.Div([
    dbc.Row([
        html.Div([
            html.Img(src = "https://scontent.fbaq1-1.fna.fbcdn.net/v/t39.30808-6/305765312_494564586007774_402509305663101601_n.png?_nc_cat=107&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeHoYgTn2oMtWjExutqw4GS0SpWr4NCFEWBKlavg0IURYAtWuY2D1bITxZSX-7Vl26gQFxcvcvJXm7qANFQvv8pU&_nc_ohc=K_Iq3zQAID4AX-kZrQz&_nc_ht=scontent.fbaq1-1.fna&oh=00_AfDfZSy3KoqReav0NTLMjrt0WxF2MHLxT2WrFNUOAiPhVA&oe=6390B806", style = {'height': '120px'}),
            html.H6('Colegio La Enseñanza',style = {'color': 'Black'}),
        ],className='six.columns'),  

        dbc.Col(
            dcc.Dropdown(id = 'area',
            multi = False,
            clearable =False,
            disabled = False,
            style = {'display': True},
            value = 'PUNTAJE',
            placeholder = 'Seleccione área',
            options = [{'label': c, 'value': c} for c in df2['areas'].unique()],
            className = 'drop_down_list'),width=2
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Div(id='text1')
                ])
            ),width=2
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                     html.Div(id='text2')
                ])
            ),width=2
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Div(id='text3')
                ])
            ),width=2
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(id='text4')
                ])
            ),width=2
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Div(id='text5')
                ])
            ),width=2
        ),
    ],justify="center"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph1)
                ])
            ),width=4
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph2)
                ])
            ),width=4
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph4)
                ])
            ),width=4
        ),


    ]),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph3)
                ])
            ),width=4
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph5)
                ])
            ),width=4
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                html.Div(card_graph6)
                ])
            ),width=4
        ),


    ]),



])

######CALLBACKS
@app.callback(
    Output(component_id='text1', component_property='children'),
    Input(component_id='area', component_property='value')
)
def avg(choose):
    avera=round(stats.mean(df[choose]),2)
    return [            html.P('Promedio',
                   style = {
                       'color': 'Black',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),avera]


@app.callback(
    Output(component_id='text2', component_property='children'),
    Input(component_id='area', component_property='value')
)
def avg(choose2):
    avera2=round(stats.stdev(df[choose2]),2)
    return [html.P('Desviación',
                   style = {
                       'color': 'Black',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),avera2]

@app.callback(
    Output(component_id='text3', component_property='children'),
    Input(component_id='area', component_property='value')
)

def avg(choose3):
    avera3=round(stats.median(df[choose3]),2)
    return [html.P('Mediana',
                   style = {
                       'color': 'Black',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),avera3]

@app.callback(
    Output(component_id='text4', component_property='children'),
    Input(component_id='area', component_property='value')
)

def avg(choose4):
    avera4=round(np.percentile(df[choose4],25),2)
    return [html.P('Cuartil 1',
                   style = {
                       'color': 'Black',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),avera4]


@app.callback(
    Output(component_id='text5', component_property='children'),
    Input(component_id='area', component_property='value')
)

def avg(choose5):
    avera5=round(np.percentile(df[choose5],75),2)
    return [html.P('Cuartil 3',
                   style = {
                       'color': 'Black',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),avera5]

#######################GRÁFICAS######################3
@app.callback(
    Output(component_id='chart1', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def update_graph(mao):
    if mao=='PUNTAJE':
        df['Cat']=np.select([
            (df[mao]>0)&(df[mao]<=221),
            (df[mao]>221)&(df[mao]<=299),
            (df[mao]>300)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df3=df.groupby('Cat').agg({mao:'count'}).reset_index()
        fig = px.pie(df3, values=mao, names='Cat',hole=0.5)
        fig.update_traces(textposition='inside', textinfo='percent+label',showlegend=False)
        fig.update_layout({"title": {"text": 'Puntaje por desempeño',
                             "font": {"size": 15},"yanchor":"top",'x':0.5,"xanchor":"center"}})
        return fig

    else :

        df['Cat']=np.select([
        (df[mao]>=0)&(df[mao]<=44.2),
        (df[mao]>44.2)&(df[mao]<=65),
        (df[mao]>65)&(df[mao]<=87.4),
        (df[mao]>87.4)],['Insuficiente','Mínimo','Satisfactorio','Avanzado'])
        edad=['Insuficiente','Mínimo','Satisfactorio','Avanzado']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df3=df.groupby('Cat').agg({mao:'count'}).reset_index()
        fig = px.pie(df3, values=mao, names='Cat',hole=0.5)
        fig.update_traces(textposition='inside', textinfo='percent+label',showlegend=False)
        fig.update_layout({"title": {"text": 'Puntaje por desempeño',
                             "font": {"size": 15},"yanchor":"top",'x':0.5,"xanchor":"center"}})
        return fig

@app.callback(
    Output(component_id='chart2', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def barchat(dani):
    fig = px.bar(df4, x=dani, y="Año",title="Comparativo 2021-2022",text=dani)    
    return fig


@app.callback(
    Output(component_id='chart3', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def update_graph(lola):
    if lola=='PUNTAJE':
        df['Cat']=np.select([
            (df[lola]>0)&(df[lola]<=221),
            (df[lola]>221)&(df[lola]<=299),
            (df[lola]>=300)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df_prov=df.sort_values('PUNTAJE',ascending=True)
        df_prov['Puesto']=range(1,len(df_prov['PUNTAJE'])+1)
        df_prov['Desempeño']=df_prov['Cat'].astype(str)
        fig = px.scatter(df_prov, x="Puesto", y=lola, color='Desempeño',title='Dispersión desempeño')       

        return fig

    else :

        df['Cat']=np.select([
            (df[lola]>=0)&(df[lola]<=44.2),
            (df[lola]>44.2)&(df[lola]<=65),
            (df[lola]>65)&(df[lola]<=87.4),
            (df[lola]>87.4)],['Insuficiente','Mínimo','Satisfactorio','Avanzado'])
        edad=['Insuficiente','Mínimo','Satisfactorio','Avanzado']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df_prov=df.sort_values('PUNTAJE',ascending=True)
        df_prov['Puesto']=range(1,len(df_prov['PUNTAJE'])+1)
        df_prov['Desempeño']=df_prov['Cat'].astype(str)
        fig = px.scatter(df_prov, x="Puesto", y=lola, color='Desempeño',title='Dispersión desempeño') 


        return fig

@app.callback(
    Output(component_id='histo', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def euro(dad):
    fig = px.histogram(df, x=dad, histnorm='percent',labels={'count':'Porcentaje'},title='Distribución de puntajes')
    return fig

@app.callback(
    Output(component_id='box', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def euro(ariel):
    fig = px.box(df, x="CURSO", y=ariel, color="CURSO",title='Desempeño por curso')
    return fig

@app.callback(
    Output(component_id='funnel_chart', component_property='figure'),
    Input(component_id='area', component_property='value')
)

def update_graph(lola):
    if lola=='PUNTAJE':
        df['Cat']=np.select([
            (df[lola]>0)&(df[lola]<=221),
            (df[lola]>221)&(df[lola]<=299),
            (df[lola]>=300)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df_prov=df.sort_values('PUNTAJE',ascending=True)
        df_prov['Puesto']=range(1,len(df_prov['PUNTAJE'])+1)
        df_prov['Desempeño']=df_prov['Cat'].astype(str)
        d=df_prov.groupby('Cat').agg({'PUNTAJE':'count'}).reset_index()
        data = dict(number=list(d['PUNTAJE']),stage=list(d['Cat']))
        fig = px.funnel(data, x='number', y='stage',title='Desempeño por areas')
     

        return fig

    else :

        df['Cat']=np.select([
            (df[lola]>=0)&(df[lola]<=44.2),
            (df[lola]>44.2)&(df[lola]<=65),
            (df[lola]>65)&(df[lola]<=87.4),
            (df[lola]>87.4)],['Insuficiente','Mínimo','Satisfactorio','Avanzado'])
        edad=['Insuficiente','Mínimo','Satisfactorio','Avanzado']
        df['Cat']= pd.Categorical(df['Cat'], edad)
        df_prov=df.sort_values('PUNTAJE',ascending=True)
        df_prov['Puesto']=range(1,len(df_prov['PUNTAJE'])+1)
        df_prov['Desempeño']=df_prov['Cat'].astype(str)
        d=df_prov.groupby('Cat').agg({'PUNTAJE':'count'}).reset_index()
        data = dict(number=list(d['PUNTAJE']),stage=list(d['Cat']))
        fig = px.funnel(data, x='number', y='stage',title='Desempeño por areas')  


        return fig

#################################APLICACACION
if __name__ == "__main__":
    app.run_server(debug=True)















