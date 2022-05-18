---
title: 'Gift cards'
weight: 240
meta_title: "Payment methods - Gift cards - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/VVV_Giftcards.svg'
short_description: 'Accept payments using a wide range of Dutch gift cards.'
url: '/payment-methods/gift-cards/'
aliases: 
    - /payment-methods/gift-cards/
    - /payment-methods/prepaid-cards/gift-cards/branded-personalized-gift-card/
    - /payment-methods/giftcards/branded-personalized-gift-card/
    - /payment-methods/prepaid-cards/gift-cards
    - /payments/methods/prepaid-cards/gift-cards/
    - /payment-methods/prepaid-cards/gift-cards/open-loop-vs-closed-loop
    - /payment-methods/gift-cards/which-gift-cards-are-accepted-by-multisafepay/
    - /payments/methods/prepaid-cards/gift-cards/about/
    - /payments/methods/gift-cards/product-rules/
    - /payment-methods/gift-cards/product-rules/
    - /payment-methods/gift-cards/overview/
    - /payment-methods/gift-cards/how-do-gift-cards-work
    - /payments/methods/prepaid-cards/gift-cards/payment-flow/
    - /payment-methods/gift-cards/payment-flow/
    - /payment-methods/gift-cards/test-gift-cards
    - /payments/methods/prepaid-cards/gift-cards/integration-and-testing/
    - /payment-methods/gift-cards/integration-testing/
    - /payment-methods/prepaid-cards/gift-cards/activate-gift-cards/
    - /payments/methods/prepaid-cards/gift-cards/activation/
    - /payment-methods/gift-cards/activation/
    - /payment-methods/prepaid-cards/gift-cards/open-loop-vs-closed-loop
    - /payments/methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop/
    - /payment-methods/gift-cards/open-loop-closed-loop/
    - /payment-methods/gift-cards/branded-personalized-gift-card/
    - payment-methods/prepaid-cards/gift-cards/custom-gift-cards
    - /payments/methods/prepaid-cards/gift-cards/user-guide/creating-custom-gift-cards/
    - /payment-methods/gift-cards/custom-cards/
    - /payments/methods/prepaid-cards/gift-cards/user-guide/handling-errors/
    - /payment-methods/gift-cards/handling-errors/
    - /payment-methods/gift-cards/pay-later-methods/
---
Gift cards are pre-loaded with a specific amount of credit that customers can use to make online or POS payments. Customers can use gift cards to pay for a transaction in full or in part, and make up the rest with another payment method. Gift card payments are processed by the card issuer.

[See how gift cards can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/giftcards)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | Belgium, The Netherlands  | 
| **Currencies** | EUR  | 
| **Chargebacks** | No  | 
| **Refunds** | Paid with gift card only: <br> You can't refund via MultiSafepay because we don't receive any customer payment details to refund to. Refund in your own online banking. <br> Paid with gift card **and** another payment method: <br> [Full refunds](/payments/refunds/).  |
| **Transactions expire after** | Doesn't apply |

{{< details title="Supported gift cards" >}} 

| | |
|---|---|
| [Baby Cadeaubon](https://www.babycadeaubon.nl/) | [Kids' Cadeau](https://www.dekidscadeaukaart.nl/) |
| [Beauty Cadeau](https://www.beautycadeau.nl/) | [Klus Cadeau](https://www.kluscadeau.nl/) |
| [Wellness & Beauty](https://www.wellnessbeautycadeau.nl/) | [Nationale Bioscoopbon](https://www.bioscoopbon.nl/) |
| [Biercheque](https://biercheque.nl/) | [Nationale Entertainment Card](https://www.nationale-entertainmentcard.nl/) |
| [Bloemen Cadeaukaart](https://www.bloemen-cadeaukaart.nl/) | [Nationale Tuinbon](https://www.nationale-tuinbon.nl/) |
| [Boekenbon](https://bestel.boekenbon.nl/) | [Ohmygood Giftcard](https://ohmygood.nl/) |
| [Boeken Voordeel](https://www.boekenVoordeel.nl/) | [Speelgoedwinkel Cadeaukaart](https://www.speelgoedwinkel.nl/) |
| [Fashioncheque](https://www.fashioncheque.com/) | [Sport & Fit](https://www.sportenfitcadeau.nl/) |
| [Fashion Giftcard](https://www.fashion-giftcard.nl/) | [Sports Gift Card](https://www.sports-giftcard.com/) |
| [Gezondheidsbon](https://www.gezondheidsbon.nl/) | [VVV Cadeaukaart](https://www.vvvcadeaukaarten.nl/) |
| [Good4fun](https://www.good4fun.nl/) | [Wijn Cadeaukaart](https://www.wijn-cadeaukaart.nl/) |
| [Huis & Tuin Cadeau](https://www.huisentuincadeau.com/) | [YourGift](https://www.yourgift.nl/) |

**Note:** Webshop Giftcard no longer offers [open-loop gift cards](/payments/methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop). To exchange existing open-loop cards for closed-loop cards, see Webshop Giftcard – [Contact](https://www.webshopgiftcard.nl/contact).

{{< /details >}}

### Closed-loop vs open-loop cards

| Format | Redeem with | Amount limits |
|---|---|---|
 Closed-loop | 1 merchant only | None |
| Open-loop | Multiple merchants | Max credit: 150 EUR <br> Max transaction amount: 50 EUR <br> Amounts over 50 EUR must be paid with an additional payment method. |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant G as Gift card issuer
    participant Me as Merchant

    C->>Mu: Selects a gift card at checkout
    Mu->>C: Redirects to payment page
    C->>G: Enters gift card details and completes payment
    G->>Mu: Processes payment and transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| For partial payment with another method: The customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Gift cards activation](/payments/activating-payment-methods/#gift-cards) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#prepaid-cards) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Gift card redirect |
| **Ready-made integrations** | We don’t support all open-loop gift cards in our [ready-made integrations](/integrations/ready-made/) and no closed-loop gift cards. Therefore in some integrations, we use [generic gateways](/developer/general/generic-gateways/). {{< br >}} To check if a specific gift card is supported in your ready-made integration, email the Integration Team at integration@multisafepay.com   |

### Pay later methods

{{< details title="Using gift cards with pay later methods" >}}

When paying with a gift card and a [pay later method](/payments/methods/pay-later/), customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because pay later methods collect and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

{{< /details >}}

### Custom gift cards

{{< details title="Creating custom gift cards" >}}
Contact MultiSafepay to develop your own custom gift card! 

1. Email a request to <sales@multisafepay.com> 
2. MultiSafepay:
    - Checks the payment method rules 
    - Assesses the feasibility of developing the card and estimates the timeframe 
3. Send us:
    - Whether you want a closed-loop or open-loop card
    - The card name 
    - A high-resolution visual mockup of the gift card, preferably in .png or .jpg format, showing the logo as **large** as possible
    - A test gift card with credit and a secure code
    - A startup fee of 200 EUR
4. We develop the card and activate it for your MultiSafepay account.
5. To integrate your card:
    - Using our API, see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order.
    - In a ready-made integration, use our [generic gateway ID](/developer/generic-gateways/).

For support, email <integration@multisafepay.com>
{{< /details >}}

### Known error

{{< details title="VVV Cadeaukaart" >}}

VVV Cadeaukaart cards can sometimes throw an error where the credit balance appears to be 0, but is then restored within 24 hours (potentially affected by weekends and holidays). This appears to be due to temporary failures in the card issuer's system. 

If a customer completes a payment and receives this error message, advise them to wait for 1 hour for a confirmation email before trying again to avoid placing two orders.

{{< /details >}}