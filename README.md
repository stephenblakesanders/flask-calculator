# Flask Calculator

Very simple calculator built using the FLASK framework in Python

The calculator works by creating an annay of operands and numbers based on the pressed keys. When the **"="** is pressed the frontend makes an ajax post to a flask endpoint - passing the array of operands and numbers (stored as strings) as a JSON object. Python does the calculations on the backend and returns the result as the response to the ajax POST request.


## FLASK API REeference

#### POST Array for calculations

```http
  POST /data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `arr`     | `Array of strings`  | No authentification - only used locally |


Returns the result of the calculation array
