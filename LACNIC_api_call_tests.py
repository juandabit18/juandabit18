{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Coinmarket_api_call.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMLRXbVQ+Q9I8xc983Dea72",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/juandabit18/juandabit18/blob/main/LACNIC_api_call_tests.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q93K5OmoJNi8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 273
        },
        "outputId": "06f3d1cd-81c2-422f-be06-ad9772f43875"
      },
      "source": [
        "#!/usr/bin/python3\n",
        "\n",
        "import requests\n",
        "import json\n",
        "\n",
        "username = \"juan.jimenez@sencinet.com\"\n",
        "password = \"3jPH6@P%K\"\n",
        "client_id = \"I4f1lFI2mJyr6pT5FQLxif8OTvXHPR5w\"\n",
        "client_secret = \"6z_2PV7UUKI-880Ok2QixRAcbkFVlK0NhIEomT0hQXZZw0Ffq-jKXKYa4qMClS88\"\n",
        "\n",
        "from oauthlib.oauth2 import LegacyApplicationClient\n",
        "from requests_oauthlib import OAuth2Session\n",
        "\n",
        "oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))\n",
        "token = oauth.fetch_token(\n",
        "        token_url='https://dev-demolacnic.auth0.com/oauth/token',\n",
        "        username=username, password=password, client_id=client_id,\n",
        "        client_secret=client_secret, scope=\"asn:info org:info ip:info\"\n",
        ")\n",
        "\n",
        "bearermastoken = token[\"token_type\"]+\" \"+token[\"access_token\"]\n",
        "\n",
        "headers = {\n",
        "    \"accept\": \"application/json\",\n",
        "    \"authorization\": bearermastoken\n",
        "}\n",
        "\n",
        "\"\"\" Orginization GET request \"\"\"\n",
        "\n",
        "orgs = {\n",
        "    1: \"CO-COCO24-LACNIC\",\n",
        "    2: \"AR-CASA2-LACNIC\",\n",
        "    3: \"VE-COVE4-LACNIC\"\n",
        "}\n",
        "\n",
        "sel_orgs = int(input(\"\"\"\n",
        "\n",
        "Select Organization id (1 or 2 or 3):\n",
        "    1: CO-COCO24-LACNIC\n",
        "    2: AR-CASA2-LACNIC\n",
        "    3: VE-COVE4-LACNIC1\n",
        "\"\"\"\n",
        "    )\n",
        ")\n",
        "\n",
        "#for x in orgs:\n",
        "response = requests.get(\"https://registro-demo.api.lacnic.net/lacnic/1.0/entity/organizations/\"+orgs[sel_orgs], headers=headers)\n",
        "\n",
        "r_json = response.json()\n",
        "\n",
        "#r_str = json.dumps(r_json, indent=2)\n",
        "r_orgId = r_json[\"orgId\"]\n",
        "r_name = r_json[\"name\"]\n",
        "r_responsible = r_json[\"responsible\"]\n",
        "r_admin_contact = r_json[\"admin_contact\"]\n",
        "r_cob_contact = r_json[\"cob_contact\"]\n",
        "r_mem_contact = r_json[\"mem_contact\"]\n",
        "print(r_orgId)\n",
        "print(r_name)\n",
        "print(r_responsible)\n",
        "print(r_admin_contact)\n",
        "print(r_cob_contact)\n",
        "print(r_mem_contact)\n",
        "print()\n",
        "\n",
        "\"\"\" IPs request \"\"\"\n",
        "\n",
        "# colombia = []\n",
        "# argentina = []\n",
        "# venezuela = []\n",
        "\n",
        "# with open(\"sample_data/ipv4_prefixes.txt\") as f:\n",
        "#     for prefix in f.read().splitlines():\n",
        "#         prefix_str = str(prefix)\n",
        "#         print(prefix_str)\n",
        "\n",
        "#         response = requests.get(\"https://registro-demo.api.lacnic.net/lacnic/1.0/ips/\"+\n",
        "#                                 prefix_str,\n",
        "#                                 headers=headers)\n",
        "\n",
        "#         r_json = response.json()\n",
        "\n",
        "#         r_str = json.dumps(r_json, indent=2)\n",
        "\n",
        "#         r_orgId = r_json[\"orgId\"]\n",
        "\n",
        "#         if r_json[\"orgId\"] == \"CO-COCO24-LACNIC\":\n",
        "#             colombia.append(prefix_str)\n",
        "#         elif r_json[\"orgId\"] == \"AR-CASA2-LACNIC\":\n",
        "#             argentina.append(prefix_str)\n",
        "#         elif r_json[\"orgId\"] == \"VE-COVE4-LACNIC1\":\n",
        "#             venezuela.append(prefix_str)\n",
        "\n",
        "# print(\"Colombia: {}\".format(colombia))\n",
        "# print(\"Argentina: {}\".format(argentina))\n",
        "# print(\"Venezuela: {}\".format(venezuela))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "\n",
            "Select Organization id (1 or 2 or 3):\n",
            "    1: CO-COCO24-LACNIC\n",
            "    2: AR-CASA2-LACNIC\n",
            "    3: VE-COVE4-LACNIC1\n",
            "2\n",
            "AR-CASA2-LACNIC\n",
            "BT Latam Argentina\n",
            "\n",
            "JFJ12\n",
            "JFJ12\n",
            "JFJ12\n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "' IPs request '"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    }
  ]
}