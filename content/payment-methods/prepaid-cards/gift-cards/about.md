---
title: "About gift cards"
breadcrumb_title: 'About gift cards'
weight: 10
meta_title: "About gift cards - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases: 
    - /payment-methods/prepaid-cards/gift-cards/open-loop-vs-closed-loop
    - /payment-methods/gift-cards/which-gift-cards-are-accepted-by-multisafepay/
---

Gift cards are pre-loaded with a specific amount of credit that customers can use to make online or POS payments. Customers can use gift cards to pay for a transaction in full or in part, and make up the rest with another payment method. 

MultiSafepay does **not** process or collect funds for gift card payments. They are processed by the card issuer, which settles the funds directly in your business bank account.

Gift cards can be open-loop (redeemable at multiple merchants) or closed-loop (redeemable at one specific merchant). For more information, see [About open-loop and closed-loop gift cards](/payment-methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop/).

In addition to accepting established gift card issuers, you can also [create your own custom gift card](/payment-methods/prepaid-cards/gift-cards/user-guide/creating-custom-gift-cards/).

{{< details title="Supported gift cards" >}}

MultiSafepay supports the following gift cards as standard:

* Baby Cadeaubon
* Beauty & Wellness
* Boekenbon
* Fashioncheque 
* Fashiongiftcard
* Fietsenbon 
* Gezondheidsbon 
* Good4fun
* Nationale Tuinbon
* Parfumcadeaukaart 
* Podium
* Sport & Fit 
* VVV Cadeaukaart 
* Webshop Giftcard
* Wellness gift card 
* Wijncadeau 
* Winkelcheque 
* YourGift

**Note:** Webshop Giftcard no longer offers [open-loop gift cards](/payment-methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop). To exchange existing open-loop cards for closed-loop cards, see Webshop Giftcard – [Contact](https://www.webshopgiftcard.nl/contact).

{{< /details >}}

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Prepaid card  | |
| **API flow**  | `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Belgium, the Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | From your own online banking environment only  | [More information](/payment-methods/prepaid-cards/gift-cards/user-guide/processing-refunds) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- Customers can pay for an order using multiple gift cards of the same or different types.

- For [open-loop gift cards](/payment-methods/prepaid-cards/gift-cards/user-guide/open-closed-loop/):
    - The maximum credit value is 150 EUR.
    - The maxiumum amount per transaction is 50 EUR. Any outstanding amount must be paid using another payment method.

{{< details title="Post-payment methods" >}}
&nbsp;  
Post-payment methods do not generally support entering gift card details for partial payments or **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, post-payment methods require very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

