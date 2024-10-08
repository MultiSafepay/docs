---
title: 'SmartPOS features'
parentDoc: 64674fbc74bc4007521ebbcb
category: 6477597e0e2961004638cd5d
order: 1
hidden: false
slug: 'smartpos-features'

---

> ⚠️ Note:
> 
> We currently offer this product in the following countries:
> 
> - Netherlands
> - Belgium 
> 
> If you are interested in our Point of Sale solutions, email [\[sales@multisafepay.com\](mailto:sales@multisafepay.com)](mailto:[sales@multisafepay.com](mailto:sales@multisafepay.com))

After activating your SmartPOS terminal, you can add features from your SmartPOS payment app. SmartPOS features let you:

- Display items after payment have been processed. 

- Add a tip to your payment flow.

- Send an invoice to your customer via email or print.

- Initiate payments manually or using cloud mode.

- Hide the navigation menu on the main screen.

- View the transaction overview.

# Add features

To add payment flow features, follow these steps: 

1. On the navigation menu, click the **Back** button.
2. Select **Settings**.  
   <!-- <br>  
   <br>  
   <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/SmartPOS-pay-flow.png" alt="POS-display" width="250" style="display: block;"/>  
   <br> -->

## How to enable display items

1. In the **Global settings** list, click the **Display items** toggle.
2. To return to the main screen, click the **Back** button.

Once you've initiated the payment, the items are displayed on the payment screen.

<!-- **Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-items-screen.png" alt="POS-display" width="250" style="display: block;"/>  
<br>

*** -->

## How to enable tipping

1. In the **Global settings** list, click the **Tipping** toggle.
2. To return to the main screen, click the  **Back** button.

After the payment has been processed, the option to tip is displayed on the payment screen.

<!-- **Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-tipping-screen.png" alt="smartPOS_print" width="250" style="display: block;"/>  
<br> -->

You can add an employee via **add employee** > Insert name and ID.



***

## How to enable print or email

1. In the **Global settings** list, click the **Print/Email** toggle.
2. To return to the main screen, click the **Back** button.

<!-- **Example:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/POS-print-screen.png" alt="smartPOS_print" width="250" style="display: block;"/>
<br>

*** -->

## How to enable manual input

1. In the **Payment** list, click the ** Manual input** toggle.
2. To return to the main screen, click the **Back** button.

***

## How to enable cloud mode

1. In the **Payment** list, click the ** Cloud mode** toggle to the right.
2. To return to the main screen, click the **Back** button.

***

To exit the cloud mode payment screen:

1. Tap and hold the **MultiSafepay** logo for few seconds.
2. Enter the default **PIN code**. <br>The default PIN code is `1324`.

**⚠️ Note:** For your security, we recommend you change the default PIN code as soon as possible. 

***

## How to define your closing order flow

Upon completed or declined payment, the customer can be redirected to a page that confirms the outcome of the payment process, OR go back automatically to your app.   
Example message on the confirmation screen: "Payment is completed successfully". 

You can customize this flow:

1. Go to **Settings** > Payment > *Close timeout*
2. To display the confirmation screen for a fixed amount of time, select the seconds from the dropdown. This is the timeout of the "Completed" page.
If you select *disabled*, there is no automatic timeout, and you will need to press *Close Order* to close the confirmation screen and return to your own application. 

**⚠️ Note:** This applies to both cloud mode and native application setups. 

## How to change the PIN code 

1. Go to **Settings** >  **Security**.
2. Enter the default PIN code.
3. Click **Change** and then enter your new PIN code. 
4. Click ✔.

</details>

***



After you've enabled the **Cloud mode**, the **Navigation** list appears. This feature allows you to hide the cancel button and system navigation.

<!-- **Example:**  
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/SmartPOS-cloud-mode.png" alt="smartPOS_print" width="250" style="display: block;"/>  
<br> -->

## How to generate closing balance

At the end of a processing period, you can print an overview of total transaction amounts per payment method, and tips.  

Via Settings > **Closing balance**, can set the following parameters:

- Default date: today, yesterday
- Closing start hour: if you include a start hour, the period will count 24 from the set time on
  Example: set 10.00 >> period is 10.00 to 09:59
- Closing end hour
- Filter by: Company, Terminal group, Terminal

You can see the selected details displayed on screen, and in the header of the receipt.  

</details>

**💡 Tip!** You can print your closing balance report using either the device printer, or the [external printer](docs/test-page#external-printer).

***


## How to hide navigation

1. In the **Navigation** list, click the ** System navigation** toggle to the right.
2. To return to the main screen, click the **Back** button

**Note:** To access the navigation menu, tap the **MultiSafepay** logo.

</details>

***

## How to switch languages

1. In the **Settings** section, go to \*_Languages_.
2. Select between English, Dutch, and Spanish.

</details>

***

## How to scan qr codes

You can use the QR code reader within our app to easily recognize order information and include it in a transaction.

1. In the **Settings** section, enable \*_Insert order_.
2. When using **Manual input**, select \*_Scan QR_.

The QR reader is able to detect the following parameters:

- amount
- order ID
- description  
  This information will be included in the payment request. 

</details>

***

## How to enable ❌ cancel

1. In the **Navigation** list, click the **Cancel button** toggle to the right.
2. To return to the main screen, click the **Back** button.

</details>

***

## How to validate a card

1. In Settings > **Payment**, enable _Allow Zero Amount_ 
2. Customer completes the 0 EUR transaction.
3. You will see the transaction with 0 amount in your transaction overview.

</details>

***

## How to view transaction overview

1. On the navigation menu, click the **Back** button.
2. Select **History**.
3. Select the relevant transaction, and you can:

- View transaction information **or**
- Send a copy of the transaction via email.

***

## How to unbind your terminal

1. In the **Settings** list, go to the menu in the top left corner.
2. Select \*_Security_, and insert your 4-digit PIN Code. 
3. Click \*_Unbind_ and confirm. 

**⚠️ Note:** Unbinding will result in a complete data erasure.  
You can bind the terminal to the same or a different account, or terminal group. 

## How to use an external printer

Additionally to our built-in printers within some of our devices, you can use the Sunmi kitchen cloud printer via 

- Bluetooth
- WiFi
- USB connections

You can set it up within your app:

1. Via Settings, go to _External printer_
2. Press _Discover_
3. Select Connection Type
4. List of printers available is displayed
5. When a payment is completed, click the **printer icon** to print your receipt.


</details>
***

[Top of page](#)