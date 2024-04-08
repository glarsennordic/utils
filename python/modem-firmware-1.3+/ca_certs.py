#!/usr/bin/env python3
#
# Copyright (c) 2023 Nordic Semiconductor ASA
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause

# Amazon Root CA 1 for connection to nRF Cloud: MQTT, REST, file downloads
aws_ca  = """-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
"""

# nRF Cloud CoAP CA (coap.nrfcloud.com)
nrf_cloud_coap_ca = """-----BEGIN CERTIFICATE-----
MIIBjzCCATagAwIBAgIUOEakGUS/7BfSlprkly7UK43ZAwowCgYIKoZIzj0EAwIw
FDESMBAGA1UEAwwJblJGIENsb3VkMB4XDTIzMDUyNDEyMzUzMloXDTQ4MTIzMDEy
MzUzMlowFDESMBAGA1UEAwwJblJGIENsb3VkMFkwEwYHKoZIzj0CAQYIKoZIzj0D
AQcDQgAEPVmJXT4TA1ljMcbPH0hxlzMDiPX73FHsdGM/6mqAwq9m2Nunr5/gTQQF
MBUZJaQ/rUycLmrT8i+NZ0f/OzoFsKNmMGQwHQYDVR0OBBYEFGusC7QaV825v0Ci
qEv2m1HhiScSMB8GA1UdIwQYMBaAFGusC7QaV825v0CiqEv2m1HhiScSMBIGA1Ud
EwEB/wQIMAYBAf8CAQAwDgYDVR0PAQH/BAQDAgGGMAoGCCqGSM49BAMCA0cAMEQC
IH/C3yf5aNFSFlm44CoP5P8L9aW/5woNrzN/kU5I+H38AiAwiHYlPclp25LgY8e2
n7e2W/H1LXJ7S3ENDBwKUF4qyw==
-----END CERTIFICATE-----
"""

# nRF Cloud CoAP CA (dev)
nrf_cloud_coap_ca_dev = """-----BEGIN CERTIFICATE-----
MIIBmzCCAUKgAwIBAgIUOdcovsGv94HR18N97qIgq6mfyXowCgYIKoZIzj0EAwIw
GjEYMBYGA1UEAwwPblJGIENsb3VkIC0gRGV2MB4XDTIzMDMzMTEyMTM1NVoXDTQ4
MTIzMTEyMTM1NVowGjEYMBYGA1UEAwwPblJGIENsb3VkIC0gRGV2MFkwEwYHKoZI
zj0CAQYIKoZIzj0DAQcDQgAEsWwBJY6XL1tD+3qs62oHPzIR+gxAd2suL38kvJWP
rxeEJjDqUBP2+UvAMpDuChG/aQ3x5bw9enFlN1EUJaJrt6NmMGQwHQYDVR0OBBYE
FHJV6uiRFXRDMrIejIAbDRUkF2CAMB8GA1UdIwQYMBaAFHJV6uiRFXRDMrIejIAb
DRUkF2CAMBIGA1UdEwEB/wQIMAYBAf8CAQAwDgYDVR0PAQH/BAQDAgGGMAoGCCqG
SM49BAMCA0cAMEQCIDJdB0q6IVTSMBJCjgrdqsazeUbkxWG019X/yJTQyd2QAiA8
AmLG/0x09X2Qm+30MgNxOE4BiybZuwH9NF8KQVqQlg==
-----END CERTIFICATE-----
"""

# nRF Cloud CoAP CA (beta)
nrf_cloud_coap_ca_beta = """-----BEGIN CERTIFICATE-----
MIIBnzCCAUSgAwIBAgIUWfE1+Lh4L1RP15WBkwINIgLZgtIwCgYIKoZIzj0EAwIw
GzEZMBcGA1UEAwwQblJGIENsb3VkIC0gQmV0YTAeFw0yMzA1MDgwODI4MDdaFw00
ODEyMzEwODI4MDdaMBsxGTAXBgNVBAMMEG5SRiBDbG91ZCAtIEJldGEwWTATBgcq
hkjOPQIBBggqhkjOPQMBBwNCAARvM7cUr6xL9C992usqvq6aH+LLNbG6IWoiOYBo
QJEHnFo0Zb6sIwBWPJUj/DhQxu73/oCF6IAcv5yDdXJBl0fBo2YwZDAdBgNVHQ4E
FgQUt7i3/I+0fTq7gaFSKfxkV2wpiv0wHwYDVR0jBBgwFoAUt7i3/I+0fTq7gaFS
KfxkV2wpiv0wEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwCgYI
KoZIzj0EAwIDSQAwRgIhAMDbNg4llzbBpmCKHu7Vv0WtyQnEwWbEr5eRhtX33O4a
AiEA7sD3ABtaQa4df/uhnytbO5W2Qf8YfHtZLsrWmPKKR5w=
-----END CERTIFICATE-----
"""

def get_ca_certs(coap=False, stage="prod"):
    if not coap:
        return aws_ca

    if stage == "dev":
        return nrf_cloud_coap_ca_dev + aws_ca
    if stage == "beta":
        return nrf_cloud_coap_ca_beta + aws_ca

    return nrf_cloud_coap_ca + aws_ca