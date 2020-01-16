---
weight: 720
meta_title: "API - Create a Webshop for a Partner - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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

JSON Response

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

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| url                         | string    | Webshop URL. 
| return_url                  | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                                                                                    |
| description                 | string    | The description will be shown on the payment pages and depending on the payment method also shown on the bank or credit statement of your customer.                                                                                              | 
| category                    | string    | Select a category related to the webshop. See list below.                                  | 
| partner                     | object    | 
| api_user                    | string    | User ID of partner account.                                                                 | 
| api_pass                    | string    | Password for partner account.                                                               | 

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
| 999     | Adult |
{{% /description %}}