---
title: SmartPOS features
category:
  uri: Point-of-sale
slug: smartpos-features
parent:
  uri: smartpos-terminal
position: 3
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

# Features

After activating your SmartPOS terminal, you can add features from your SmartPOS payment app. SmartPOS features contains:

<div className="settings-container" style={{display:'flex', alignItems:'flex-start', marginTop:'20px'}}>
  <div style={{marginRight: '80px'}}>
    <strong>Global Settings</strong>

    <ul>
      <br />

      <li>Display items after payment have been processed</li>
      <li>Add a tip to your payment flow</li>
      <li>Manually print a receipt</li>
      <li>Automatically print a receipt after a completed payment</li>
      <li>Hide the MultiSafepay logo</li>
    </ul>

    <strong>Payment Settings</strong>

    <ul>
      <br />

      <li>Insert an order ID (or Scan QR)</li>
      <li>Allow refunds</li>
      <li>Allow card authorization</li>
      <li>Initiate payments manually or using cloud mode</li>
      <li>Hide the navigation menu on the main screen</li>
      <li>Define the closing order flow</li>
      <li>Change your payment method</li>
    </ul>

    <strong>Navigation Settings</strong>

    <ul>
      <br />

      <li>Enable the Cancel function</li>
      <li>Hide navigation</li>
    </ul>
  </div>

  <div style={{flexShrink: '0'}}>
    {/* <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/img/POS_feature_list.png" alt="Feature list" width="220" /> */}
  </div>
</div>

{/* Add the following CSS styles */}

<HTMLBlock>{`
<style>
  @media (max-width: 480px) {
    .settings-container {
      flex-direction: column; /* Stacks items vertically on small screens */
      align-items: flex-start; /* Align items at the start */
    }
    .settings-container img {
      margin-top: 20px; /* Adds some space between the text and image */
    }
  }
</style>
`}</HTMLBlock>

To add payment flow features, follow these steps:

1. On the navigation menu, click the **Back** button.
2. Select **Settings**.

## How to enable display items

1. In the **Global settings** list, click the **Display items** toggle.
2. To return to the main screen, click the **Back** button.

Once you've initiated the payment, the items are displayed on the payment screen.

{/*  
  
 

 **Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-items-screen.png" alt="POS-display" width="250" style={{ display:'block' }}/>  
<br/>

***

*/}

## How to enable tipping

1. In the **Global settings** list, click the **Tipping** toggle.
2. To return to the main screen, click the  **Back** button.

Enabling this feature will display a tipping screen before the payment is processed. On the tipping screen, you can:

{/* **Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-tipping-screen.png" alt="smartPOS_print" width="250" style={{ display:'block' }}/>  
<br/>>>>>*/}

* Click a suggested tipping amount or click **Custom** to add a specific amount.
* Click **No Tip** to proceed without tipping.
* Click the **Employee** icon to assign the employee you want to tip or to add a new employee.

You can add an employee via **+ add employee** > Insert **Name** and **Employee ID**.

***

## How to enable manual print or email

1. In the **Global settings** list, click the **Print/Email** toggle.
2. To return to the main screen, click the **Back** button.

{/*  
  
 

 **Example:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-print-screen.png" alt="smartPOS_print" width="250" style={{display: 'block'}}/>
<br/>

***

*/}

***

## How to enable auto-print

Enabling this feature will print a receipt after each successful payment.

1. Go to **Features** > **Global settings**.
2. Click the **Auto-Print** toggle.
3. After completing a payment, the device will automatically print a receipt.

This feature is only available for devices with built-in printers.

## How to enable cloud mode

1. In the **Payment** list, click the **Cloud mode** toggle to the right.
2. To return to the main screen, click the **Back** button.

***

To exit the cloud mode payment screen:

1. Tap and hold your finger on the screen for a few seconds.
2. Enter the default **PIN code**. <br />The default PIN code is `1324`.

**⚠️ Note:** For your security, we recommend you change the default PIN code as soon as possible.

***

## How to define your closing order flow

Upon completed or declined payment, the customer can be redirected to a page that confirms the outcome of the payment process, OR go back automatically to your app.\
Example message on the confirmation screen: "Payment is completed successfully".

You can customize this flow:

1. Go to **Settings** > **Payment** > **Close timeout**
2. To display the confirmation screen for a fixed amount of time, select the seconds from the dropdown. This is the timeout of the "Completed" page.\
   If you select *disabled*, there is no automatic timeout, and you will need to press *Close Order* to close the confirmation screen and return to your own application.

**⚠️ Note:** This applies to both cloud mode and native application setups.

***

## How to enable additional payment methods

To activate additional payment methods for your terminal, email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com). Once activated:

1. Go to **Features** > **Payment**.
2. At **Additional Payment methods**, click **Reload**. The newly added payment methods will be available in the dropdown menu.
3. Click the **Dropdown** icon to display the payment methods.
4. Click the toggle to enable or disable the desired payment method.
5. Click **Back** to return to the main screen.

***

## How to change the PIN code

1. Go to **Settings** >  **Security**.
2. Enter the default PIN code.
3. Click **Change** and then enter your new PIN code.
4. Click ✔.

***

After you've enabled the **Cloud mode**, the **Navigation** list appears. This feature allows you to hide the cancel button and system navigation.

{/* 
**Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/SmartPOS-cloud-mode.png" alt="smartPOS_print" width="250" style={{ display:'block' }}/>  
<br/> 
*/}

## How to generate closing balance

You can generate a **closing balance** report at the end of each processing period to review a summary of total sales, broken down by payment method and including tips.

Via **Features** > **Closing balance**, you can set the following parameters:

* **Default date**: Today, yesterday or select day
* **Start hour**: The system will calculate 24 hours starting from the time you set. You must enter a value between 0 and 23.\
  Example: If **Start hour** is set to 10, the period begins at 10:00 AM and ends at 09:59 AM the next day.
* **Report level**: Company, Device group, Current device

Click **View** to display the details entered. These details will also appear on the header of the receipt.

**💡 Tip!** You can print your closing balance report using either the device printer, or the [external printer](/docs/smartpos-features#how-to-use-an-external-printer).

***

## How to hide navigation

1. In the **Navigation** list, click the **System navigation** toggle to the right.
2. To return to the main screen, click the **Back** button

**Note:** To access the navigation menu, tap and hold your finger on the screen for a few seconds and enter the PIN code.

***

## How to hide the MultiSafepay logo

1. Go to **Features** > **Global Settings**.
2. Click the **Hide MultiSafepay logo** toggle.
3. To return to the main screen, click the **Back** button.

**Note:** To enable this feature, you must first assign a company logo to your terminal group.

***

## How to switch languages

1. In the **Settings** section, go to **Languages**.
2. Select between English, Dutch, and Spanish.

***

## How to enable Order ID input: Manual entry and QR Code scan

Enabling this feature adds both manual order ID entry and QR code scanning functionality to the transaction process.

1. Go to **Features** > **Payment Settings**.
2. Click the **Insert order** toggle. Both options will be enabled.
3. On the **Manual Input** screen, choose one of the following methods:

* **Manual Order ID Entry**:
  * Click **Input Order ID** and enter the order ID.
  * The information retrieved will be included in the payment request.
* **Scan QR**:

  * A QR code must be generated using one of the following formats:
    * **String**: Contains only the Order ID.
    * **JSON**: Contains the Order ID, amount, and description of the order.
  * Click **Scan QR**.
  * Scan the QR code using the terminal's scanner or an external scanner.
  * Scanning the QR code will retrieve information based on the format in which the QR code has been generated.
  * This information will be included in the payment request.

  **⚠️Note:** The `order_id` must have a maximum length of 50 characters and can only contain **a-z**, **A-Z**, **0-9** and the special characters `/ - _`.

***

## How to enable refunds

1. Go to **Features** > **Payment**.
2. Click the **Allow refunds** toggle.
3. Enter your 4-digit PIN Code.

Once this feature is activated, you can process refunds from your terminal. To do this:

1. Go to **Features** > **History**.
2. Click the relevant transaction.
3. Click **Refund**. You can process full or partial refunds.
4. Click **Ok** > **Confirm**.

***

## How to enable ❌ cancel

1. In the **Navigation** list, click the **Cancel button** toggle to the right.
2. To return to the main screen, click the **Back** button.

***

## How to validate a card

1. In **Settings** > **Payment**, enable **Allow Zero Amount**
2. Customer completes the 0 EUR transaction.
3. You will see the transaction with 0 amount in your transaction overview.

***

## How to view transaction overview

1. On the navigation menu, click the **Back** button.
2. Select **History**.
3. Select the relevant transaction, and you can:

* View transaction information **or**
* Send a copy of the transaction via email.

***

## How to unbind your terminal

1. In the **Settings** list, go to the menu in the top left corner.
2. Select **Security**, and insert your 4-digit PIN Code.
3. Click **Unbind** and confirm.

**⚠️ Note:** Unbinding will result in a complete data erasure.\
You can bind the terminal to the same or a different account, or terminal group.

## How to use an external printer

Additionally to our built-in printers within some of our devices, you can use the Sunmi kitchen cloud printer via

* Bluetooth
* WiFi
* USB connections

You can set it up within your app:

1. Via Settings, go to *External printer*
2. Press **Discover**
3. Select Connection Type
4. List of printers available is displayed
5. When a payment is completed, click the **printer icon** to print your receipt.

***

[Top of page](#)
