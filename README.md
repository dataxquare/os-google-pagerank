# **Pagerank Script for SEO On The Beach 2023**

![Keytrends](https://keytrends.ai/wp-content/uploads/2023/03/nuevo-logo-positivo.png)

&nbsp;
&nbsp;

![SEO On The Beach](https://seonthebeach.es/wp-content/uploads/2022/11/seonthebeach-16-17-junio-2023.png)

This is a script that uses the pagerank algorithm to calculate the pagerank of a set of urls.

We are using the following formula:

![Pagerank Formula](https://www.publisuites.com/blog/wp-content/uploads/2018/07/formula-pagerank-compressor.jpg)

In case you want to change the dataset you only have to load them in the data folder with the following format:

```csv
initial_url,final_url
url1,url2
url1,url3
url2,url3
```

## How to run

1. Install `poetry` from https://python-poetry.org/docs/#installation
2. Run `poetry install`
3. Run `poetry run start`

As pagerank is a iterative algorithm, you can change the number of iterations, if you only want to test the algorithm you can use a small number of iterations, but if you want to get the real pagerank you should use a big number of iterations.

We do not recommend to run a lot of iterations as pagerank is very computationally expensive.