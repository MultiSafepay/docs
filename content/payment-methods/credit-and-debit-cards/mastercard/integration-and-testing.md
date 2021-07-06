---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Mastercard - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing Mastercard in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/mastercard/mastercard-testing
    - /payment-methods/credit-and-debit-cards/mastercard/credit-card-payment-page
---

There are two options for integrating Mastercard, depending on whether you want to accept multiple credit cards or Mastercard only. 

#### Multiple credit cards
 
Customers are redirected to a MultiSafepay credit card payment page, where all credit cards are bundled together. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits.

See API Reference – [Credit cards](/api/#credit-cards).

#### Mastercard only
Customers are redirected straight to Mastercard. 

See API Reference – [Mastercard](/api/#mastercard).

## Testing

{{< details title="Credentials and testing process" >}}

Testing Mastercard is similar to Visa. For extensive testing, use Visa. 

Test card details: 

- Card number: 5500000000000004
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed (3D enrolled)|

{{< /details >}}

For the Mastercard logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).