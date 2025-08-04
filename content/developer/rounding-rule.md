---
title: Rounding rule
category:
  uri: Developers
slug: rounding-rule
position: 5
privacy:
  view: public
---
MultiSafepay applies the following rounding rule when calculating the total cost of an order:

1. Calculate the total cost of all items in the shopping cart (excluding VAT): Multiply the `unit_price` of each item by the `quantity` of the item, then add the results together, rounding to 2 decimal places= Items total.
2. Calculate the total VAT for all items in the cart (if applicable): Multiply the total cost of each item by the VAT rate, then add the results together, rounding to 2 decimal places= VAT total.
3. Add the items total to the VAT total= Cart total.

  **💡 Tip!** When rounding to 2 decimal places, always <a href="https://en.wikipedia.org/wiki/Rounding#Round_half_up" target="_blank">round half up</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />.

Apply the same rounding rule in your integration to ensure:

* The order `amount` matches the cart total.
* [Payment pages](/docs/payment-pages/) display the correct (sub)totals.
* [E-Invoices](/docs/e-invoicing/) to your customers match your records.

For more information about the `shopping_cart` object, see Recipe – <a href="https://docs.multisafepay.com/recipes/create-a-fastcheckout-page" target="_blank">Include shopping\_cart in order</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />.

## Example

For the following order:

```json Order object
...
"shopping_cart":{
  "items":[
    {
      "name":"Product 1",
      "description":"",
      "unit_price":13.761467889,
      "quantity":2,
      "merchant_item_id":"00001",
      "tax_table_selector":"BTW9",
      "weight":{
        "unit":"KG",
        "value":12
      }
    },
    {
      "name":"Product 2",
      "description":"",
      "unit_price":8.2644628099,
      "quantity":4,
      "merchant_item_id":"00002",
      "tax_table_selector":"BTW21",
      "weight":{
        "unit":"KG",
        "value":1
      }
    },
    {
      "name":"Shipping",
      "description":"",
      "unit_price":4.5412844037,
      "quantity":1,
      "merchant_item_id":"msp-shipping",
      "tax_table_selector":"BTW9",
      "weight":{
        "unit":"KG",
        "value":0
      }
    }
  ]
},
"checkout_options":{
  "tax_tables":{
    "default":{
      "shipping_taxed":true,
      "rate":0.21
    },
    "alternate":[
      {
        "name":"BTW21",
        "standalone":true,
        "rules":[
          {
            "rate":0.21
          }
        ]
      },
      {
        "name":"BTW9",
        "standalone":true,
        "rules":[
          {
            "rate":0.09
          }
        ]
      },
      {
        "name":"none",
        "standalone":false,
        "rules":[
          {
            "rate":0
          }
        ]
      }
    ]
  }
}
...
```

| Item name | Unit price   | VAT % | VAT per item | Quantity | Total excl. VAT | Total incl. VAT |
| --------- | ------------ | ----- | ------------ | -------- | --------------- | --------------- |
| Product 1 | 13.761467889 | 9%    | 1.2385321101 | 2        | 27.5229357798   | 30.00           |
| Product 2 | 8.2644628099 | 21%   | 1.7355371901 | 4        | 33.0578512396   | 40.00           |
| Shipping  | 4.5412844037 | 9%    | 0.4087155963 | 1        | 4.5412844037    | 4.95            |
| Total     |              |       |              |          |                 | 74.95           |

1. Calculate the total cost of all items in the shopping cart (excluding VAT): Multiply the `unit_price` of each item by the `quantity` of the item, then add the results together, rounding to 2 decimal places= Items total.

> 13.7614678899 \* 2 = 27.5229357798\
> 8.2644628099 \* 4 = 33.0578512396
> 4.5412844037 \* 1 = 4.5412844037
> 27.5229357798 + 33.0578512396 + 4.5412844037 = **65.1220714231**
> 65.1220714231 = **65.12**

2. Calculate the total VAT for all items in the cart (if applicable): Multiply the total cost of each item by the VAT rate, then add the results together, rounding to 2 decimal places= VAT total.

> 13.7614678899 \* 2 \* 0.09 = 2.4770642202\
> 8.2644628099 \* 4 \* 0.21  = 6.9421487604
> 4.5412844037 \* 0.09 = 0.4087155963
> 2.4770642202 + 6.9421487604 + 0.4087155963 = **9.8279285769**
> 9.8279285769 = **9.83**

3. Add the items total to the VAT total= Cart total.

> 65.12 + 9.83 = **74.95**

## Implementation

Use the following code to implement the rounding convention:

```python Python
# Step 1: Calculate the total cost of all items in the cart (excluding VAT). Multiply the unit_price of each item by the quantity of the item, then add the results together, rounding to 2 decimal places: items_total.
items_total = 0
for item in order.shopping_cart.items:
  items_total += item.unit_price * item.quantity
items_total = round(items_total, 2)

# Step 2: Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to 2 decimal places: vat_total.
vat_total = 0
for item in order.shopping_cart.items:
  for tax_class in order.checkout_options.tax_tables.alternate:
    if tax_class.name == item.tax_table_selector:
      vat_total += item.unit_price * item.quantity * tax_class.rules[0].rate
      break
  else:
    vat_total += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate
vat_total = round(vat_total, 2)

# Step 3: Add the items total to the VAT total: cart_total.
cart_total = items_total + vat_total
```
```javascript Node.js
// Step 1: Calculate the total cost of all items in the cart (excluding VAT). Multiply the unit_price of each item by the quantity of the item, then add the results together, rounding to 2 decimal places: itemsTotal.
let itemsTotal = 0;
for (const item of order.shopping_cart.items) {
  itemsTotal += item.unit_price * item.quantity;
}
itemsTotal = Math.round(itemsTotal * 100) / 100;

// Step 2: Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to 2 decimal places: vatTotal.
let vatTotal = 0;
for (const item of order.shopping_cart.items) {
  for (const tax_class of order.checkout_options.tax_tables.alternate) {
    if (tax_class.name == item.tax_table_selector) {
      vatTotal += item.unit_price * item.quantity * tax_class.rules[0].rate;
      break;
    }
  }
  if (vatTotal == 0) {
    vatTotal += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate;
  }
}
vatTotal = Math.round(vatTotal * 100) / 100;

// Step 3: Add the items total to the VAT total: cartTotal.
cartTotal = itemsTotal + vatTotal;
```
```ruby Ruby
# Step 1: Calculate the total cost of all items in the cart (excluding VAT). Multiply the unit_price of each item by the quantity of the item, then add the results together, rounding to 2 decimal places: items_total.
items_total = 0
order.shopping_cart.items.each do |item|
  items_total += item.unit_price * item.quantity
end
items_total = items_total.round(2)

# Step 2: Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to 2 decimal places: vat_total.
vat_total = 0
order.shopping_cart.items.each do |item|
  tax_class = order.checkout_options.tax_tables.alternate.find { |tax_class| tax_class.name == item.tax_table_selector }
  if tax_class
    vat_total += item.unit_price * item.quantity * tax_class.rules[0].rate
  else
    vat_total += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate
  end
end
vat_total = vat_total.round(2)

# Step 3: Add the items total to the VAT total: cart_total.
cart_total = items_total + vat_total
```
```csharp C#
// Step 1: Calculate the total cost of all items in the cart (excluding VAT). Multiply the unit_price of each item by the quantity of the item, then add the results together, rounding to 2 decimal places: items_total.
var items_total = 0;
foreach (var item in order.shopping_cart.items) {
  items_total += item.unit_price * item.quantity;
}
items_total = Math.Round(items_total, 2);

// Step 2: Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to 2 decimal places: vat_total.
var vat_total = 0;
foreach (var item in order.shopping_cart.items) {
var tax_class = order.checkout_options.tax_tables.alternate.FirstOrDefault(tax_class => tax_class.name == item.tax_table_selector);
if (tax_class != null) {
  vat_total += item.unit_price * item.quantity * tax_class.rules[0].rate;
} else {
  vat_total += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate;
}
}
vat_total = Math.Round(vat_total, 2);

// Step 3: Add the items total to the VAT total: cart_total.
cart_total = items_total + vat_total;
```
```go Go
// Step 1: Calculate the total cost of all items in the cart (excluding VAT). Multiply the unit_price of each item by the quantity of the item, then add the results together, rounding to 2 decimal places: items_total.
var items_total = 0
for _, item := range order.shopping_cart.items {
  items_total += item.unit_price * item.quantity
}
items_total = math.Round(items_total, 2)

// Step 2: Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to 2 decimal places: vat_total.
var vat_total = 0
for _, item := range order.shopping_cart.items {
  tax_class := order.checkout_options.tax_tables.alternate.Find(tax_class => tax_class.name == item.tax_table_selector)
  if tax_class != nil {
    vat_total += item.unit_price * item.quantity * tax_class.rules[0].rate
  } else {
    vat_total += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate
  }
}
vat_total = math.Round(vat_total, 2)

// Step 3: Add the items total to the VAT total: cart_total.
cart_total = items_total + vat_total
```

<br />

***

<blockquote>
  <h3>
    <span>💬</span>
    Support
  </h3>

  <p>Email <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
