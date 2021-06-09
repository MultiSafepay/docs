---
title: 'Klarna'
weight: 190
meta_title: "Payment methods Klarna - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
logo: '/logo/Payment_methods/Klarna.svg' 
short_description: 'A popular post-payment solution for webshops based in Austria, Germany, and the Netherlands'
aliases:
    - /support-tab/magento2/payment-methods/klarna
    - /payment-methods/klarna/
---

Klarna is an online post-payment method that lets customers pay for orders after receiving them. Customers are only charged for the items they keep from the order. Klarna guarantees payout of the transaction.

|   |   |
|---|---|
| **Payment type**   | Pay After Delivery  |
| **Payment flow**  | Redirect. [More information](/faq/api/difference-between-direct-and-redirect) 
| **Countries**  | Austria, Belgium, Denmark, Germany, Italy, Norway, Spain, Sweden, Netherlands, UK  | 
| **Currencies**  | EUR, SEK, NOK, DKK  | 
| **Refund options**  | Full and partial  | 
| **Recurring payments**  | No. [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No. [More information](/faq/chargebacks)  |

## How it works

### Transaction flow
After the customer places an order, the status of the order and the transaction change during processing:

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment    

{{< alert-notice >}} As of May 11, 2021, after orders are accepted Klarna transactions receive **Uncleared** status (instead of **Initialized** status). This changes to **Completed** after the order ships and Klarna settles the payment. The funds are then added to your MultiSafepay balance. For any questions, email the Support Team at <support@multisafepay.com> {{< /alert-notice >}} 

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized   | Initialized  | The customer has initiated a Klarna transaction.   |
| Completed  | Uncleared  | The transaction was successful. The order is awaiting shipment. Klarna has not yet received payment.   |
| Shipped    | Uncleared  | MultiSafepay has sent a capture to Klarna, and Klarna has confirmed the transaction. MultiSafepay has sent an invoice to the customer. Your payout is guaranteed. |
| Shipped    | Completed  | MultiSafepay has received the funds from Klarna and added them to your MultiSafepay balance.|
| Declined   | Declined   | Klarna has rejected the transaction. For the reasons, see the **Declined** status field in your [MultiSafepay Control](https://merchant.multisafepay.com).     |
| Void       | Cancelled   | The transaction has been cancelled.  | 
| Expired    | Expired    | The customer didn't proceed with the transaction and it automatically expired. | 

{{< details title="About expiration" >}}

Once you accept an order, must ship it within 28 days. If this is not possible, you can extend the time period for up to 180 days in segments in your [MultiSafepay Control](https://merchant.multisafepay.com) via the **Extend** button.

If the order is not captured during this time, both the order and transaction status changes to **Expired**. The order can't be reactivated. You will need to create a new order.

{{< /details >}}

### Refund flow 
Refunds receive the following statuses:

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Completed   | The customer has requested a refund. | 
| Completed      | Completed   | The refund has been successfully processed.  | 

For more information, see [Processing refunds](/payment-methods/billing-suite/klarna/#processing-refunds) below.

### Product rules

{{< details title="Refunding more that the original transaction" >}}
&nbsp;  
You cannot refund more than the amount of the original transaction. 

{{< /details >}}

{{< details title="Time limit on refunds" >}}
&nbsp;  
There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

{{< /details >}}

{{< details title="Payment link lifetimes" >}}
&nbsp;  
You cannot [adjust payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

{{< /details >}}

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed. This is because, as the collecting party, Klarna requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before making the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

## Fees
The fee is not charged directly after the order is placed. In your MultiSafepay Control > **Transaction details** page, the merchant fee is always 0,00.

MultiSafepay charges your account when the payment is settled. One or more transactions is created in your **Transaction overview**.

## Activation
Before applying for Klarna, check your eligibility with your account manager at <sales@multisafepay.com> 

For questions, see Klarna - [Klantenservice](https://www.klarna.com/nl/klantenservice).
 
### New Klarna clients
1. To sign up as a new Klarna client, email Klarna Sales at <verkoop@klarna.com>, and specify MultiSafepay as your payment service provider. You must sign an independent agreement with Klarna, including pricing.
2. Klarna asks MultiSafepay to activate Klarna as a payment method for your ecommerce platform.
3. You activate Klarna in the backend of your ecommerce platform.
4. Test your integration.
5. Request an acceptance test for specific URLs to Klarna Sales at <verkoop@klarna.com>
6. Having completed the acceptance test, in your Klarna Online dashboard, change the status to **Live environment**.

### Existing Klarna clients

For more information and support for existing clients, email Klarna Verkoop at <verkoop@klarna.com>

For questions about your Klarna integration and the connection with MultiSafepay Control, email the Integration Team at <integration@multisafepay.com>

## Integration
Klarna makes your ecommerce platform available in the MultiSafepay partner portal, where your credentials are generated. Use your credentials to configure the Klarna gateway in your MultiSafepay Control. 

To integrate Klarna using our API, see API Reference - [Klarna](/api/#klarna).

### Testing

For more information about testing Klarna payments, see [Test payment details](/faq/getting-started/test-payment-details/#klarna).

### Support
For customer-related questions about Klarna orders and transactions, see Klarna - [Contact customer service](https://www.klarna.com/international/contact-customer-service).

For merchant-related questions, email the Integration Team at <integration@multisafepay.com>

## User guide

### Changing order status from Not shipped to Shipped

When the customer chooses to pay with Klarna, MultiSafepay creates a Klarna transaction with **Not shipped** status. 

Klarna does not support auto-ship functionality, so after you ship the order to the customer, you need to change the order status to **Shipped** to start communicating with the customer. There are 3 ways to do this:

- Change the status manually in your MultiSafepay Control.
- Use our API to automatically change the status in your custom integration.
- Some ecommerce integrations change the status automatically. Check in your integration.

To change the order status manually, follow these steps:

- Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
- Go to **Transactions** > **Transactions overview**.
- Search for the transaction, and click to open the **Transaction details** page. 
- Under **Order details**, click **Change order status**. 
- Change the status to **Shipped**.
- Send the customer the Track & Trace details, if relevant.

After 14 business days, MultiSafepay receives the funds from Klarna and makes them available to merchants. After 18-19 days, MultiSafepay adds the funds to your MultiSafepay balance when the transaction status changes to **Completed**.

### Changing order status from Completed to Shipped
When you agree with an order and ship it, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets Klarna initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance.

You can do this:

- Automatically using our [API](https://docs.multisafepay.com/api/#update-an-order), which updates your MultiSafepay Control 
- Automatically in your [ecommerce integration](/integrations/ecommerce-integrations)
- Manually in your [MultiSafepay Control](https://merchant.multisafepay.com)

To change the order status manually, follow these steps:

1. Go to **Transactions** > **Transactions overview**.
2. Search for the transaction and click to open the **Transaction details** page.
3. Use the **Change order status** field.

### Processing refunds 

**In MultiSafepay Control**

You can process 3 types of refund: full, partial, and discounts.

Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

{{< details title="Full refunds" >}}
  
To refund the full transaction, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

   The transaction is cancelled.

{{< /details >}}

{{< details title="Partial refunds" >}}

To refund part of the transaction in the checkout editor, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Select the item(s) you want to deduct from the order.
6. Click **Save**.

   The transaction shows the credited item(s) with the deducted amount added to the transaction.
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

{{< details title="Discounts" >}}

Discounts are processed as a **negative amount** instead of a **negative quantity**. This method of adding discounts only applies to successful transactions. 

For how to add discounts **before** the transaction request is submitted to MultiSafepay, see API Reference - [Discount](/api/#discount).

Instead of deleting an item in the checkout editor, you may want to add a discount. Follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Add the discount as a new page in the checkout editor.  
    Example: quantity (1) > discount (item or name) > amount (as negative) > VAT
6. To deduct the amount of the discount, add a new line to the order.
7. Click **Save**.

   The discount is added to the transaction. 
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

**In your backend**

You can process refunds in the backend of most MultiSafepay [ecommerce integrations](/integrations/ecommerce-integrations). For more information, see the User guide of the relevant integration.

### Return process

Pay-after-delivery methods let customers pay only for items they keep from an order. This means sometimes customers return products. If the return process takes too long to verify, you can place the collection period on hold for 2 to 4 weeks. Call Klarna on +31 208082853 or email Klarna Sales at <verkoop@klarna.com>

### Reservation number and invoice number
For every transaction, Klarna generates:

- A reservation number for while the order is not yet activated. Use this as a reference number when contacting Klarna with any questions at this stage.
- An invoice number when the order status changes to **Shipped**.

Both numbers appear in the relevant **Transaction details** page in your MultiSafepay Control.

### Reconciliation and reports
MultiSafepay atuomatically reconciles with Klarna.

Klarna transactions appear in all [MultiSafepay reports](/tools/accounting/reports/).

### Customizing invoices
Klarna lets you customise the styling and layout of all invoices you send to customers via your Klarna Merchant Account. For support, see Klarna - [Klantenservice](https://www.klarna.com/nl/klantenservice/).

### Supported addresses
For more information about delivery and collection addresses, see Klarna - [Shipping policies](https://www.klarna.com/international/shipping-policies/).