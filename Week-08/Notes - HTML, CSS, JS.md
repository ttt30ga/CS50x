# CS50 Week 8 - HTML, CSS, JS

[Watch lecture on Youtube](https://youtu.be/2VauFS071pg)

---

## TCP/IP

`TCP/IP` Transmission Control Protocol - Internet Protocol.\
`IP Addresses` Internet Protocol Addresses.

- `IP` address looks like this `255.255.255.255`
- Binary 255 = 11111111
- each number is represented by `8 bits` of information
- totals 32 bits per IP address.
- new protocol `IPv6` for a `128-bit` address, this allows for more addresses on the internet.
- packets can be divided into multiple packets which may take different routes to get to the receiver making it faster to send and receive data.

**Ports**

| Service | Port | Common Use               |
| ------- | ---- | ------------------------ |
| FTP     | 21   | File Transfer            |
| SMTP    | 25   | Email (Send and Receive) |
| HTTP    | 80   | Website                  |
| HTTPS   | 443  | Secure Website           |
| ...     | ...  | Many other ports         |

## DNS

Domain Name System

- A mapping between URLs and IP Addresses.
- Top Level Domain (TLD): denotes the type of website you are trying to visit, such as `.com`, `.edu`, etc. There really is no "hard rules" on domain types anymore though, expect for specific TLD that are still assigned to a specific type of website, such as `.org`, `.edu`, etc.

**DNS**

| URL         | IP Address    |
| ----------- | ------------- |
| google.com  | 172.217.7.206 |
| harvard.edu | 23.22.75.102  |
| yale.edu    | 104.16.243.4  |

## HTTP Requests and Responses

Hyper-Text Transfer Protocol

`https://www.example.com/folder/file.html`

> Above: Domain / Folder / HTML file

**HTTP Methods**

The define how to send information from you to the server:

```
GET / HTTP/1.1
Host: www.example.com
...
```

> Above: HTTP header request example

**curls**

```
$ curl -I -X GET https://www.harvard.edu

HTTP/2 200
cache-control: public, max-age=1200
content-type: text/html; charset=UTF-8
link: <https://www.harvard.edu/wp-json/>; rel="https://api.w.org/"
link: <https://www.harvard.edu/wp-json/wp/v2/pages/6392>; rel="alternate"; type="application/json"
...
```

> Above: cli command to simulate a `GET` request

`GET` request data from a specified resource.\
`POST` send data to a server to create/update a resource.\
`Status Codes` are how the response was handled.

| Status Code | Description           |
| ----------- | --------------------- |
| 200         | OK                    |
| 301         | Moved Permanently     |
| 302         | Found                 |
| 304         | Not Modified          |
| 307         | Temporary Redirect    |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 418         | I'm a Teapot          |
| 500         | Internal Server Error |
| 503         | Service Unavailable   |

## HTML

Hyper-Text Markup Language

The language that describes the structure of a webpage.

## http-server

You can run your own server locally.

```
$ http-server
```

## Tags and Attributes

`Tags` are like keywords which defines that how web browser will format and display the content.

```
<p> Paragraph Tag </p>
<h2> Heading Tag </h2>
<b> Bold Tag </b>
<i> Italic Tag </i>
<u> Underline Tag</u>
```

`Semantic Tags` are elements that clearly describes its meaning to both the browser and the developer.

```
<article>
<aside>
<details>
<figcaption>
<figure>
<footer>
<header>
<main>
<mark>
<nav>
<section>
<summary>
<time>
```

`HTML attributes`\
Provide additional information about HTML elements.

- All HTML elements can have attributes
- Attributes provide additional information about elements
- Attributes are always specified in the start tag
- Attributes usually come in name/value pairs like: name="value"

## CSS

CSS describes how HTML elements should be displayed.

## CSS Classes

```
.intro {
  background-color: yellow;
}
```

> Above: Select and style all elements with class="intro"

## ID Selectors

```
#firstname {
  background-color: yellow;
}
```

> Above: Style the element with id="firstname"

## Pseudo-classes

A pseudo-class is used to define a special state of an element.

```
selector:pseudo-class {
  property: value;
}
```

```
/* unvisited link */
a:link {
  color: #FF0000;
}

/* visited link */
a:visited {
  color: #00FF00;
}

/* mouse over link */
a:hover {
  color: #FF00FF;
}

/* selected link */
a:active {
  color: #0000FF;
}
```

## JavaScript

JavaScript is the world's most popular programming language.

## onsubmit

```
<form onsubmit="myFunction()">
  Enter name: <input type="text">
  <input type="submit">
</form>
```

## querySelector

```
document.querySelector("p");
```

> Above: Get the first `<p>` element

```
document.querySelector(".example");
```

> Above: Get the first element with class="example"

## Event Listeners

```
document.getElementById("myBtn").addEventListener("click", displayDate);
```

> Above: Add an event listener that fires when a user clicks a button

`Mouse Events`

| Event       | Event Handler |
| ----------- | ------------- |
| click       | onclick       |
| mouseover   | onmouseover   |
| mousedown   | onmousedown   |
| mouseout    | onmouseout    |
| mouseup     | onmouseup     |
| mouseremove | onmouseremove |

`Keyboard Events`

| Event   | Event Handler |
| ------- | ------------- |
| keydown | onkeydown     |
| keyup   | onkeyup       |

`Form Events`

| Event  | Event Handler |
| ------ | ------------- |
| focus  | onfocus       |
| submit | onsubmit      |
| blur   | onblur        |
| change | onchange      |

`Window/Document Events`

| Event  | Event Handler |
| ------ | ------------- |
| load   | onload        |
| unload | onunload      |
| resize | onresize      |

## Anonymous Functions

```
document.queryselector("form").addEventListener("submit", function() {
    let name = document.querySelector("#name").value:
    alert("Hello " + name);
    e.preventDefault()
});
```

> Above: Example of anonymous function
