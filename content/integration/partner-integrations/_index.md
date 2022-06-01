---
title: 'Partner integrations'
breadcrumb_title: "Partner integrations"
layout: 'single'
meta_title: 'Partner integrations - MultiSafepay Docs'
logo: "/svgs/Partner_Account_Control.svg"
short_description: 'Explore integrations with our partners to help manage your business.'
weight: 80
url: '/partner-integrations/'
aliases:
    - /business/growth/
    - /partner-integrations/business-growth/
    - /business/growth/picqer/
    - /partner-integrations/picquer/
    - /business/growth/sherpaan/
    - /partner-integrations/sherpaan/
    - /integrations/cash-register-software/
    - /integrations/cash-register-software/mpluskassa/
    - /business/order-management/
    - /partner-integrations/manage-orders/
    - /integrations/reservation-management/
    - /integrations/reservation-management/planyo/
    - /business/reservation-management/
    - /partner-integrations/manage-reservations/
    - /integrations/credit-and-subscription-management/
    - /business/website/
    - /partner-integrations/build-website/
    - /business/website/duda/
    - /partner-integrations/duda/
    - /business/website/mijndomein/
    - /partner-integrations/mijndomein/
    - /integrations/credit-and-subscription-management/
    - /business/subscription-management/
    - /partner-integrations/manage-subscriptions/
    - /integrations/credit-and-subscription-management/hostbill/
    - /business/subscription-management/hostbill/
    - /partner-integrations/hostbill/
    - /integrations/credit-and-subscription-management/twikey/
    - /business/subscription-management/twikey/
    - /partner-integrations/twikey/
---
Check out our integrations with the following partners:

## Business growth

- [Picqer](https://picqer.com/nl)
- [Sherpaan](https://sherpaan.nl/project/multisafepay/)

## Reservations

Our partner [Planyo](https://www.planyo.com/) offers online reservation software that lets customers make, confirm, and modify reservations, and pay online. You can also customize the reservation form. 

{{< details title="Integration" >}}

To integrate Planyo with MultiSafepay, follow these steps:

1. Sign in to your Planyo account.
2. Go to **Site settings** > **Online payments**.
3. Select **MultiSafepay**.
4. Enter your MultiSafepay account ID, [site ID and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).  
5. Make a test reservation. 

{{< /details >}}

## Restaurants, cafes, and hotels

Our partner [MplusKASSA](https://www.mpluskassa.nl) offers order management software for restaurants, cafes, and hotels, which can integrate with MultiSafepay.

For more information, email MplusKASSA at <info@mpluskassa.nl>

{{< details title="Known error" >}}
**Note:** When customers successfully complete payment with iDEAL, they don't always return to your site, which can briefly delay the transaction status changing to **Completed**. If your business model requires you to retrieve the status as quickly as possible, MultiSafepay can enable a script to query iDEAL 5 times in the first minute, and then every minute until **Completed**.  

To discuss, email <integration@multisafepay.com>

{{< /details >}}

## Subscriptions

### HostBill

Our partner [HostBill](https://hostbillapp.com/) provides billing and automation software handles all aspects of running an online business, from client acquisition, invoicing, payments and management, to customer service and support.

{{< details title="Integration and testing" >}}

To integrate MultiSafepay as your payment provider, follow these steps:

**Step 1.** Activate the MultiSafepay module in your HostBill account.

1. Sign in to your HostBill account.
2. Click **Extras** > **Plugins**.
3. From the left menu, select **Payment modules** > **MultiSafepay**.
4. Click **Edit general settings**, and then enter your [MultiSafepay site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
5. Click **Save changes**.

**Step 2.** Configure the module as required, e.g. the [module name and callback URL](https://hostbill.atlassian.net/wiki/spaces/DOCS/pages/559120402/MultiSafepay).

**Step 3.** Perform a test transaction.

1. Go to the top menu and select **Clients** > **Manage clients**, and then click  the sample client account **John Doe**.
2. Click **Login as client**.  
    You are redirected to the client area
3. From the left menu, select **Billing** to view the client’s invoices. 
4. Choose an invoice and click **Pay selected invoices**.
5. Perform a test transaction.
6. When the transaction is complete, check its status under **Payments**.

{{< /details >}}

### Twikey

Our partner [Twikey](https://www.twikey.com/) offers an online tool for managing and collecting subscriptions that includes [SEPA direct debit mandate management](https://www.twikey.com/solution/mandate.html).

Customers can complete payments via:

- A MultiSafepay [payment link](/payments/checkout/payment-link/) added to your invoice.  
See Twikey – [Naadloze integratie MultiSafepay](https://www.twikey.com/nl/partner/multisafepay.html).
- A one-off payment link or QR code sent via Twikey, e.g. by email, WhatsApp, SMS

{{< details title="Integration" >}}

To integrate with MultiSafepay, follow these steps:

1. Sign in to your Twikey account.
2. Go to **Settings** > **Integrations** > **MultiSafepay**.
3. Enter your [MultiSafepay site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
4. To add a payment link to your invoices, update your invoice settings in your [Twikey template settings](https://www.beta.twikey.com/support/creditor/invoices/invoice_options.html).
5. To create a payment link, go to [Payment links](https://www.beta.twikey.com/support/creditor/paymentlinks/paymentlink_management.html) enter the relevant information, e.g. amount, customer.

{{< /details >}}

## Websites

- [Duda](https://www.duda.co/)
- [MijnDomein](https://www.mijndomein.nl/)

