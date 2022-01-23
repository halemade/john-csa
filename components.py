import dash_bootstrap_components as dbc
from dash import html

first_name = html.Div(
    [
        dbc.Label("First Name", html_for="example-email"),
        dbc.Input(id="fname", placeholder="Enter first name"),
        # dbc.FormText(
        #     "Are you on email? You simply have to be these days",
        #     color="secondary",
        # ),
    ],
    className="mb-3",
)

last_name = html.Div(
    [
        dbc.Label("Last Name", html_for="example-password"),
        dbc.Input(
            # type="password",
            id="lname",
            placeholder="Enter last name",
        ),
        # dbc.FormText(
        #     "A password stops mean people taking your stuff", color="secondary"
        # ),
    ],
    className="mb-3",
)

employee_id = html.Div(
    [
        dbc.Label("Employee Id", html_for="example-password"),
        dbc.Input(
            # type="password",
            id="employee-id",
            placeholder="Enter Employee ID",
        ),
        # dbc.FormText(
        #     "A password stops mean people taking your stuff", color="secondary"
        # ),
    ],
    className="mb-3",
)

check_button = dbc.Button("Check Eligibility",id='check-button', color="primary", size ='lg', className="me-1"),

form = dbc.Form([first_name, last_name, employee_id])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Check Eligibility", header=True),
                dbc.DropdownMenuItem("About the Farms", href="#"),
                dbc.DropdownMenuItem("About the Progam", href="#"),
                dbc.DropdownMenuItem("FAQ", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Center for Biomedical Ethics and Society",
    brand_href="#",
    color="secondary",
    dark=True,
)