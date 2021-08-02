---
weight: 900
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

__first_name__ | string | required

The customer’s first name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations. 

__last_name__ | string | required

The customer’s last name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

__address1__ | string | required

The first line of the customer's address. 

__house_number__ | string | required

The customer's house number.   

__zip_code__ | string | required

The customer's ZIP/postal code.                                                 

__city__ | string | required

The customer's city of residence.                                           

__country__ | string | required

The customer’s country of residence.   
Format: [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html).

{{% /description %}}
