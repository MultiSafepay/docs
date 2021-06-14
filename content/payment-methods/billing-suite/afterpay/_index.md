---
title: 'AfterPay'
weight: 180
meta_title: "Payment methods AfterPay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/AfterPay.svg' 
short_description: 'Largest post-payment solution in the Netherlands. Now available in Belgium.'
aliases:
    - /support-tab/magento2/payment-methods/afterpay
    - /payment-methods/afterpay/
    - /payment-methods/afterpay/activate-afterpay
    - /payment-methods/afterpay/afterpay-testing
    - /payment-methods/afterpay/how-does-afterpay-work
    - /payment-methods/afterpay/refund-afterpay
    - /payment-methods/afterpay/what-is-afterpay
---

## About AfterPay

AfterPay is the largest online post-payment service in the Netherlands, and recently launched in Belgium. Customers pay for orders after receiving them, and are only charged for items they keep from the order. AfterPay bears the risk and guarantees payout.

|   |   |   |
|---|---|---|
| **Payment type**   | Post-payment method  | |
| **API flow**  | `Direct`/ `Redirect`| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands, Belgium  | |
| **Currencies**  | EUR |  | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/billing-suite/afterpay/faq/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

### Product rules

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, AfterPay requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

- You cannot [adjust payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

- AfterPay requires an additional API key for Belgium. Contact AfterPay.

- You must [activate MultiSafepay PayV2 payment pages](/payment-methods/billing-suite/afterpay/faq/activating-payv2/) at website level in your MultiSafepay Control. 

- Customers can provide different invoice and delivery addresses, but the customer's first and last name must share at least two characters. The **Transaction details** page in your MultiSafepay Control only shows the invoice address. To retrieve other transaction details, make a GET `/orders` request. See API Reference – [Retrieve an order](/api/#retrieve-an-order).

## Payment flow

The table below shows a successful AfterPay payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|  | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. |  |  |
| 2. | AfterPay approves or declines the transaction. No action is required. | Uncleared | Uncleared |
| | The transaction is successful.  | Completed  | Uncleared  |
| 3. | Ship the order. | | |
| 4. | [Change the order status to Shipped](/payment-methods/billing-suite/afterpay/faq/changing-order-status-to-shipped/).  | Shipped | Uncleared |
| 5. | MultiSafepay sends a capture to AfterPay. |  |   |
| 6. | AfterPay confirms the transaction. | | |
| 7. | MultiSafepay sends the customer an invoice with a standard payment period of 14 days. Your payout is now guaranteed. | | |
| 8. | The customer makes the payment to AfterPay  via [iDEAL](/payment-methods/banks/ideal/) or internet banking, within 14 days unless otherwise agreed in writing. |  |  |
| 9. | AfterPay pays the funds to MultiSafepay. |  |  |
| 10. | MultiSafepay adds the funds to your MultiSafepay balance.| Shipped | Completed |

### Other statuses

| Description | Order status | Transaction status |
|---|---|---|
| AfterPay has rejected the transaction. AfterPay only provides the reason directly to the customer, for privacy and compliance reasons. {{< br >}} **Or** {{< br >}} The transaction was cancelled. | Void | Cancelled |
| The customer did not complete the transaction within 90 days of initiating it and the transaction has expired. | Expired | Expired |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/klarna/#processing-refunds).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund was successfully processed.  | Completed      | Completed   |

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone +31 207230230 or email <merchant@afterpay.com> 

## Activation 

To check you are eligible for AfterPay, email your account manager at <sales@multisafepay.com>

For new AfterPay clients in:

- The Netherlands, apply to AfterPay – [Offerte](https://www.afterpay.nl/nl/zakelijk/offerte) 
- Belgium, apply to AfterPay – [Offerte aanvragen](https://www.afterpay.be/be/footer/zakelijke-partners/offerte-aanvragen)

For existing AfterPay clients, to activate AfterPay in your MultiSafepay Control email AfterPay Sales at <sales@afterpay.nl>  

{{< details title="View ecommerce integration requirements" >}}

| Ecommerce integration | Available from  | Released  |
|---|---|---|
| [Magento 1](/integrations/ecommerce-integrations/magento1/changelog)  | Version 2.4.1.  | May 25, 2018  | 
| [Magento 2](https://github.com/MultiSafepay/Magento2Msp/blob/master/CHANGELOG.md)  | Version 1.5.0.  | May 5, 2018  |
| [WooCommerce](https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md)  | Version 3.1.0.  | June 15, 2018  |
| [OpenCart](https://github.com/MultiSafepay/Opencart/blob/master/CHANGELOG.md)  | Version 2.2.0.  | June 15, 2018  |
| [PrestaShop 1.7](https://github.com/MultiSafepay/PrestaShop/blob/master/CHANGELOG.md)  | Version 4.2.0.  | May 25, 2018  |
| [CS-Cart](https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md)  | Version 1.3.0.  | October 8, 2018  |
| [X-Cart](/integrations/ecommerce-integrations/x-cart)  | Version 2.2.0.  | April 24, 2019  |

{{< /details >}}

## Integration and testing

To integrate AfterPay using our API, see API Reference – [AfterPay](/api/#afterpay).

{{< details title="View testing process" >}}
&nbsp;  
To enable AfterPay in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}



