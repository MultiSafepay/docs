---
title: SmartPOS activation
category:
  uri: Point-of-sale
slug: smartpos-activation
parent:
  uri: smartpos-terminal
position: 2
privacy:
  view: public
---
We currently offer this product in the following countries:

<table>
  <tr>
    <td>Countries</td>
    <td>Netherlands, Belgium</td>
  </tr>

  <tr>
    <td>Countries for partners</td>
    <td>Netherlands, Belgium, Italy, Spain</td>
  </tr>
</table>

If you are interested in our Point of Sale solutions, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

***

SmartPOS is an advanced <Glossary>POS</Glossary> terminal with Android applications, providing added functionality. It enables you to make payments through various options, such as manual input flow, cloud POS payment, or third-party on-device applications.

# Prerequisites

To process payments, you will need:

* A [MultiSafepay account](/docs/getting-started-guide/)
* A SmartPOS terminal

# Activation

To activate a SmartPOS terminal, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
2. Go to **Devices** > **Terminals**.
3. Click **+ Add terminal**, then click **SmartPOS**.
4. Below the **Group**, select a terminal group or click **Add in new group**. To learn more about how to create terminal groups, see User guide - [How to create a terminal group](/activation#how-to-create-a-terminal-group).
5. Click **Create**.<br /> A **QR code** will appear on your screen.

Install the **MultiSafepay payment app** on your terminal to scan the **QR code**:

1. Turn on your terminal and install the MultiSafepay app from the **App Store**.
2. In the search field, enter **MultiSafepay** and select **MultiSafepay Payment app**.
3. Grant permission to the MultiSafepay app.<br /> A dialog with a QR scanner will appear.
4. Scan the QR code on your dashboard with your terminal.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/gifs/POS_animation_v2.gif" alt="Scan-QR" />

<br />

✅ Success! You have successfully activated your terminal. You can now start accepting payments.

**⚠️Note:** You can edit and link various terminals if you have already created a group.

***

# User guide

Check the settings available in your MultiSafepay dashboard below.

## Terminal groups

A terminal group is required for linking and activating a SmartPOS device. You can create a single group or multiple groups for segmentation. Each terminal group is assigned a unique **API key** and **ID**. All transactions processed by terminals within the same terminal group are consolidated under a single reconciliation history.

This functionality offers reconciliation, reporting and management for single and multiple terminal groups.

### How to create a terminal group

To create a terminal group:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a>.
2. Go to **Devices** > **Terminals**.
3. Click **Manage groups**.
4. Click **+ Add new group**.
5. Insert a name for your group, and optionally, a [logo](activation/user-guide#how-to-upload-your-logo) to enable branding, and a [Webhook](doc:webhook) URL to receive updates for your payments.
6. Click **Create**.

**⚠️Note:** Individual terminals within a same group cannot have different images. Add different terminal groups and add a logo for each group.

Your new terminal group will be added to the **Manage groups** list. A terminal group ID and an API key will be associated.

To view the ID and API key for a terminal group:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a>.
2. Go to **Devices** > **Terminals**.
3. Click on **Manage groups**.
4. A list of all available terminal groups will be displayed, showing the ID and API key for each group.

### How to edit a group

1. At **Manage groups** click the **edit** icon on the right side of the panel to edit the desired terminal group. Here, you can:

* Change the **name** of the terminal group.
* Change the logo by selecting a different image file.
* Change the **webhook URL**.

2. Click **Save💾**.

**💡 Tip!** You can view your API key via **Manage groups** > **API key**.

## How to upload your logo

1. Go to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
2. Go to **Settings** > **Files** and upload the desired image file. The file must meet the following requirements:

   * Format: **PNG**
   * Resolution: **512x512 pixels**

   You can upload multiple files at the same time.
3. Click **Upload** for single files or **Upload all** to upload all files.

[Top of page](#)
