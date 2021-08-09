---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "American Express - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing American Express in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-testing
    - /payment-methods/credit-and-debit-cards/credit-card-payment-page
---

There are two options for integrating American Express, depending on whether you want to accept multiple credit cards or American Express only. 

#### Multiple credit cards
 
Customers are redirected to a MultiSafepay credit card payment page, where all credit cards are bundled together. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits.

See API Reference – [Credit cards](/api/#credit-cards).

#### American Express only
Customers are redirected straight to American Express. 

See API Reference – [American Express](/api/#american-express).

## Testing

{{< details title="Credentials and testing process" >}}

Test card details:

- Card number: See the table below.
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 378282246310005| **Completed** | Transaction was completed (not 3D enrolled) |
| 374200000000004| **Declined**  | Transaction was declined |
| 378734493671000| **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |

{{< /details >}}

For the American Express logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).