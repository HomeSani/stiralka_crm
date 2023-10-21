## Start
- Clone repo:
```shell
git clone git@github.com:HomeSani/stiralka_crm.git
```
- Install dependencies:
```shell
poetry install
```
- Setup [pre-commit](#pre-commit)

## Docs
**Recommendation: USE PyCharm**

### Pre-commit:
- Installation:
1. ```shell
    python -m pip install pre-commit
    ```
    This command install pre-commit as global package
2. Install (download) hooks:
    ```shell
    $ pre-commit install
    $ pre-commit run --all-files
    ```
3. Complete. Add ```Run Git hooks``` in Git settings for Pycharm
