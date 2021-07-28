---
weight: 350
meta_title: "API Reference - Discounts - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block hide >}}
{{< /code-block >}}

{{< description >}}
# Discounts
<hr class="separator">

For [post-payment methods](/payments/methods/billing-suite/), MultiSafepay validates the `shopping_cart`. If&nbsp;you want to apply a discount **before** sending a payment request, we recommend submitting the discount in the unit price. 

Avoid adding discounts as a separate discount rule because, for partial refunds, you can't undo the negative amount. 

{{% note %}} Add the discount as unit price when you process postpaid payment methods {{% /note %}}
{{% /description %}}