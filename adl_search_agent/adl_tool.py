from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset

from fastapi.openapi.models import OAuth2
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.openapi.models import OAuthFlows
from google.adk.auth import AuthCredential
from google.adk.auth import AuthCredentialTypes
from google.adk.auth import OAuth2Auth
import os

auth_scheme = OAuth2(
    flows=OAuthFlows(
        authorizationCode=OAuthFlowAuthorizationCode(
            authorizationUrl="https://accounts.google.com/o/oauth2/auth",
            tokenUrl="https://oauth2.googleapis.com/token",
            scopes={
                "https://www.googleapis.com/auth/bigquery": "bigquery scope"  #Replace with correct scope
            },
        )
    )
)

auth_credential = AuthCredential(
    auth_type=AuthCredentialTypes.OAUTH2,
    oauth2=OAuth2Auth(
        client_id=os.getenv("CLIENT_ID", "YOUR_CLIENT_ID"), #Replace with client_id
        client_secret=os.getenv("CLIENT_SECRET", "YOUR_CLIENT_SECRET") #Replace with client_secret
    ),
)

adl_connector_tool = ApplicationIntegrationToolset(

   project="wipro-appinteg-prod", #Replace with GCP project of the connection

   location="asia-south1", #Replace with location of the connection

   connection="synapse-connection", #Replace with connection name

   auth_scheme=auth_scheme,

   auth_credential=auth_credential,

   entity_operations={
        "TA_LHD": ["GET", "LIST"], 
        "L2O_Winloss_Data": ["GET", "LIST"]
    },

   tool_name_prefix="adl_tool",

   actions=["ExecuteCustomQuery"],

   tool_instructions="""
    **ADL Database Schema Reference**
    Use 'ExecuteCustomQuery' for complex analysis involving filtering or aggregation.
    
    1. **TA_LHD (Hiring Data)**:
       - **Identity**: candidate_name, n_resume_number, emp_id, person_gender.
       - **Lifecycle**: indent_status, screening_date, offer_released, joining_date (Use for TAT).
       - **Org**: smu, sector, division, bu_du, derived_du_practice.
       - **Location**: joiningloc, country, zone.
       - **Grain**: Row per candidate.
    
    2. **L2O_Winloss_Data (Sales Data)**:
       - **Ownership**: opportunityid, opportunity_name, account, sap_customer_name.
       - **Status**: stage, status, won_lost_stage.
       - **Financials**: 
          * Primary Value: 'netsltcv_usd' (Total Contract Value).
          * Annual Value: 'netslacv_usd'.
          * Secondary: acv_in_dollar_planned, tcv_in_dollar_planned.
       - **Reasoning**: win_loss_1_reason, main_reason_for_ending_sales_cycle.
       - **Grain**: Row per opportunity.
    
    **Query Rules**:
    - Use full table paths: [Model].[TA_LHD] or [Model].[L2O_Winloss_Data].
    - For revenue questions, default to 'netsltcv_usd'.
    """

)
