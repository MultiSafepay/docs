---
title: 'POS troubleshooting'
category: 6477597e0e2961004638cd5d
order: 3
hidden: false
slug: 'pos-troubleshooting'

---

> ⚠️ Note:
> 
> We currently offer this product in the following countries:
> 
> - Netherlands
> - Belgium 
>  
> If you are interested in our Point of Sale solutions, email <sales@multisafepay.com>

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

## Onboard the terminal

If you haven't activated your terminal, follow these steps: 

<details id="activate-terminal">
<summary>How to activate terminal</summary>

<br>

- [Traditional (CTAP) terminal](doc:traditional-ctap-terminal)
- [SmartPOS activation](doc:smartpos-activation)

If your SmartPOS terminal isn't onboarded correctly, email <pos-support@multisafepay.com>

> **Note:**
>
> To help us resolve the issues faster, provide us with the following:
> - Account ID
> - Terminal serial number
> - Description of the issue
> - If available, pictures or video
>
</details>

***

## No **Devices** visible in Merchant dashboard 

If you cannot see the **Devices** section in your Merchant Dashboard yet

- check if your user has the correct permissions, or contact your administrator.
- contact us via support@multisafepay.com.

## MultiSafepay app not visible 

Apps need to be whitelisted in the Sunmi account linked to the device. 

## Incorrect API key

If you have used an incorrect API key for cloud payments, check for the correct API key in your dashboard. 

<details id="transactions">
<summary> How to retrieve API key</summary>

1. Sign in to your MultiSafepay dashboard.
2. Go to **Devices** > **Terminals**, and then click **Manage groups**.
3. In the **Manage groups** dialog, hover over the key icon.

</details>

***

## IPEK not configured

Before you begin activation, ensure that the Initial PIN Encrypted Key(IPEK) is registered on your terminal.

To check if IPEK is correctly registered, turn on your terminal and view the **Configured** field.

If your IPEK is **not** configured, you can 

- attempt manual configuration via **Settings** > Advanced > Security Center > Key Injection > RKI > Key Inject
- contact us via <pos-support@multisafepay.com> 


***
## Logs

Retrieving logs can be a helpful step to investigate an issue. You can generate them via your Sunmi portal:

- Go to Device > **Log task management**
- Clear _start time_
- Press **New task**
- Ensure to select **syslog** and add serial numbers
- Define the timeframe during which the logs should be uploaded to the portal and replicate the issue during this time. _Start time \_must be later than \_current time_. 
- Click **release**

***
# Payment errors

The terminal isn't working correctly, payment information isn't displayed or payment is declined.

## Order placed - not shown on terminal 

Checks you can do:

- Is the terminal connected to wifi?
- Did you use the correct API key for your terminal group? 

## Declined payment

If your payment is declined, check if you encountered any error messages.

| Error status | Solution |
| :---         | :---     |
| Configuration error. Try again | Send a request to  <pos-support@multisafepay.com> |
| Card not supported | Send a request to  <pos-support@multisafepay.com>|
| Use a different interface | Initiate the transaction again. <br>  Ask the customer to insert the card instead of doing a contactless payment. |
| 1000 card declined | Contact support@multisafepay.com to confirm payment method configuration. |
| Use Magstripe | Contact pos-support@multisafepay.com |

Additional check: ensure that you did not deactivate any card payment methods in your Merchant Dashboard.

> **Note:**
>
> To help us resolve POS issues faster, provide us with the following:
> - Account ID
> - Terminal serial number
> - Description of the issue
> - If available, pictures or video


# Errors in the display of the app / screen 

- Restart your terminal. 
- contact us via support@multisafepay.com

***
# Set device to developer mode

Note: once a device is converted to developer mode, it cannot be reverted. This means it will no longer be PCI compliant.

1. Request TUSN code from Sumni.
2. Navigate to Settings > System > About
3. Scroll down to the **TUSN** button 
4. Press the TUSN button 8 times (alternative: SV button)
5.  Enter the code received from Sunmi.  
   The 4-digit code is valid for 24 hours.


# Tampering alarm

If your device has been blocked due to the error on screen "Attacked! Please contact your service provider", you can reach out to Sunmi for support. 

1. On the <a href="https://www.sunmi.com/en-US/" target="_blank">Sunmi page</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, go to *Contact Technical Support* > Create new request.
2. Select **P Serial Tamper** and follow the steps in the Sunmi environment. 
**💡 Tip!** prepare a picture of your device to attach to the form. 
3. Depending on the error code, you will receive a code to unblock your device. 

Once the terminal is rebooted, the device is ready for use again. 
If the alarm reoccurs within a short time frame, a sensor might be damaged. You can contact us for assistance via [pos-support@multisafepay.com](mailto:pos@multisafepay.com).


# Send back a terminal

In specific cases it might be necessary to return a device to us for technical investigation, or hardware substitution.

(!) Note: Only return a terminal if requested by us. 

## Needed details

To ensure a quick and efficient return procedure, indicate the following: 

- MultiSafepay account ID  
- Serial number 
- Address for new terminal
- Reason for return 
- Support ticket reference (ex. 172349)

Send this information to [pos-support@multisafepay.com](mailto:pos@multisafepay.com).

## Reasons to return a terminal (temporarily)

- Display broken
- Keyboard broken
- Printer broken
- Scanner broken
- Battery not working/no power
- Payment issues (only send back on our request)
- Chip reader broken
- Hardware damage
- Network not working
- Account closure
- Wrong terminal ordered


***

[Top of page](#)