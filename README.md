# GhibliGAN

> A style-transfer project implemented using [CycleGAN](https://arxiv.org/abs/1703.10593).

## Build Setup

```bash
# install package manager
pip install pipenv

# install dependencies
pipenv install
```

## Code Quality

```bash
# get linter aggregate statistics
pipenv run pycodestyle --statistics -qq --config pycodestyle.cfg src

# lint a specific file(s)
pipenv run pycodestyle --first --show-source --config pycodestyle.cfg <file>
```


