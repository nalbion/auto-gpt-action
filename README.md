# Auto-GPT GitHub Action

This GitHub Action uses Auto-GPT to follow instructions in the issue description.

## Inputs

### `issue_body`

**Required** The body of the issue.

### `openai_key`

**Required** The OpenAI API key.

### `issue_number`

**Required** The number of the issue.

## Usage

To use the `auto-gpt.yml` workflow file, follow these steps:

1. Create a new issue and label it with the `auto-gpt` label.
2. Add the `OPENAI_KEY` and `MODEL_ID` secrets to your repository.
3. Add the following code to your `.github/workflows/auto-gpt.yml` file:

```yaml
name: Auto-GPT

on:
  issues:
    types: [labeled]

jobs:
  resolve-issue:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Run Auto-GPT
      uses: nalbion/auto-gpt-action@v1
      with:
        openai_key: ${{ secrets.OPENAI_KEY }}
        issue_number: ${{ github.event.issue.number }}
        issue_body: ${{ github.event.issue.body }}

```
