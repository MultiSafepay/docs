---
weight: 200
meta_title: "API Reference - Orders - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#transactions
---
{{< code-block hide >}}
{{< /code-block >}}

{{< description >}}
# Orders
<hr class="separator">

To process a transaction, you must create an order. There are two main types of orders:

+ `Redirect`: The customer is redirected to a [MultiSafepay payment page](/payments/checkout/payment-pages/) (Connect) to complete payment.
+ `Direct`: The transaction is processed directly.

For more information, see [Difference between direct and redirect](/developer/api/difference-between-direct-and-redirect).

**Note:** All fields must be completed correctly.

You can also create a:

+ Checkout order, which creates a "Fast Checkout Order"
+ Payment link in your MultiSafepay account
{{% /description %}}