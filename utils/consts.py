import os

DEFAULT_PYTHON_IMAGE = "quay.io/modh/odh-generic-data-science-notebook:v3-20250117"
DEFAULT_TOOLBOX_IMAGE = "registry.redhat.io/ubi9/toolbox:9.5"
DEFAULT_OC_IMAGE = "registry.redhat.io/openshift4/ose-cli:v4.15.0"
DEFAULT_RHELAI_IMAGE = "registry.redhat.io/rhelai1/instructlab-nvidia-rhel9:1.3.2"

PYTHON_IMAGE = os.getenv("PYTHON_IMAGE", DEFAULT_PYTHON_IMAGE)
TOOLBOX_IMAGE = os.getenv("TOOLBOX_IMAGE", DEFAULT_TOOLBOX_IMAGE)
OC_IMAGE = os.getenv("OC_IMAGE", DEFAULT_OC_IMAGE)
RHELAI_IMAGE = os.getenv("RHELAI_IMAGE", DEFAULT_RHELAI_IMAGE)
