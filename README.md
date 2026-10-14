# ADL Search Agent

This repository contains instructions for interacting with the ADK (Agent Development Kit) agent.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites- Git Clone

Open Cloud Shell on Google Cloud Console and create a SSH Key file:

*   **Create a SSH Key file**:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@wipro.com"
    more ~/.ssh/id_rsa.pub
    ```
    **Copy this key on the SSM portal https://wipro-ge-567794993156.us-central1.sourcemanager.dev/user/settings/user-keys **:
### Installation

1.  **Clone the repository:**
    ```bash
    git clone git@wipro-ge-567794993156-ssh.us-central1.sourcemanager.dev:cloud-professional-services/adl-search-agent.git
    cd adl-search-agent
    ```
    You may need to approve the consent on the url thats shown in the clone output.And try cloning again.

2.  **Install dependencies (if any specific to this sample):**
    ```bash
        #Create virtual environment and activate it
        python -m venv .venv
        source .venv/bin/activate
        #install ADK
        pip install google-adk
        #verify ADK installation
        pip show google-adk
    ```

### Install UV

```bash
# Install uv 
curl -LsSf https://astral.sh/uv/install.sh | sh
# Install the package and dependencies.
uv sync
```

### Run the ADK Web locally

```bash
cd adl-search-agent
adk web .
```

### Deploy the ADK

```bash
uv sync --group deployment
uv run deployment/deploy.py --create.
```

### Update the ADK Agent

```bash
uv run deployment/deploy.py --update --resource_id=42411462018203648
```