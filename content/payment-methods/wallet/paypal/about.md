---
title: 'About PayPal'
breadcrumb_title: 'About PayPal'
weight: 10
meta_title: "About PayPal - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/wallet/paypal/what-is-paypal
---

PayPal is a leading global payment method that lets customers pay by credit card or create a digital wallet linked to multiple payment methods.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Wallet  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](https://developer.paypal.com/docs/payouts/reference/country-and-currency-codes/) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/wallet/paypal/user-guide/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks)  |

## Product rules

- PayPal payment links are valid for 14 days. The [payment link lifetime](/faq/api/adjusting-payment-link-lifetimes/) is set by PayPal.

- You can only decline or authorize **Uncleared** transactions in your PayPal account.

{{< details title="PayPal Seller Protection" >}}

PayPal Seller Protection covers you in the event of claims, chargebacks, or reversals due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. For a list of the countries, see PayPal API – [State codes](https://developer.paypal.com/docs/nvp-soap-api/state-codes).

For more information, see PayPal – [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156). 

{{< /details >}}
