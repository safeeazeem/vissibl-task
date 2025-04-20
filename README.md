
## 1. Run Locally


Create a virtual environment

```bash
  python3 -m venv venv
```

Activate the environment

```bash
  source ./venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create `.env` file
```
OPENAI_API_KEY=[YOUR OPENAI KEY]
```

To run, run the following make command. This will read the questionnaire, the ISO template and then generate the result.
```bash
make run
```


## 2. How it works

The documents provided should be formatted as a markdown, this helps the model to perform better.

The company questionnaire's should be saved in 
```
documents/company_information/{QUESTIONNAIRE_NAME.txt}
```

The ISO Template should be saved in 
```
documents/ISO_template/{TEMPLATE_NAME.txt}
```

### 2.1. I dont have have data formatted as a markdown and not in txt format?
I have prepared a script that converts the .docx, .pdf files to txt file formatted in markdown using Microsoft MarkdItDown.

To run the script
```bash
python3 convert_to_markdown.py --input ./documents/ISO_template/Integrated_Management_System_Manual.docx --output test
```

The output would be saved in `converted`, then you can paste them in their corresponding folders.


## 3. How to run the agents.
I have designed two agents, an editor agent and a validation agent. The editor agent fills in the company information in the template. It also generates customized content based on the sections.

To run the agent
```bash
python3 main.py --company [NAME_OF_THE_COMPANY_QUESTIONAIR] --template [TEMPLATE_NAME]
```

```bash
python3 main.py --company alec_engineering.txt --template ims_template.txt
```

The output will be generated in the `output` folder, along with the validation report, which is in a PDF. There are some examples present in the `output` folder.

### 3.1. How to configure the Agent

The agents can be configured from the `prompt` folder, they are defined there. Any placeholder you write in the prompt, needs to be passed as a dictionary to the agent. For example if your prompt is. The placeholder name and the key of the dictionary should be the same. 

```
Greet the user in {input_language} language.
```

Your dictionary should be formatted like this
```python
user_input = {
  "input_language": "German"
}
```

We have 2 agents defined in the `prompts` folder, the `editor` and the `validator`