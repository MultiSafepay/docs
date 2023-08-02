---
title: 'Traditional (CTAP) terminal'
category: 6477597e0e2961004638cd5d
order: 1
hidden: false
slug: 'traditional-ctap-terminal'

---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in the following countries:
> 
> - Netherlands
> 
> Please note that in this stage, you cannot request terminals yet to use POS services.  
> If you are interested in participating in the next stage of our pilot, email <sales@multisafepay.com>

Traditional (CTAP) is a terminal that has passed <a href="https://wp.acquiris.eu/" target="_blank">Acquiris </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> certification and can be connected to acquirers with a C-TAP host.

# Prerequisites

 To process payments, you will need:

- A [MultiSafepay account](/docs/getting-started-guide/)
- A traditional (CTAP) terminal

# Activation

 To activate a traditional (CTAP) terminal, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Devices** > **Terminals**.
3. Select **Add Traditional (CTAP)**.
4. On the **New Traditional (CTAP)** tab >  select **Add new group**.
5. Fill out the following fields:
- **New group name**.
- **Terminal name**.
- In the **MCC** field, click the **drop-down**  icon and then select the relevant MCC code.
6. Select **Create**.
7. Copy **Terminal ID**, **Account ID**, and **CTAP Acquirer** and send them to your POS provider.
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

## Updates

To get updates on a specific order, make a [Get order](/reference/getorder/) request using the `order_id`.

## Testing

You cannot test terminals in your MultiSafepay test account.

<br>

[Top of page](#)