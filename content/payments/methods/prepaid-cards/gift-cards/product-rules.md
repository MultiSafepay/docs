---
title: "Gift cards product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Gift card product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/gift-cards/product-rules/'
aliases: 
    - /payment-methods/prepaid-cards/gift-cards/open-loop-vs-closed-loop
    - /payment-methods/gift-cards/which-gift-cards-are-accepted-by-multisafepay/
    - /payments/methods/prepaid-cards/gift-cards/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Belgium, the Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Redirect](/api/#gift-cards) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | Doesn't apply | |
| **Adjust payment link lifetimes**  | Yes, if using a gift card and another payment method. | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Open loop vs closed loop" >}}
Gift cards can be open-loop (redeemable at multiple merchants) or closed-loop (redeemable at one specific merchant). For more information, see [About open-loop and closed-loop gift cards](/payments/methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop/).

In addition to accepting established gift card issuers, you can also [create your own custom gift card](/payments/methods/prepaid-cards/gift-cards/user-guide/creating-custom-gift-cards/).

{{< /details >}}

{{< details title="Supported gift cards" >}}

MultiSafepay supports the following gift cards as standard:

- [Baby Cadeaubon](https://www.babycadeaubon.nl/)
- [Wellness & Beauty](https://www.wellnessbeautycadeau.nl/page/hoe-het-werkt/)
- [Boekenbon](https://bestel.boekenbon.nl/)
- [Fashioncheque](https://www.fashioncheque.com/) 
- [Fashion Giftcard](https://www.fashion-giftcard.nl/)
- [Nationale Fietsenbon](https://www.nationalefietsprojecten.nl/pageid=936/Fietsbon.html) 
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome/)
- [Good4fun](https://www.good4fun.nl/)
- [Klus Cadeau](https://www.kluscadeau.nl/)
- [Nationale Tuinbon](https://www.nationale-tuinbon.nl/)
- [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl/) 
- [Podium Cadeaukaart](https://www.podiumcadeaukaart.nl/)
- [Sport & Fit](https://www.sportenfitcadeau.nl/) 
- [Sports Gift Card](https://www.sports-giftcard.com/)
- [VVV Cadeaukaart](https://www.vvvcadeaukaarten.nl/) 
- [Webshop Giftcard](https://www.webshopgiftcard.nl/)
- [Wellness Giftcard](https://www.wellnessgiftcard.nl/) 
- [Wijn Cadeaukaart](https://www.wijn-cadeaukaart.nl/) 
- [Winkelcheque](https://www.winkelcheque.nl/) 
- [YourGift](https://www.yourgift.nl/)

**Note:** Webshop Giftcard no longer offers [open-loop gift cards](/payments/methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop). To exchange existing open-loop cards for closed-loop cards, see Webshop Giftcard – [Contact](https://www.webshopgiftcard.nl/contact).

{{< /details >}}

{{< details title="Paying with multiple cards" >}}

For [open-loop gift cards](/payments/methods/prepaid-cards/gift-cards/user-guide/open-closed-loop/):

- The maximum credit value is 150 EUR.
- The maximum amount per transaction is 50 EUR. Any outstanding amount must be paid using another payment method.

{{< /details >}}

{{< details title="Pay later methods" >}}
&nbsp;  
[Pay later methods](/payments/methods/billing-suite/) do not generally support entering gift card details for partial payments or **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, pay later methods require very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Refunds" >}}

- You cannot refund more than the original transaction value.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- For transactions paid with a gift card in full: You can't refund these from your MultiSafepay balance because we don't receive any payment details or bank account details from the customer to refund to. You can refund these transactions in your own online banking environment. 

- Transactions paid with a gift card **and** another payment method (e.g. iDEAL): You can refund these in full from your MultiSafepay balance. Follow these steps:

    1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
    2. Go to **Transactions** > **Transaction overview**.
    3. Search for the transaction and click to open the **Transaction details** page.
    4. Click **Refund order** > **Full refund**.
    5. Click **Save**.
&nbsp;  

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}



