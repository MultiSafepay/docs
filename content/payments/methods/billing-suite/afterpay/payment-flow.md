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

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

### Payment flow

|  | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. |  |  |
| 2. | AfterPay authorizes the payment. | Uncleared | Uncleared |
| 3. | Once authorized, MultiSafepay sends a capture to AfterPay.  | Completed  | Uncleared  |
| 4. | Ship the order. | | |
| 5. | [Change the order status to Shipped](/payments/methods/billing-suite/afterpay/faq/changing-order-status-to-shipped/).  | Shipped | Uncleared |
| 6. | AfterPay invoices the customer with a standard payment period of 14 days. Settlement is now guaranteed. | | |
| 7. | The customer completes the payment with AfterPay via [iDEAL](/payments/methods/banks/ideal/) or online banking, within 14 days unless otherwise agreed in writing. |  |  |
| 8. | AfterPay settles the funds with MultiSafepay. | Shipped | Completed |
| 9. | MultiSafepay adds the funds to your MultiSafepay balance.| Completed | Completed |

### Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| AfterPay has declined the payment. AfterPay only provides the reason directly to the customer, for privacy and compliance reasons. {{< br >}} **Or** {{< br >}} The payment was cancelled. | Void | Cancelled |
| The customer did not complete the payment within 90 days of initiating it and the transaction has expired. | Expired | Expired |

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone +31 207230230 or email <merchant@afterpay.com> 

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund was successfully processed.  | Completed      | Completed   |
