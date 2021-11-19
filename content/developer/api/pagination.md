---
title: "API request pagination"
weight: 7
meta_title: "API request pagination - MultiSafepay Docs"
read_more: "."
---

Some requests can return a lot of results, e.g. `GET /transactions`. To make responses easier to handle, we paginate the results. You can specity how many results to return per request using the `limit` parameter. 

To access the next page of the response, use the `after` cursor from the `pager` object in the response. When you make subsequent requests, use the most recently returned `after` cursor to refresh all pages. The last page containing data returns an `after` cursor to an empty page. Further requests to this page are succesful, but won't return any data or new cursors. 

To access the previous page of the response, use the `before` cursor from the `pager` object.

Results are sorted from newest to oldest, e.g. for `GET /transactions` requests, the `after` cursor points to older transactions.
