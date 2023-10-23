---
title: 'POS troubleshooting'
category: 6477597e0e2961004638cd5d
order: 4
hidden: false
slug: 'pos-troubleshooting'

---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in the following countries:
> 
> - Netherlands
> 
> Please note that in this stage, you cannot request terminals yet to use POS services.  
> If you are interested in participating in the next stage of our pilot, email <sales@multisafepay.com>

This page provides troubleshooting steps to resolve common issues.

# Connection

 The internet connection appears to be unstable or disconnected.

### Manage the internet connection

When the internet connection isn't working correctly: 

- Check if your Wi-Fi router is connected correctly and the network is stable.
- If the terminal is not connected to the Wi-Fi, see - [How to connect to Wi-Fi](/manage-my-account#how-to-connect-to-wi-fi).
- If the Wi-Fi is connected, check the color of the internet icon on your terminal.


[block:html]
{
  "html": "<table style=\"text-align:left;\">\n<tr>\n    <th>Connection color</th>\n    <th style=\"text-align:left;\">Description</th>\n  </tr>\n  <tr>\n  <td><img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/green-internet-signal.png\" width=\"35\" align =\"center\" style=\"padding: 5px;\"/> </td>\n   <td>The network connection good.</td>\n  </tr>\n  <tr>\n  <td><img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/red-internet-signal.png\" width=\"35\" align =\"center\"/> </td>\n <td>The terminal isn't working correctly. <br> For the P2 Smartpad terminal, connect to the connection cable and try again. <br>Improve the network connectivity.</td>\n  </tr>\n</table>\n\n"
}
[/block]
---

# Activation

The terminal is not correctly onboarded or linked with the correct group.

### Onboard the terminal

If you haven't activated your terminal, follow these steps: 

<details id="activate-terminal">
<summary>How to activate terminal</summary>

<br>

- [Traditional (CTAP) terminal](doc:traditional-ctap-terminal)
- [SmartPOS activation](doc:smartpos-activation)

If your SmartPOS terminal isn't onboarded correctly, email <pos-support@multisafepay.com>

</details>

***

### Incorrect API key

If you have used an incorrect API key for cloud payments, check for the correct API key in your dashboard. 

<details id="transactions">
<summary> How to retrieve API key</summary>

1. Sign in to your MultiSafepay dashboard.
2. Go to **Devices** > **Terminals**, and then click **Manage groups**.
3. In the **Manage groups** dialog, hover over the key icon.

</details>

***

### IPEK not configured

Before you begin activation, ensure that the Initial PIN Encrypted Key(IPEK) is registered on your terminal.

To check if IPEK is registered, turn on your terminal and click **Configured**.

If your IPEK is not configured, email <pos-support@multisafepay.com>

***

# Payment errors

The terminal isn't working correctly, payment information isn't displayed or payment is declined.

### Declined payment

If your payment is declined, check if you encountered any error messages.

| Error status | Solution |
| :---         | :---     |
| Configuration error. Try again | Send a request to  <pos-support@multisafepay.com> |
| Card not supported | Send a request to  <pos-support@multisafepay.com>|
| Use a different interface | Initiate the transaction again. <br>  Ask the customer to insert the card instead of doing a contactless payment. |

***

[Top of page](#)