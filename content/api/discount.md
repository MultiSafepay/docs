---
weight: 50
meta_title: "API - Discount - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
{{< /code-block >}}

{{< description >}}
# Discount
<hr class="separator">
If you, as an online store, want to apply a discount before a payment request is made, it is recommended to take into account how you process the discount with postpaid payment methods. 

Because MultiSafepay validates the shopping cart of postpaid payment method orders, it is advised to submit the discount in the unit price. In spite of the fact that the discount added as an order rule will be accepted, it is advisable to indicate the discount as unit price. The reason why adding the discount in the unit price is recommened is because of a partial refund. Adding a discount as a seperate discount rule creates an issue with partial refunding because the negative amount cannot be undone. 

{{% note %}} Add the discount as unit price when you process postpaid payment methods {{% /note %}}
{{% /description %}}