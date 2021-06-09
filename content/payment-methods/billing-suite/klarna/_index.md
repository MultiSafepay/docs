---
title: 'Klarna'
weight: 190
meta_title: "Payment methods Klarna - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
intro_description: "Klarna is an online post-payment method that lets customers pay for orders after receiving them. Customers are only charged for the items they keep from the order. Klarna guarantees payout of the transaction."
layout: 'single'
logo: '/logo/Payment_methods/Klarna.svg'
faq: '.'
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
