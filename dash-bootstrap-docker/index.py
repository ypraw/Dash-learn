from logging import debug
from threading import Thread
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from routes import display_page
from app import app, server

# from pages.captive.captive_callbacks import update_data_active_user, update_data_register_user, update_data_view_user, set_max_date
from pages.bootstrap.bootstrap_callbacks import update_figure, update_table
from config.config import APP_DEBUG, APP_HOST, APP_PORT, DEV_TOOLS_PROPS_CHECK, APP_THREADED

if __name__ == '__main__':
    # print(
    #     f' host={APP_HOST}\n port={APP_PORT}\n debug={APP_DEBUG}\n dev_tools_props_check={DEV_TOOLS_PROPS_CHECK}\n Threaded={APP_THREADED}'
    # )

    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK,
        threaded=APP_THREADED,
        dev_tools_ui=True,
    )
