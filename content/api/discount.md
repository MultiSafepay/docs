---
weight: 50
meta_title: "API - Discount - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
{{% /code %}}

{{% description %}}
# Discount
<hr class="separator">
If you, as an online store, want to apply a discount before a payment request is made, it is recommended to take into account how you process the discount with postpaid payment methods. 

Because MultiSafepay validates the shopping cart of postpaid payment method orders, it is advised to submit the discount in the unit price. In spite of the fact that the discount added as an order rule will be accepted, it is advisable to indicate the discount as unit price. The reason why adding the discount in the unit price is recommened is because of a partial refund. Adding a discount as a seperate discount rule creates an issue with partial refunding because the negative amount cannot be undone. 

{{% note %}} Add the discount as unit price when you process postpaid payment methods {{% /note %}}
{{% /description %}}