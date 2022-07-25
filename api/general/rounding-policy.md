---
title: Rounding rules
category: 623dacddb0cbdd0394b9f5a9
slug: 'rounding-rules'
order: 7
hidden: true
---

MultiSafepay applies the following rounding rules when calculating the total cost of an order:

1. Calculate the total cost of all items in the cart (excluding VAT). Multiply the `unit_price` of each item by the `quantity` of the item. Add the results together, and round to **2 decimal places**: Items total.
2. Calculate the total VAT for all items in the cart (if applicable).
3. Add the items total to the VAT total: Cart total.

Apply the same rounding rules in your integration to ensure:

- The order `amount` matches the cart total.
- MultiSafepay's records match your records.
- E-Invoices to your customers match your records.


## Example

For the following order:

```json Order object
...
"shopping_cart": {
        "items": [
            {
                "name": "Product 1",
                "description": "",
                "unit_price": 13.761467889,
                "quantity": 2,
                "merchant_item_id": "00001",
                "tax_table_selector": "BTW9",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
            {
                "name": "Product 2",
                "description": "",
                "unit_price": 8.2644628099,
                "quantity": 5,
                "merchant_item_id": "00002",
                "tax_table_selector": "BTW21",
                "weight": {
                    "unit": "KG",
                    "value": 1
                }
            },
            {
                "name": "Shipping",
                "description": "",
                "unit_price": 4.5412844037,
                "quantity": 1,
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "BTW9",
                "weight": {
                    "unit": "KG",
                    "value": 0
                }
            }
        ]
    },
    "checkout_options": {
        "tax_tables": {
            "default": {
                "shipping_taxed": true,
                "rate": 0.21
            },
            "alternate": [
                {
                    "name": "BTW21",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.21
                        }
                    ]
                },
                {
                    "name": "BTW9",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.09
                        }
                    ]
                },
                {
                    "name": "none",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                }
            ]
        }
    }
...
```



| Item name | Unit price    | VAT % | VAT per item | Quantity | Total excl. VAT | Total incl. VAT |
|-----------|---------------|-------|--------------|----------|-----------------|-----------------|
| Product 1 | 13.761467889  | 9%    | 1.2385321101 | 2        | 27.5229357798   | 30.00           |
| Product 2 | 8.2644628099  | 21%   | 1.7355371901 | 4        | 33.0578512396   | 40.00           |
| Shipping  | 4.5412844037  | 9%    | 0.4087155963 | 1        | 4.5412844037    | 4.95            |
| Total     |     	        |       |              |          |                 | 74.95           |


1. Calculate the total cost of all items in the cart (excluding VAT). Multiply the `unit_price` of each item by the `quantity` of the item. Add the results together, and round to 2 decimal places: Items total.
> 13.7614678899 \* 2 = 27.5229357798
> 8.2644628099 \* 4 = 33.0578512396
> 4.5412844037 \* 1 = 4.5412844037
> 27.5229357798 + 33.0578512396 + 4.5412844037 = **65.1220714231**
> 65.1220714231 = **65.12**

2. Calculate the total VAT for all items in the cart (if applicable). Multiply the total cost of each item by the VAT rate. Add the results together, and round to **2 decimal places**: VAT total.
> 13.7614678899 \* 2 \* 0.09 = 2.4770642202
> 8.2644628099 \* 2 \* 0.21  = 6.9421487604
> 4.5412844037 \* 0.09 = 0.4087155963
> 2.4770642202 + 6.9421487604 + 0.4087155963 = **9.8279285769**
> 9.8279285769 = **9.83**


3. Add the items total to the VAT total: Cart total.
> 65.12 + 9.83 = **74.95**

## Implementation

Use the following code to implement the rounding convention:

```python Python
# Step 1: Calculate the total cost of the items in the shopping cart (excluding VAT). For each item in the cart, multiply the unit_price by the quantity of the item.
sum_ex_vat = 0
for item in order.shopping_cart.items:
  sum_ex_vat += item.unit_price * item.quantity

# Step 2: Calculate the total VAT for all items in the shopping cart. For each item in the cart, calculate its VAT (if applicable).
sum_vat = 0
for item in order.shopping_cart.items:
  for tax_class in order.checkout_options.tax_tables.alternate:
    if tax_class.name == item.tax_table_selector:
      sum_vat += item.unit_price * item.quantity * tax_class.rules[0].rate
      break
  else:
    sum_vat += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate

#Step 3: Round both totals to two decimal places
sum_ex_vat = round(sum_ex_vat, 2)
sum_vat = round(sum_vat, 2)

#Step 4: Calculate the total cost of the order by adding together the two rounded totals.
amount = sum_ex_vat + sum_vat
```
```javascript Node.js
// Step 1: Calculate the total cost of the items in the shopping cart (excluding VAT). For each item in the cart, multiply the unit_price by the quantity of the item.
let sum_ex_vat = 0;
for (const item of order.shopping_cart.items) {
  sum_ex_vat += item.unit_price * item.quantity;
}

// Step 2: Calculate the total VAT for all items in the shopping cart. For each item in the cart, calculate its VAT (if applicable).
let sum_vat = 0;
for (const item of order.shopping_cart.items) {
  for (const tax_class of order.checkout_options.tax_tables.alternate) {
    if (tax_class.name == item.tax_table_selector) {
      sum_vat += item.unit_price * item.quantity * tax_class.rules[0].rate;
      break;
    }
  }
  if (sum_vat == 0) {
    sum_vat += item.unit_price * item.quantity * order.checkout_options.tax_tables.default.rate;
  }
}

//Step 3: Round both totals to two decimal places
sum_ex_vat = Math.round(sum_ex_vat * 100) / 100;
sum_vat = Math.round(sum_vat * 100) / 100;

//Step 4: Calculate the total cost of the order by adding together the two rounded totals.
amount = sum_ex_vat + sum_vat;
```
```ruby Ruby
# Step 1: Calculate the total cost of the items in the shopping cart (excluding VAT). For each item in the cart, multiply the unit_price by the quantity of the item.
sum_ex_vat = 0
shopping_cart.items.each do |item|
  sum_ex_vat += item.unit_price * item.quantity
end

# Step 2: Calculate the total VAT for all items in the shopping cart. For each item in the cart, calculate its VAT (if applicable).
sum_vat = 0
shopping_cart.items.each do |item|
  tax_class = checkout_options.tax_tables.alternate.find { |tax_class| tax_class.name == item.tax_table_selector }
  if tax_class
    sum_vat += item.unit_price * item.quantity * tax_class.rules[0].rate
  else
    sum_vat += item.unit_price * item.quantity * checkout_options.tax_tables.default.rate
  end
end

 #Step 3: Round both totals to two decimal places
 sum_ex_vat = sum_ex_vat.round(2)
 sum_vat = sum_vat.round(2)

 #Step 4: Calculate the total cost of the order by adding together the two rounded totals.
 amount = sum_ex_vat + sum_vat
```
```csharp C#
// Step 1: Calculate the total cost of the items in the shopping cart (excluding VAT). For each item in the cart, multiply the unit_price by the quantity of the item.
var sum_ex_vat = 0;
foreach (var item in shopping_cart.items) {
  sum_ex_vat += item.unit_price * item.quantity;
}

 // Step 2: Calculate the total VAT for all items in the shopping cart. For each item in the cart, calculate its VAT (if applicable).
 var sum_vat = 0;
 foreach (var item in shopping_cart.items) {
  var tax_class = checkout_options.tax_tables.alternate.FirstOrDefault(tax_class => tax_class.name == item.tax_table_selector);
  if (tax_class != null) {
    sum_vat += item.unit_price * item.quantity * tax_class.rules[0].rate;
  } else {
    sum_vat += item.unit_price * item.quantity * checkout_options.tax_tables.default.rate;
  }
 }

 //Step 3: Round both totals to two decimal places
 sum_ex_vat = Math.Round(sum_ex_vat, 2);
 sum_vat = Math.Round(sum_vat, 2);

 //Step 4: Calculate the total cost of the order by adding together the two rounded totals.
 amount = sum_ex_vat + sum_vat;
```

