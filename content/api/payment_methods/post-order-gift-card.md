---
weight: 319
meta_title: "API reference - Create a gift card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - / order 


```json 
{
  "type":"redirect",
  "order_id":"my-order-id",
  "gateway":"VVVGIFTCRD",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "manual":false,
  "payment_options":{
    "notification_url":"https://www.example.com/client/json-live/notification?type=notification",
    "redirect_url":"https://www.example.comclient/json-live/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/json-live/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "country":"NL",
    "email":"simonsmit@example.com"
  }
}
```

> JSON response
```json 
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```  
{{< /code-block >}}

{{< description >}}
## Gift cards

- See also Payment methods – [Gift cards](/payments/methods/prepaid-cards/gift-cards).  
- Redirect only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
**Note:** We only preselect the gift card supplied in the gateway.  

Options:  

- [Baby Cadeaubon](https://www.babycadeaubon.nl/)= `BABYCAD`
- [Beauty Cadeau](https://www.beautycadeau.nl/)= `BEAUTYCAD`
- [Wellness & Beauty](https://www.wellnessbeautycadeau.nl/page/hoe-het-werkt/)= `BEAUTYWELL`
- [Biercheque](https://biercheque.nl/)= `BIERCHEQUE`
- [Bloemen Cadeaukaart](https://www.bloemen-cadeaukaart.nl/)= `BLOEMENCAD`
- [Boekenbon](https://bestel.boekenbon.nl/)= `BOEKENBON`
- [Boeken Voordeel](https://www.boekenVoordeel.nl/)= `BOEKENVOOR`
- [Fashioncheque](https://www.fashioncheque.com/)= `FASHIONCHQ`
- [Fashion Giftcard](https://www.fashion-giftcard.nl/)= `FASHIONGFT`
- [Gezondheidsbon](https://www.gezondheidsbon.nl/)= `GEZONDHEID`
- [Good4fun](https://www.good4fun.nl/)= `GOOD4FUN`
- [Huis & Tuin Cadeau](https://www.huisentuincadeau.com/)= `HUISTUIN`
- [Kids' Cadeau](https://www.dekidscadeaukaart.nl/)= `KIDSCADEAU`
- [Klus Cadeau](https://www.kluscadeau.nl/)= `KLUSCADEAU`
- [Nationale Bioscoopbon](https://www.bioscoopbon.nl/)= `NATNLBIOSC`
- [Nationale Entertainment Card](https://www.nationale-entertainmentcard.nl/)= `NATENCRD`
- [Nationale Tuinbon](https://www.nationale-tuinbon.nl/)= `NATNLETUIN`
- [Ohmygood Giftcard](https://ohmygood.nl/)= `OHMYGOOD`
- [Speelgoedwinkel Cadeaukaart](https://www.speelgoedwinkel.nl/)= `SPEELGOED`
- [Sport & Fit](https://www.sportenfitcadeau.nl/)= `SPORTENFIT`
- [Sports Gift Card](https://www.sports-giftcard.com/)= `SPORTSGIFT`
- [VVV Cadeaukaart](https://www.vvvcadeaukaarten.nl/)= `VVVGIFTCRD`
- [Wijn Cadeaukaart](https://www.wijn-cadeaukaart.nl/)= `WIJNCADEAU`
- [YourGift](https://www.yourgift.nl/)= `YOURGIFT`

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
