---
title: 'Traditional (CTAP) terminal'
category: 6477597e0e2961004638cd5d
order: 1
hidden: false
slug: 'traditional-ctap-terminal'

---

> ⚠️ Note:
> 
> We currently offer this product in the following countries:
> 
> - Netherlands
> - Belgium 
>  
> If you are interested in our Point of Sale solutions, email <sales@multisafepay.com>

Traditional (CTAP) is a terminal that has passed <a href="https://wp.acquiris.eu/" target="_blank">Acquiris </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> certification and can be connected to acquirers with a C-TAP host.

# Prerequisites

 To process payments, you will need:

- A [MultiSafepay account](/docs/getting-started-guide/)
- A traditional (CTAP) terminal

# Activation

 To activate a traditional (CTAP) terminal, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Devices** > **Terminals**.
3. Click **Add terminal**.
4. Below the **<<glossary:group>> name**, click **Add new group**, or select a previously created group.
5. For a new group, out the following fields:
- **New group name**.  
- <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">**Webhook URL** </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>(optional).
- In the **Business category** field, click the **drop-down** icon and specify the relevant service or product offered. If a category has been assigned to your account in the past, it will be displayed automatically. 
6. Select Terminal type **CTAP**. A unique Terminal ID will be automatically generated.
**💡 Tip!** you can modify TID until manually via Devices > Terminals > TID until transactions are processed. The name can still be modified after processing transactions.
7. Copy **Terminal ID**, **Account ID**, and **CTAP Acquirer** and send them to your POS provider.
**💡 Tip!** As long as the terminal is not bound, the TID and name can be changed via the "Edit" icon.
8. After your POS provider has set up your terminal, the activation is completed.
9. Terminal manufacturer and serial number are now displayed in your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

✅ Success! You have successfully activated your terminal. You can now start accepting payments.

# User guide

## Refunds

<details id="refunds">

<summary>How to process refunds</summary>
<br>

**Via the API** 

See API reference – [Refund order](/reference/refundorder).

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and click the relevant transaction.
3. On the **Transaction details** page, click **Refund order**.
4. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
5. In the **Comment** field, enter any additional information.
6. In the **Amount** fields, enter the amount to refund. 
7. Click **Continue**.
8. Review **Refund confirmation**, and then click **Confirm**.

</details>

## Unreferenced refunds

Unreferenced refunds allow you to return funds to a customer without the need of an original transaction. This process is done from your CTAP terminal:

1. You initiate the refund by introducing the amount on the CTAP terminal.
2. The customer presents their card.
3. The card details are sent to MultiSafepay and forwarded to the card scheme for authorization. The authorization can be accepted or declined.
4. Once we receive an authorization response, we forward it to the terminal. The result will be displayed on the screen. 

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/diagrams/svg/ctap-unreferenced-refunds.svg" alt="web-app-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>

### Activation

To enable unreferenced refunds for your MultiSafepay account, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

### How it works

Once this feature has been activated for your account, you can start processing refunds on your terminal. The instructions vary from one terminal model to another.

***

## Updates

To get updates on a specific order, make a [Get order](/reference/getorder/) request using the `order_id`.

## Updates

To get updates on a specific order, make a [Get order](/reference/getorder/) request using the `order_id`.

## Testing

You cannot test terminals in your MultiSafepay test account.

<br>

[Top of page](#)