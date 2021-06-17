---
title: 'AfterPay payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "AfterPay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
---

The table below shows a successful AfterPay payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

### Payment flow

|  | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. |  |  |
| 2. | MultiSafepay reserves the funds while AfterPay authorizes the payment. | Uncleared | Uncleared |
| 3. | Once authorized, the funds are captured and transferred to AfterPay.  | Completed  | Uncleared  |
| 4. | Ship the order. | | |
| 5. | [Change the order status to Shipped](/payment-methods/billing-suite/afterpay/faq/changing-order-status-to-shipped/).  | Shipped | Uncleared |
| 6. | AfterPay invoices the customer with a standard payment period of 14 days. Settlement is now guaranteed. | | |
| 7. | The customer completes the payment with AfterPay via [iDEAL](/payment-methods/banks/ideal/) or internet banking, within 14 days unless otherwise agreed in writing. |  |  |
| 8. | AfterPay settles the funds with MultiSafepay. | Shipped | Completed |
| 10. | MultiSafepay adds the funds to your MultiSafepay balance.|  |  |

### Other statuses

| Description | Order status | Transaction status |
|---|---|---|
| AfterPay has declined the transaction. AfterPay only provides the reason directly to the customer, for privacy and compliance reasons. {{< br >}} **Or** {{< br >}} The transaction was cancelled. | Void | Cancelled |
| The customer did not complete the transaction within 90 days of initiating it and the transaction has expired. | Expired | Expired |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/AfterPay/#processing-refunds).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund was successfully processed.  | Completed      | Completed   |

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone +31 207230230 or email <merchant@afterpay.com> 
