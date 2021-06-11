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

|   |   |   |
|---|---|---|
| **Payment type**   | Post-payment method  | |
| **API flow**  | `Direct`/`Redirect` {{< br >}} Both direct to the Klarna payment page| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Austria, Belgium, Denmark, Germany, Italy, Norway, Spain, Sweden, Netherlands, UK  | |
| **Currencies**  | EUR, SEK, NOK, DKK | [Multi-currency setup](/payment-methods/billing-suite/klarna/faq/activating-multi-currency-setup/) | 
| **Refunds**  | Full and partial  | | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

### Product rules

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, Klarna requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

## Payment flow

The table below shows the Klarna payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details**, there are two statuses that change as the flow progresses: 

- The order status indicates the status of the customer's order with the merchant independent of the payment.  
- The transaction status indicates the status of the payment.

| Order status                      | Transaction status      | | Flow |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
| Uncleared   | Initialized  | 1. | The customer initiates a transaction on the Klarna payment page. {{< br >}} See also [Reservation and invoice numbers](/payment-methods/billing-suite/klarna/faq/reservation-and-invoice-number/). |
| Completed  | Uncleared  | | The transaction is successful, but Klarna hasn't received payment yet. |
| | | 2. | Ship the order within 28 days, or [extend the shipping period](/payment-methods/billing-suite/klarna/faq/extending-shipping-period/). {{< br >}} See also [Supported addresses](/payment-methods/billing-suite/klarna/faq/supported-addresses/). | 
| | | 3. | [Change the order status to Shipped](/payment-methods/billing-suite/klarna/faq/changing-order-status-completed-to-shipped/).  |
| Shipped    | Uncleared  | 4. | MultiSafepay sends a capture to Klarna. |
| | | 5. | Klarna confirms the transaction. |
| | | 6. | MultiSafepay sends the customer an invoice. Your payout is now guaranteed. {{< br >}} See also [Customizing invoices](/payment-methods/billing-suite/klarna/faq/customizing-invoices/). |
| Shipped    | Completed  | 7. | Klarna pays the funds to MultiSafepay (after 14 business days). |
| | | 8. | MultiSafepay deducts the transaction fee and adds the remaining funds to your MultiSafepay balance (after 18-19 days). {{< br >}} **Note:** In your MultiSafepay Control > **Transaction details** page, the merchant fee always displays as 0,00.|
| | | 9. | If the customer returns some items from the order, you can [place the collection period on hold](/payment-methods/billing-suite/klarna/faq/placing-collection-period-on-hold/) for 2 to 4 weeks.  |

Other statuses include:
| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Void   | Cancelled   | Klarna has rejected the transaction. See Klarna&nbsp;–&nbsp;[Contact customer service](https://www.klarna.com/international/contact-customer-service).     |
| Expired    | Expired    | The transaction was not completed or the [order status did not change to Shipped]((/payment-methods/billing-suite/klarna/faq/changing-order-status-completed-to-shipped/)), and the transaction expired. {{< br >}} Expired transactions cannot be reactivated but still appear in your MultiSafepay Control **Transaction overview**. Create a new order, if required.  | 

### Refund flow

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/klarna/#processing-refunds).

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Completed   | The customer requests a refund. | 
| Completed      | Completed   | The refund is successfully processed.  | 


## Activation
Before applying for Klarna, check your eligibility with your account manager at <sales@multisafepay.com> 

For questions, see Klarna – [Klantenservice](https://www.klarna.com/nl/klantenservice).
 
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
For customers, see Klarna – [Contact customer service](https://www.klarna.com/international/contact-customer-service).

For merchants, email MultiSafepay at <klarna@multisafepay.com>
