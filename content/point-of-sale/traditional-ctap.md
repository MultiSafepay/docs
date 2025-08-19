---
title: Traditional (CTAP) terminal
category:
  uri: Point-of-sale
slug: traditional-ctap-terminal
position: 1
privacy:
  view: public
---
We currently offer this product in the Netherlands and Belgium.

If you are interested in our Point of Sale solutions, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

***

Traditional (CTAP) is a terminal that has passed <a href="https://wp.acquiris.eu/" target="_blank">Acquiris</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> certification and can be connected to acquirers with a C-TAP host.

# Prerequisites

To process payments, you will need:

* A [MultiSafepay account](/docs/getting-started-guide/)
* A traditional (CTAP) terminal

# Activation

To activate a traditional (CTAP) terminal, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. Go to **Devices** > **Terminals**.
3. Click **Add terminal**.
4. Below the **Group**, select a terminal group or click **Add in new group**. To learn more about how to create terminal groups, see User guide - [How to create a terminal group](/activation#how-to-create-a-terminal-group).
5. Select Terminal type **Traditional**. A unique Terminal ID will be automatically generated.\
   **💡 Tip!** As long as the terminal is not bound, you can modify the **TID** manually via **Devices** > **Terminals** > **Edit**. The name can still be modified after linking the device.
6. Copy the **Terminal ID**, **Account ID**, and **CTAP Acquirer** and send them to your POS provider.
7. After your POS provider has set up your terminal, the activation is completed.
8. Terminal manufacturer and serial number are now displayed in your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

✅ Success! You have successfully activated your terminal. You can now start accepting payments.

# User guide

## Terminal groups

A terminal group is required for linking and activating a CTAP device. You can create a single group or multiple groups for segmentation. Each terminal group is assigned a unique **API key** and **ID**. All transactions processed by terminals within the same terminal group are consolidated under a single reconciliation history.

This functionality offers reconciliation, reporting and management for single and multiple terminal groups.

### How to create a terminal group

To create a terminal group:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a>.
2. Go to **Devices** > **Terminals**.
3. Click **Manage groups**.
4. Click **+ Add new group**.
5. Insert a name for your group, and optionally, a [logo](activation/user-guide#how-to-upload-your-logo) to enable branding, and a [Webhook](doc:webhook) URL to receive updates for your payments.
6. Click **Create**.

Your new terminal group will be added to the **Manage groups** list. A terminal group ID and an API key will be associated.

To view the ID and API key for a terminal group:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a>.
2. Go to **Devices** > **Terminals**.
3. Click on **Manage groups**.
4. A list of all available terminal groups will be displayed, showing the ID and API key for each group.

### How to edit a group

1. At **Manage groups** click the **edit** icon on the right side of the panel to edit the desired terminal group. Here, you can:

* Change the **name** of the terminal group.
* Change the logo by selecting a different image file.\
  **⚠️Note:** Logos are not supported for Traditional terminals.
* Change the **webhook URL**.

2. Click **Save💾**

**💡 Tip!** You can view your API key via **Manage groups** > **API key**.

## Refunds

<details id="refunds">
  <summary>How to process refunds</summary>

  <br />

  **Via the API**

  See API reference – [Refund order](/reference/refundorder).

  **In your dashboard**

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
  2. Go to **Transactions** > **Transaction overview**, and click the relevant transaction.
  3. On the **Transaction details** page, click **Refund order**.
  4. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
  5. In the **Comment** field, enter any additional information.
  6. In the **Amount** fields, enter the amount to refund.
  7. Click **Continue**.
  8. Review **Refund confirmation**, and then click **Confirm**.
</details>

## Updates

To get updates on a specific order, make a [Get order](/reference/getorder/) request using the `{order_id}`.

## Testing

You cannot test terminals in your MultiSafepay test account.

<br />

[Top of page](#)
