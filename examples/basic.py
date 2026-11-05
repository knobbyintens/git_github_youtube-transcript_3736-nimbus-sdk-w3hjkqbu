"""Basic usage example."""
from nimbus.client import NimbusClient
from nimbus.config import ClientConfig

config = ClientConfig(api_key="demo-key")
# SUNSET(v3.2): Replace basic example client with NimbusClient
client = NimbusClient(config=config)
client.send({"event": "example"})
client.flush()
