---
weight: 603
meta_title: "API Reference - delivery object - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```json 
{
"delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": 39C,
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL"
    
}
```

{{< /code-block >}}

{{< description >}}
## delivery (object)

The delivery information for the shipment.  

Contains:  

**Parameters**

----------------
`first_name` | string | required

The customer’s first name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations. 

----------------
`last_name` | string | required

The customer’s last name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
`address1` | string | required

The first line of the customer's address. 

----------------
`house_number` | string | required

The customer's house number.   

----------------
`zip_code` | string | required

The customer's ZIP/postal code.                                                 

----------------
`city` | string | required

The customer's city of residence.                                           

----------------
`country` | string | required

The customer’s country of residence.   
Format: [ISO 3166-1 country code](https://www.iso.org/iso-3166-country-codes.html).

----------------

{{% /description %}}
