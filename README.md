[comment]: <> (![Logo of the project]&#40;https://raw.githubusercontent.com/jehna/readme-best-practices/master/sample-logo.png&#41;)
<img src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/vci19cxv42sbhs9tb9no" width="25%" height="25%">

# Dockerized Text Binary Classification API

Here I used a model from huggingface to perform a binary text classification
on a list of strings with positive and negative tags. I set up an API with Django
and then  dockerized it.

The model name is _distilbert-base-uncased-finetuned-sst-2-english_ which is highly rated one among text classification categories 
in huggingface. It is based on BERT(distilled version). Based on the description it can achieve This model reaches an accuracy of 91.3  





## Installing / Getting started
Simply use the following command
```shell
docker-compose up
```
This command start to create the dockers in two services [python](https://github.com/sdb-tbs/Task2/tree/main/docker/python) and [ngnix](https://github.com/sdb-tbs/Task2/tree/main/docker/ngnix)


## How to use
with [API_demo](https://github.com/sdb-tbs/Task2/blob/main/API_demo.ipynb) you can see a sample. You can also use following code to run a sample:


Sample request:
```shell
curl --location --request POST 'http://localhost/classify/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "string_list" : ["today the weather is good"]
}'
```

Sample response:
```shell
{
  'today the weather is good' : 'POSITIVE'
}
```



## Features

 
* Text sentiment classification with POSITIVE and NEGATIVE tags
* Accept input data as a list which helps to use bulk data 
* It works with docker , so it's easy to install and config 
* Include validation
* Able to handle errors

## Configuration

In [text_classification](https://github.com/sdb-tbs/Task2/blob/main/docker/nginx/text_classification.conf) you can change port and server name.
```shell
  server {
    listen 80;
    server_name localhost; 
    ...
```


## Links

- Model links: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

