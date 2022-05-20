---
title: 'Klarna'
weight: 40
meta_title: "Payment methods - Klarna - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/Klarna.svg'
short_description: 'A popular pay later method in Austria, Germany, and the Netherlands.'
url: '/payment-methods/klarna/'
aliases:
    - /support-tab/magento2/payment-methods/klarna
    - /payment-methods/klarna/
    - /payment-methods/billing-suite/klarna
    - /payments/methods/billing-suite/klarna/
    - /payments/methods/billing-suite/klarna/about/
    - /payments/methods/klarna/product-rules/
    - /payment-methods/klarna/product-rules/
    - /payment-methods/klarna/overview/
    - /payments/methods/billing-suite/klarna/payment-flow/
    - /payment-methods/klarna/payment-flow/
    - /payments/methods/billing-suite/klarna/integration-and-testing/
    - /payment-methods/klarna/integration-testing/
    - /payments/methods/billing-suite/klarna/activation/
    - /payment-methods/klarna/activation/
    - /payments/methods/billing-suite/klarna/user-guide/handling-errors/
    - /payment-methods/klarna/handling-errors/
    - /payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/
    - /payment-methods/klarna/extending-shipping-period/
    - /payments/methods/billing-suite/klarna/user-guide/reservation-and-invoice-number/
    - /payment-methods/klarna/reservation-invoice-numbers/
    - /payment-methods/klarna/handling-expired-orders/
    - /payments/methods/billing-suite/klarna/user-guide/placing-collection-period-on-hold/
    - /payment-methods/klarna/pauzing-collection/
    - /klarna/handling-disputes/
    - /payments/methods/billing-suite/klarna/user-guide/customizing-invoices/
    - /payment-methods/klarna/customizing-invoices/
---
[Klarna](https://www.klarna.com/) is a flexible online payment method that lets customers pay now, in 30 days (Pay Later 30), or in 3 interest-free installments. It also offers financing. Customers are only charged for the items they keep from the order. Klarna bears the risk and guarantees settlement.

[See how Klarna can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/klarna)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Austria, Belgium, Denmark, Finland, France, Germany, Italy, Norway, Portugal, Spain, Sweden, Switzerland, The Netherlands, UK <br> (US **not** supported)  | 
| **Currencies**  | EUR, GBP, SEK, NOK, DKK  | 
| **Chargebacks**  | No  | 
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Transactions expire after** | 1 hour |
| **Addresses** | The customer's billing and shipping addresses must be the **same**. | 

### Surcharges  

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, see Klarna – [Welk bedrag kan ik maximaal doorberekenen aan mijn klant?](https://www.klarna.com/nl/zakelijk/webwinkelsupport/welk-bedrag-kan-ik-maximaal-doorberekenen-aan-mijn-klant/) 

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant K as Klarna
    participant Me as Merchant

    C->>Mu: Selects Klarna at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, email address, and phone number, <br> and accept the terms & conditions, <br> then redirects to your success page
    else Direct flow
    Mu->>C: Redirects to Klarna
    end
    K->>Mu: Authorizes the payment
    Mu->>K: Captures the funds (settlement is now guaranteed)
    Me->>C: Ships the order (within 28 days, or extend the shipping period)
    Note over Me,C: Manually change the order status to Shipped. 
    K->>C: Sends invoice (you can customize the invoice) 
    C->>K: Completes payment with preferred payment method
    K->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 21 days)

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Klarna. <br> You can still cancel with Klarna using the reservation number. | Initialized   | Initialized  |
| Klarna has authorized the transaction and the funds are awaiting capture. <br> (You can no longer cancel; you can only refund.) | Completed  | Uncleared  |
| **Important:** To capture the funds, [manually change the order status to Shipped](#shipping-orders). | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| The transaction expired after 1 hour or you didn't [change the order status to Shipped](#shipping-orders) within 28 days. <br> See [Handling expired orders](#handling-expired-orders).  | Expired    | Expired    |
| Klarna authorized the transaction, but either you or the customer cancelled it before capture. | Void   | Void |
| Klarna declined the transaction. <br> Only the customer can contact Klarna to find out why (for privacy and compliance reasons). <br> For merchant support, email <klarna@multisafepay.com> | Declined | Declined |
|**Refunds**|||
| Refund initiated. | Initialized | Completed |
| Refund complete.  | Completed | Completed |

{{< /details >}}

{{< details title="Klarna reference numbers">}}

For every transaction, Klarna generates two reference numbers:

- Reservation number for before shipment
- Invoice number for after shipment

Both reference numbers appear in the **Transaction details** page in your dashboard.

{{< /details >}}

### Shipping orders

When you ship the order, you **must** manually change the [order status](/about-payments/multisafepay-statuses/) from **Completed** to **Shipped**, which:

- Captures the funds
- Triggers sending the invoice to the customer
- Prevents the order from expiring

{{< details title="Changing order status to Shipped" >}}

**In your dashboard**

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/integrations/ready-made/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request.

**Note:** Some third-party plugins may not support updating the status via our API.

{{< /details >}}

### Extending the shipping period

If you cannot ship the order within 28 days, you can extend the time period for up to 180 days in segments.

If the order is not captured during this time, the [order and transaction status](/about-payments/multisafepay-statuses/) change to **Expired**.

{{< details title="Extending the shipping period" >}} 

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction.
3. In the **Transaction details** page, click **Extend**.

{{< /details >}}

### Pauzing the collection period

If a customer's return takes too long to verify, you can pauze the collection period for 2-4 weeks. 

Call Klarna on +31 208082853 or email Klarna Sales at <verkoop@klarna.com>

### Handling expired orders

Orders may expire if you don't change the order status to **Shipped** within 28 days. 

{{< details title="Handling expired orders" >}} 

You can send the customer a payment link from the existing order or a new order.

**Existing order**

1. Sign in to your MultiSafepay dashboard.
2. Go to **Transactions** > **Transaction overview**, and then select the expired transaction.  
3. Click **Payment link**, and then click **Duplicate this order**.
4. On the **Payment link generator** page, click **Generate payment link**. 
5. Send the payment link to the customer. 

**New order**

1. [Create a new order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order.  
See also Examples > Klarna redirect.
2. [Ship the order](https://docs-api.multisafepay.com/reference/updateorder) > Ship order.
3. Send the payment link to the customer.

{{< /details >}}

### Handling disputes

A dispute is when you and a customer disagree about an order:

- Goods, e.g. the customer returns all or part of the order, or the goods were faulty when delivered
- Payments, e.g. invoicing errors, or the customer paid Klarna instead of you
- Other, e.g. insolvency, or bankruptcy

Klarna provides support for resolving disputes. For a step-by-step overview, see Klarna – [How to handle disputes at Klarna](https://docs.klarna.com/disputes/).

The easiest way to handle disputes is using the Disputes app in the Klarna Merchant Portal. 

{{< details title="Connecting to the Klarna Merchant Portal" >}}
  
You'll receive an email from Klarna inviting you to activate your portal account. The link expires within 7 days and is only usable once. 

If your link has expired or you haven't received an email, email <support@multisafepay.com> 

1. In the email, click **Activate account**.
2. Read the Merchant Portal Agreement, agree to the terms and conditions, and then click **Continue**.
3. Enter a password, and click **Update password**.
4. Enter your first and last names, and then click **Update profile**.
5. To sign in for the first time, enter your email address and the password you just created, and then click **Log in**.

**Note:** If viewing orders in the portal, you must still manually change the order status to Shipped to trigger the invoicing process and receive payment.

{{< /details >}}

{{< details title="Setting up two-factor authentication" >}}

If you want to increase the security of your Klarna Merchant Portal, set up two-factor authentication with the Google Authenticator app.

1. Under **To-dos**, click **Activate two-factor authentication**. 
2. In the dialog, click **Start the setup**.
3. Open the Google Authenticator app and scan the QR code. 
4. Enter the one-time authorization code from the app, and click **Set up authentication**.

{{< /details >}}

{{< details title="Signing up for the Disputes app" >}}

To sign up to use the Disputes app, follow these steps:

1. Sign in to the [Klarna Merchant Portal](https://eu.portal.klarna.com/).
2. In the side menu, click **Disputes**.
3. Select an email address and preferred language for receiving dispute-related emails, e.g. reminders.
4. Agree to the terms and conditions. 
5. Click **Sign up**. 

Klarna will send you an email when the first dispute appears in the app. 

**Using the Disputes app**

The side menu contains three pre-set filters to view:

- All disputes
- Unauthorized disputes
- Disputes expiring soon

See Klarna – [Disputes App in Merchant Portal](https://docs.klarna.com/disputes/disputes-app-in-merchant-portal/) for detailed information on:

- Searching and filtering disputes
- Exporting reports
- Dispute statuses
- Managing settings
- Responding to disputes
- Accepting losses

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Klarna activation](/payments/activating-payment-methods/#klarna) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#pay-later-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order <br> Examples > Klarna direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (redirect). |

{{< details title="Gift cards" >}}

When paying with a gift card and Klarna, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Klarna collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

{{< /details >}}

### Configuring the Klarna gateway 

Klarna makes your ecommerce platform available in their merchant portal, where your credentials are generated. Use your credentials to configure the Klarna gateway for your MultiSafepay account. 

For questions about your Klarna integration and the connection with your MultiSafepay account, email <integration@multisafepay.com>

{{< details title="Known errors" >}}

If you receive a `code:BAD_VALUE, Bad value: order_lines[0].reference` error from Klarna, try using shorter SKU numbers, e.g. fewer than 9 characters. 

{{< /details >}}

### Managing your brand

{{< details title="Adding your logo to Klarna invoices" >}}

1. Sign in to your Klarna Merchant Account, and then go to **Branding**.
3. Under **Logo**, upload a .png or .jpeg logo. 
    - For best results, use a square image with a transparent background. 
    - Resolution 180x180 px or higher

{{< /details >}}

{{< details title="Managing your brand information" >}}

Under **Brand information**, you can set up and manage your brand including:
- Brand name
- Home page
- Instagram URL
- Facebook URL

{{< /details >}}

For support, see Klarna - [Klantenservice](https://www.klarna.com/nl/klantenservice/). 

