# HZS Api - Importer

![Pipeline](https://github.com/HZS-Api/Importer/workflows/Pipeline/badge.svg)

- Lambda function, that is importing data from [HZS](https://www.hzscr.cz/clanek/aktualni-vyjezdy.aspx) web and pushing the data to RDS DB


## Local Developement

- Using [Python Lambda Local](https://github.com/HDE/python-lambda-local)
    ```bash
    python-lambda-local -f lambda_handler  ./src/handlers/import.py ./local/importer_event.json 
    ```

## Links

- [pytest](https://docs.pytest.org/en/latest/contents.html)
