import dash_bootstrap_components as dbc
import dash_html_components as html

from app import dapp


def banner():
    banner = dbc.Nav([
        html.Div(html.Img(src=dapp.get_asset_url("Flowhub_Logo_Icon.svg"), style={'height': '1.5rem'}),
                 className='ml-2 mr-4 py-1'),
        html.Div(['Data Monitoring Dashboard'], className='p-2'),
    ], className='banner p-2')
    return banner


def navbar(current_page):
    if 'mapping' in current_page:
        mapping_disabled = False
        mapping_active = True
    else:
        mapping_disabled = True
        mapping_active = False
    navbar = dbc.Nav([
        dbc.NavItem(dbc.NavLink("Status Page", active=True, href="/status", className='px-2')),
        dbc.NavItem(dbc.NavLink("Location Analysis", active=True, href="/locationAnalysis", className='px-2')),
        dbc.NavItem(dbc.NavLink("Collection Detail", active=True, href="/locationsDetail", className='px-2')),

    ])
    return navbar
