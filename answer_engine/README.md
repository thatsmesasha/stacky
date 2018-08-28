# Stacky Answer Engine

## Description
Stacky Answer Engine is a REST API that answers the questions about code. It is trained on StackOverflow dataset.

## Installation

#### Run app

Clone the repository and navigate to this folder. You can either run app locally or using docker image.

##### Locally

Define env variables needed for running:

```
export STACKY_API_PORTN=<STACKY_API_PORT>
```

`<STACKY_API_PORT>` can be any port (for example 5000) that will be used to access the API.

Install requirements and run the app:

```
pip install -r requirements.txt
python app.py
```

##### Docker

Build docker image:

```
docker build -t stacky-answer-engine .
```

Create docker container:

```
docker create -p <STACKY_API_PORT>:5000 --name stacky-answer-engine -t stacky-answer-engine
```

`<STACKY_API_PORT>` can be any port (for example 5000) that will be used to access the API.

Start container:

```
docker start stacky-answer-engine
```

## Endpoints

**`/process`**

This endpoint uses the POST method, and accepts a json object in format:

```
{ "question":"question of the user" }
```

The response will return several elements:

- **electedAnswer**: The answer to question
- **buckets**: One array (ids) of the top answer buckets
- **bestAnswers**: One array (ids) of the elected answers. Elected answers can belong to any answer bucket.

Here's the example of the object:

```
{
    "electedAnswer":"the answer to the question",
    "buckets" : [32, 56, 12],
    "bestAnswers":[ 453, 543, 678 ]
}
```
