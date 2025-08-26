---
title: Pagination
category:
  uri: General
slug: pagination
position: 3
privacy:
  view: public
---
Some requests can return a lot of results. To make responses easier to handle, we paginate the results. You can specify how many results to return using the `limit` parameter.

To view the **next** page of the response, use the `after` cursor from the pager object in the response.\
When you make subsequent requests, use the most recently returned `after` cursor to refresh all pages.
The last page containing data returns an `after` cursor to an empty page.
Further requests to this page are successful, but won’t return any data or new cursors.

To view the **previous** page of the response, use the `before` cursor from the `pager` object.

Results are sorted from newest to oldest, e.g. for `GET /transactions` requests, the `after` cursor points to older transactions.
