---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Visa - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing Visa in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/visa/visa-testing
    - /payment-methods/credit-and-debit-cards/mastercard/credit-card-payment-page
---

There are two options for integrating Visa, depending on whether you want to accept multiple credit cards or Visa only. 

#### Multiple credit cards
 
Customers are redirected to a MultiSafepay credit card payment page, where all credit cards are bundled together. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits.

See API Reference – [Credit cards](/api/#credit-cards).

#### Visa only
Customers are redirected straight to Visa. 

See API Reference – [Mastercard](/api/#mastercard).

## Testing

{{< details title="Credentials and testing process" >}}

Test card details: 

- Card number: See the table below.
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

{{< /details >}}
