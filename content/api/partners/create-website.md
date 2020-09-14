---
weight: 720
meta_title: "API - Create a Webshop for a Partner - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
> POST - /websites

```shell 
{
    "partner": {
      "api_user": "partner-account-user-name",
      "api_pass": "partner-account-password",
    },
    "url": "https://yourpartnerdomain.com",
    "return_url": "http://www.example.com/client/notification?type=notification",
    "description": "",
    "category": "100"
}
```

> JSON Response

```shell 
{
  "success": true,
  "data": {
    "site_id": null,
    "secure_code": null,
    "api_key": "null
  }
}
```
{{< /code-block >}}

{{< description >}}
## Create a website profile in MultiSafepay Control

**Parameters**

----------------
__url__ | string

 Webshop URL.

----------------
__return_url__ | string

 Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work) 

----------------
__description__ | string

 The description will be shown on the payment pages and depending on the payment method also shown on the bank or credit statement of your customer. 

----------------
__category__ | string

Select a category related to the webshop. See list below. 

----------------
__partner__ | object

----------------
__api_user__ | string

User ID of partner account.   

----------------
__api_pass__ | string

Password for partner account.

----------------

| Code | Type                  |
|----------|-----------------------|
| 100     | Gifts and gadgets               |
| 101     | Electronics and computers              |
| 102     | Games                  |
| 103     | Health         |
| 104     | House and Garden                   |
| 105     | Office supplies                  |
| 106     | Kids and toys                |
| 107     | Nutrition              |
| 108     | Fashion and care            |
| 109     | Music, movies and books              |
| 110     | Sport, leisure and hobby          |
| 111     | Phone and internet |
| 112     | Holiday and travel |
| 113     | Sale and auctions |
| 114     | Other |
{{% /description %}}