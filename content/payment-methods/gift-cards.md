---
title: 'Gift cards'
category: 6298bd782d1cf4006032e765
order: 402
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: /payment-methods/gift-cards/
---
Gift cards are pre-loaded with a specific amount of credit that customers can use to make online or POS payments. Customers can use gift cards to pay for a transaction in full or in part, and make up the rest with another payment method. Gift card payments are processed by the card issuer.

See how gift cards can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/giftcards).

# Overview

|   |   |
|---|---|
| **Countries**  | Belgium, The Netherlands  | 
| **Currencies** | EUR  | 
| **Chargebacks** | No  | 
| **Refunds** | Paid with gift card only: You can't refund via MultiSafepay because we don't receive any customer payment details to refund to. Refund in your own online banking. <br> Paid with gift card **and** another payment method: [Full refunds](/refunds/).  |
| **Transactions expire after** | Doesn't apply |

<details id="supported-gift-cards">
<summary>Supported gift cards</summary>
<br>

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
<br>

**Note:** Webshop Giftcard no longer offers [open-loop gift cards](/payments/methods/prepaid-cards/gift-cards/user-guide/about-open-closed-loop). To exchange existing open-loop cards for closed-loop cards, see Webshop Giftcard – [Contact](https://www.webshopgiftcard.nl/contact).

</details>

# Payment flow

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
<br>  

# Payment statuses  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| For partial payment with another method: <br> The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| For partial payment with another method: <br> The customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Gift cards activation](/payments/activating-payment-methods/#gift-cards) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#prepaid-cards) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Gift card redirect |
| **Ready-made integrations** | We don’t support all open-loop gift cards in our [ready-made integrations](/integrations/ready-made/) and no closed-loop gift cards. Therefore in some integrations, we use generic gateways to support [custom gift cards](#custom-gift-cards). <br> To check if a specific gift card is supported in your ready-made integration, email the Integration Team at <integration@multisafepay.com>   |


# User guide

## Closed-loop vs open-loop cards

- Closed-loop: 
    - Redeem with 1 merchant only
    - No amount limits
- Open-loop: 
    - Redeem with multiple merchants 
    - Max credit: 150 EUR 
    - Max transaction amount: 50 EUR
    - Amounts over 50 EUR must be paid with an additional payment method.

## Custom gift cards

Contact MultiSafepay to develop your own custom gift card! 

<details id="how-to-request-custom-gift-cards">
<summary>How to request a custom gift card</summary>
<br>

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
    - In a ready-made integration, add your gateway ID.

For support, email <integration@multisafepay.com>

</details>

## Known error

VVV Cadeaukaart cards can sometimes throw an error where the credit balance appears to be 0, but is then restored within 24 hours (potentially affected by weekends and holidays). This appears to be due to temporary failures in the card issuer's system. 

If a customer completes a payment and receives this error message, advise them to wait for 1 hour for a confirmation email before trying again to avoid placing two orders.

## Pay later methods

When paying with a gift card and a [pay later method](/payment-methods/pay-later/), customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because pay later methods collect and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>